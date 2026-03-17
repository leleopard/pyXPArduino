"""
Arduino.py
----------
High-level Arduino controller thread.

:class:`Arduino` sits between the XML configuration layer
(:mod:`lib.arduinoXMLconfig`) and the raw serial layer
(:class:`~lib.arduinoSerial.ArduinoSerial`).  One instance is created per
configured Arduino board.

Responsibilities
~~~~~~~~~~~~~~~~
* **Connection management** — detects the current USB port by serial number
  and opens an :class:`~lib.arduinoSerial.ArduinoSerial` connection.
* **Input routing** — receives input-change callbacks from the serial layer
  and translates them into X-Plane commands / dataref writes via
  ``pyXPUDPServer``.
* **Output refresh** — runs a continuous loop that reads X-Plane dataref
  values and sends the corresponding PWM / servo / digital-output commands to
  the Arduino.
* **Configuration updates** — listens for XML attribute-change callbacks and
  re-sends pin-configuration messages to the firmware when component pin
  assignments change.

Supported input types
~~~~~~~~~~~~~~~~~~~~~
* ``'SW'``     — digital switch (on / off).
* ``'POT'``    — potentiometer (0–1023 ADC value, mapped via interpolation).
* ``'ROTENC'`` — rotary encoder (±N steps, with optional acceleration).

Supported output types
~~~~~~~~~~~~~~~~~~~~~~
* ``'pwm'``       — pulse-width modulation output.
* ``'servo'``     — servo motor position.
* ``'dig_output'``— digital on/off output.
"""

import threading
import lib.arduinoSerial as ardSerial
import lib.serialArduinoUtils
import logging
import time
import re
from operator import itemgetter

logger = logging.getLogger('Arduino')


class Arduino(threading.Thread):
    """Background thread managing a single Arduino board.

    Inherits from :class:`threading.Thread`.  Start the thread with
    :meth:`threading.Thread.start`; stop it cleanly with :meth:`quit`.

    Attributes:
        running (bool): Controls the main output-refresh loop.  Set to
            ``False`` by :meth:`quit` to stop the thread.
        connected (bool): ``True`` when a serial connection has been
            successfully established with the Arduino.
        ardSerialNumber (str): USB serial number used to identify the board.
        ardXMLconfig (arduinoConfig): Reference to the shared XML config
            manager.
        XPUDPServer: Reference to the ``pyXPUDPServer`` instance used to
            send commands and datarefs to X-Plane.
        serialConnection (ArduinoSerial | None): The low-level serial thread,
            or ``None`` if not connected.
    """

    def __init__(self, ardSerialNumber, XPUDPServer, arduinoXMLconfig):
        """Initialise the Arduino thread and attempt an initial serial connection.

        Registers attribute-change callbacks on the XML config manager and
        marks the board as ``'Disconnected'`` / ``'Not Running'`` before
        calling :meth:`connect`.

        Args:
            ardSerialNumber (str): USB serial number of the Arduino board.
            XPUDPServer: ``pyxpudpserver.pyXPUDPServer`` singleton used to
                send X-Plane commands and dataref values.
            arduinoXMLconfig (arduinoConfig): Shared XML configuration
                manager instance.
        """
        threading.Thread.__init__(self)
        self.running = True
        self.connected = False

        self.ardSerialNumber = ardSerialNumber
        self.ardXMLconfig = arduinoXMLconfig
        self.XPUDPServer = XPUDPServer
        self.ardXMLconfig.registerArduinoAttributeChangedCallback(self.handleArduinoAttributeChange)
        self.ardXMLconfig.updateArduinoAttribute(ardSerialNumber, 'connected', 'Disconnected')
        self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'ard_status', 'Not Running')

        self.connect()

    def reconnect(self):
        """Disconnect then immediately reconnect the serial link.

        Called automatically when the baud rate is changed in the
        configuration.  Delegates to :meth:`disconnect` followed by
        :meth:`connect`.
        """
        self.disconnect()
        self.connect()

    def disconnect(self):
        """Close the serial connection and update configuration status flags.

        If the board is currently connected, marks it as ``'Disconnected'``
        and ``'Not Running'`` in the XML config, then stops the
        :class:`~lib.arduinoSerial.ArduinoSerial` thread.
        """
        if self.connected == True:
            self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'connected', 'Disconnected')
            self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'ard_status', 'Not Running')
            self.serialConnection.quit()

    def connect(self):
        """Attempt to establish a serial connection with the Arduino.

        Uses :func:`~lib.serialArduinoUtils.returnArduinoPort` to discover
        the current OS port for this board's serial number (the port may
        change if the Arduino is reconnected to a different USB hub).

        On success:

        * Creates and starts an :class:`~lib.arduinoSerial.ArduinoSerial`
          thread.
        * Registers :meth:`inputChanged` and :meth:`ardStateChanged`
          callbacks on the serial layer.
        * Registers :meth:`updateComponentList` on the XML config manager
          so pin changes are propagated to the firmware.
        * Sends the initial full pin-configuration to the Arduino.

        On failure (board not found or port open error), :attr:`connected` is
        set to ``False`` and a warning/error is logged.
        """
        # Initialise connection, first we will check that the Arduino with this serial nr is still connected on this port
        self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'connected', 'Disconnected')
        self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'ard_status', 'Not Running')
        ardData = self.ardXMLconfig.getArduinoData(self.ardSerialNumber)

        connected_PORT = lib.serialArduinoUtils.returnArduinoPort(self.ardSerialNumber)

        logger.debug("connected_PORT = "+ str(connected_PORT))
        if connected_PORT == None: # then the arduino is not connected, no point trying to get a serial connection going
            self.connected = False
            logger.warning("Arduino serial nr "+self.ardSerialNumber+", unable to connect on port "+ardData['port'])

        else: # the arduino is connected, we will attempt to connect on the the PORT value found as the arduino could have been reconnected to another port
            self.serialConnection = ardSerial.ArduinoSerial(connected_PORT, ardData['baud'])
            if self.serialConnection.connected == True:
                self.serialConnection.registerInputChangedCallback(self.inputChanged)
                self.serialConnection.registerArduinoStateChangedCallback(self.ardStateChanged)
                self.ardXMLconfig.registerComponentAttributeChangedCallback(self.updateComponentList) #
                time.sleep(0.01)

                self.serialConnection.start()

                self.updateComponentList('*', '', self.ardSerialNumber, 'pin') # set the pins as switches on arduino
                self.connected = True
                logger.info("Arduino serial nr "+str(self.ardSerialNumber)+" connected on port: "+str(connected_PORT)+", BAUD: "+ str(ardData['baud']))
            else:
                self.connected = False
                logger.error("Arduino serial nr "+self.ardSerialNumber+", unable to connect on port "+str(connected_PORT)+", BAUD: "+ str(ardData['baud']))

        if self.connected == True:
            self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'connected', 'Connected')
        else:
            self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'connected', 'Disconnected')

    def ardStateChanged(self, ardState, arduinoFirmwareVersion):
        """Handle Arduino ready-state change notifications from the serial layer.

        Updates the ``'ard_status'`` and ``'firmware_version'`` attributes in
        the XML config whenever the Arduino reports its ready state or firmware
        version.  These changes propagate to the UI via registered callbacks.

        Args:
            ardState (bool): ``True`` if the Arduino is ready; ``False`` if
                it has disconnected or not yet booted.
            arduinoFirmwareVersion (str): Firmware version string reported by
                the Arduino (e.g. ``'1.2'``).
        """
        logger.debug('ard state has changed: '+str(self.serialConnection.arduinoReady))
        if ardState == True:
            self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'ard_status', 'Running')
        else:
            self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'ard_status', 'Not Running')

        self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'firmware_version', arduinoFirmwareVersion)

    def handleArduinoAttributeChange(self, ardSerialNr, attribute):
        """React to Arduino-level attribute changes in the XML configuration.

        Currently only acts on baud-rate changes by triggering a full
        :meth:`reconnect` so the serial port is reopened at the new speed.

        Args:
            ardSerialNr (str): Serial number of the Arduino whose attribute
                changed.
            attribute (str): Name of the changed attribute (e.g. ``'baud'``).
        """
        logging.debug("ard attribute changed: "+attribute)
        if attribute == 'baud':
            self.reconnect()

    def run(self):
        """Main thread loop — continuously refresh all configured outputs.

        Do **not** call this method directly.  Use
        :meth:`threading.Thread.start` to launch the thread.

        The loop runs every 10 ms and calls :meth:`__refreshOutputs` for each
        output type (``'pwm'``, ``'servo'``, ``'dig_output'``).  A forced
        refresh is triggered once per second to compensate for any missed
        updates (e.g. after initial connection).

        The loop exits when :attr:`running` is set to ``False`` (via
        :meth:`quit`).
        """
        buffer =""
        startTime = time.time()
        forceRefresh = True
        lastTime = time.time();

        while self.running:
            # obtain list of outputs & associated actions
            if time.time() - lastTime > 1.0:
                forceRefresh = True
                lastTime = time.time()

            if self.connected == True:
                self.__refreshOutputs('pwm', forceRefresh)
                self.__refreshOutputs('servo', forceRefresh)
                self.__refreshOutputs('dig_output', forceRefresh)
                forceRefresh = False # forcing Refresh only on first run of the loop
            time.sleep(0.01)

    def __refreshOutputs(self, outputType, forceRefresh=False):
        """Query X-Plane dataref values and send updated output commands to the Arduino.

        For each component of ``outputType`` assigned to this Arduino:

        1. Reads the current dataref value from ``pyXPUDPServer``.
        2. Compares it to the last known value stored in the action's
           ``'state'`` field.
        3. If the value has changed by more than 0.01, or ``forceRefresh`` is
           ``True``, passes the new value through
           :meth:`__returnLinearInterpolationY` using the component's mapping
           points, and queues the result as a serial output command.

        Args:
            outputType (str): One of ``'pwm'``, ``'servo'``, or
                ``'dig_output'``.
            forceRefresh (bool): If ``True``, sends the output value
                unconditionally, regardless of whether it has changed.
                Defaults to ``False``.
        """
        if self.connected == True:
            compList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, outputType)
            for comp in compList:
                if comp['pin'] != '':
                    compActions = self.ardXMLconfig.getComponentActions(self.ardSerialNumber, outputType, comp['pin'] )
                    for action in compActions:
                        drefValue = self.XPUDPServer.getData(action['cmddref'] + "[" + action['index'] + "]")
                        prevDrefValue = 0.0
                        try:
                            prevDrefValue = float(action['state'])
                        except ValueError:
                            pass
                            logger.warning('Unable to convert dref value, defaulting to 0.0')
                        if (abs(prevDrefValue - drefValue) > 0.01) or forceRefresh == True:
                            action['state'] = str(drefValue)
                            logger.debug(outputType+' XPLANE DREF value, DREF: '+action['cmddref']+' Value: '+str(drefValue))
                            pointsList = self.__returnPointsList(action['setToValue'])
                            outPWMvalue = self.__returnLinearInterpolationY(drefValue, pointsList)
                            logger.debug('Out '+ outputType + ' value: '+ str(outPWMvalue))
                            self.ardXMLconfig.updateComponentActions(self.ardSerialNumber, outputType, comp['pin'], compActions )

                            try:
                                self.serialConnection.sendOutputValue(comp['pin'], outputType, int(outPWMvalue))
                            except:
                                pass  # BUG-03: silent exception swallows serial failures

    def inputChanged(self, inputType, pin, value):
        """Handle an input-state change received from the Arduino serial layer.

        Dispatches to the appropriate handling block based on ``inputType``:

        * **SW (switch)** — maps value 0/1 to ``'off'``/``'on'``, updates the
          component state in the XML config, then iterates over all configured
          actions.  For ``'cmd'`` actions, sends or stops the X-Plane command
          depending on the switch state and the ``continuous`` flag.  For
          ``'dref'`` actions, writes the specified value to the dataref.

        * **POT (potentiometer)** — stores the raw ADC value, then for
          ``'dref'`` actions applies linear interpolation via the configured
          mapping points before writing to X-Plane.  For ``'cmd'`` actions,
          fires the command if the value falls within any configured interval.

        * **ROTENC (rotary encoder)** — determines ``'up'``/``'down'``
          direction from the sign of ``value``.  Applies the ``multiplier``
          and optional acceleration (``abs(value)`` repetitions) to determine
          how many times the X-Plane command is sent.

        This method is registered as a callback on the
        :class:`~lib.arduinoSerial.ArduinoSerial` instance and is called from
        that thread, not from this thread's :meth:`run` loop.

        Args:
            inputType (str): Arduino input type identifier — one of
                ``'SW'``, ``'POT'``, or ``'ROTENC'``.
            pin (int): Arduino pin number that changed.
            value (int): New value on the pin.  Interpretation depends on
                ``inputType``:

                * ``SW`` — ``0`` (off) or ``1`` (on).
                * ``POT`` — raw ADC reading, 0–1023.
                * ``ROTENC`` — signed step count (positive = clockwise).
        """
        if self.connected == True:
            logger.debug("ARD CLASS ard input changed callback, input Type: "+inputType+ ", pin" + str(pin) + " value:" + str(value))
            if inputType == 'SW':
                switch_state = 'on'
                if value == 0 :
                    switch_state = 'off'

                logger.debug('updating switch state to value:' + switch_state)
                compID = self.ardXMLconfig.getComponentAttribute( self.ardSerialNumber,'switch', pin, 'id')
                self.ardXMLconfig.updateComponentAttribute(compID, 'switch', 'state', switch_state)

                for action in self.ardXMLconfig.getComponentActions(self.ardSerialNumber, 'switch', pin):
                    if action['cmddref']!= None:
                        logger.debug ("action type: "+ action['action_type']
                                        + " action state: "+action['state']
                                        + "switch state: " + switch_state
                                        + " action: " + action ['cmddref'] )
                        sendContinuous = False
                        if action['continuous'] == 'True':
                            sendContinuous = True

                        if action['action_type'] == 'cmd' and action['state'] == switch_state:
                            self.XPUDPServer.sendXPCmd(action ['cmddref'], sendContinuous)
                        if action['action_type'] == 'cmd' and action['state'] != switch_state and action['continuous'] == 'True': # suppress any continuous cmd
                            self.XPUDPServer.stopSendingXPCmd(action ['cmddref'])

                        if action['action_type'] == 'dref' and action['state'] == switch_state:
                            self.XPUDPServer.sendXPDref(action['cmddref'],action['index'],action['setToValue'])

            if inputType == 'POT':
                state = str(value)
                compID = self.ardXMLconfig.getComponentAttribute(self.ardSerialNumber, 'potentiometer', pin, 'id')
                self.ardXMLconfig.updateComponentAttribute(compID, 'potentiometer', 'state', state)

                for action in self.ardXMLconfig.getComponentActions(self.ardSerialNumber, 'potentiometer', pin):
                    if action['cmddref']!= None:
                        logger.debug ("action type: "+ action['action_type']
                                        + " action state: "+action['state']
                                        + "pot state: " + state
                                        + " action: " + action ['cmddref'] )

                        if action['action_type'] == 'dref' :
                            logger.debug('DREF set to value:'+action['setToValue'])
                            pointsList = self.__returnPointsList(action['setToValue'])
                            logger.debug('Points list: ' + str(pointsList))
                            if len(pointsList) > 0:
                                outValue = self.__returnLinearInterpolationY(float(state), pointsList)

                                logger.debug('Output value to XP DREF: ' +str(outValue))
                                self.XPUDPServer.sendXPDref(action['cmddref'],action['index'],outValue)

                        if action['action_type'] == 'cmd' :
                            logger.debug('CMD state:'+action['state'])
                            intervalsList = self.__returnPointsList(action['state'])
                            logger.debug('Intervals list: ' + str(intervalsList))
                            if len(intervalsList) > 0:
                                if self.__isValueInIntervals(float(state), intervalsList):
                                    logger.debug('Send XPlane CMD : ' +action['cmddref'])
                                    self.XPUDPServer.sendXPCmd(action['cmddref'])

            if inputType == 'ROTENC':
                acceleration = self.ardXMLconfig.getComponentAttribute( self.ardSerialNumber,'rot_encoder', pin, 'acceleration')
                multiplier = float(self.ardXMLconfig.getComponentAttribute( self.ardSerialNumber,'rot_encoder', pin, 'multiplier'))

                rot_enc_state = 'up'
                if value < 0 :
                    rot_enc_state = 'down'
                if acceleration == 'True':
                    numberTimesSendAction = int(abs(value))
                else:
                    numberTimesSendAction = 1
                numberTimesSendAction = numberTimesSendAction * int(multiplier)

                logger.debug('updating rot encoder state to value:' + rot_enc_state)
                compID = self.ardXMLconfig.getComponentAttribute( self.ardSerialNumber,'rot_encoder', pin, 'id')
                self.ardXMLconfig.updateComponentAttribute(compID, 'rot_encoder', 'state', rot_enc_state)

                for action in self.ardXMLconfig.getComponentActions(self.ardSerialNumber, 'rot_encoder', pin):
                    if action['cmddref']!= None:
                        logger.debug ("action type: "+ action['action_type']
                                        + " action state: "+action['state']
                                        + "rot_encoder state: " + rot_enc_state
                                        + " action: " + action ['cmddref'] )
                        sendContinuous = False
                        if action['continuous'] == 'True':
                            sendContinuous = True

                        if action['action_type'] == 'cmd' and action['state'] == rot_enc_state:
                            for i in range(0, numberTimesSendAction):
                                self.XPUDPServer.sendXPCmd(action ['cmddref'], sendContinuous)
                        if action['action_type'] == 'cmd' and action['state'] != rot_enc_state and action['continuous'] == 'True': # suppress any continuous cmd
                            self.XPUDPServer.stopSendingXPCmd(action ['cmddref'])

                        if action['action_type'] == 'dref' and action['state'] == rot_enc_state:
                            self.XPUDPServer.sendXPDref(action['cmddref'],action['index'],action['setToValue'])

    def updateComponentList(self, componentType, switchSerialNr, ardSerialNr, attribute):
        """Send updated pin-configuration lists to the Arduino firmware.

        Called automatically via the XML config callback whenever a component's
        ``pin``, ``pin2``, or ``stepsPerNotch`` attribute changes, and also
        called explicitly on startup.

        Builds pin lists for each applicable component type and sends them to
        :meth:`~lib.arduinoSerial.ArduinoSerial.sendPinList`.  For rotary
        encoders, the combined string ``'<pinA>,<pinB>,<stepsPerNotch>'`` is
        used as the pin identifier.

        Only acts if ``ardSerialNr`` matches this board's serial number and
        the board is currently connected.

        Args:
            componentType (str): The type of component whose pin changed, or
                ``'*'`` to refresh all component types at once.
            switchSerialNr (str): Unused; preserved for callback interface
                compatibility.
            ardSerialNr (str): Serial number of the Arduino that owns the
                changed component.  Must match :attr:`ardSerialNumber` for
                any action to be taken.
            attribute (str): The attribute that changed.  Action is only taken
                when this is ``'pin'``, ``'pin2'``, or ``'stepsPerNotch'``.
        """
        logger.debug('update component list, component type: '+str(componentType)+ 'attribute: '+str(attribute) )
        if ardSerialNr == self.ardSerialNumber and (attribute == 'pin' or attribute =='pin2' or attribute == 'stepsPerNotch') and self.connected == True: # only update pins if this is us and the attribute that has changed is pin

            if componentType == '*' or componentType == 'switch':
                switchList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'switch')
                switchPinList = []

                for switch in switchList:
                    if switch['pin'] != '':
                        switchPinList.append(switch['pin'])
                logger.debug ('Ard serial '+ self.ardSerialNumber+ 'switch pin list: ' + str(switchPinList))
                self.serialConnection.sendPinList('switch', switchPinList)

            if componentType == '*' or componentType == 'potentiometer':
                compList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'potentiometer')
                compPinList = []

                for comp in compList:
                    if comp['pin'] != '':
                        compPinList.append(comp['pin'])
                logger.debug ('Ard serial '+ self.ardSerialNumber+ 'pot pin list: ' + str(compPinList))
                self.serialConnection.sendPinList('potentiometer', compPinList)

            if componentType == '*' or componentType == 'rot_encoder':
                logger.debug('updating rot_encoder')
                compList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'rot_encoder')
                compPinList = []

                for comp in compList:
                    if comp['pin'] != '' and comp['pin2'] != '' :
                        compPinList.append(comp['pin']+','+comp['pin2']+','+comp['stepsPerNotch'])
                logger.debug ('Ard serial '+ self.ardSerialNumber+ 'rot encoder pin list: ' + str(compPinList))
                self.serialConnection.sendPinList('rot_encoder', compPinList)

            if componentType == '*' or componentType == 'pwm':
                compList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'pwm')
                compPinList = []

                for comp in compList:
                    if comp['pin'] != '':
                        compPinList.append(comp['pin'])
                logger.debug ('Ard serial '+ self.ardSerialNumber+ 'pwm pin list: ' + str(compPinList))
                self.serialConnection.sendPinList('pwm', compPinList)

            if componentType == '*' or componentType == 'servo':
                compList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'servo')
                compPinList = []

                for comp in compList:
                    if comp['pin'] != '':
                        compPinList.append(comp['pin'])
                logger.debug ('Ard serial '+ self.ardSerialNumber+ 'servo pin list: ' + str(compPinList))
                self.serialConnection.sendPinList('servo', compPinList)

            if componentType == '*' or componentType == 'dig_output':
                compList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'dig_output')
                compPinList = []

                for comp in compList:
                    if comp['pin'] != '':
                        compPinList.append(comp['pin'])
                logger.debug ('Ard serial '+ self.ardSerialNumber+ 'dig_output pin list: ' + str(compPinList))
                self.serialConnection.sendPinList('dig_output', compPinList)

    def quit(self):
        """Stop the Arduino thread and close the serial connection cleanly.

        Calls :meth:`disconnect` to close the serial port, then sets
        :attr:`running` to ``False`` to exit the :meth:`run` loop.  Should be
        called before the application exits.
        """
        self.disconnect()
        self.running = False
        self.connected = False
        logger.info('Arduino thread stopped, ard serial nr'+self.ardSerialNumber)

    def __isValueInIntervals(self, value, intervalsList):
        """Return whether a value falls inside any of the given intervals.

        Used by :meth:`inputChanged` to determine whether a potentiometer
        value should trigger a command configured with interval-based
        activation.

        Args:
            value (float): The value to test.
            intervalsList (list[list[float, float]]): List of
                ``[lower, upper]`` bounds pairs, e.g.
                ``[[0.0, 200.0], [600.0, 800.0]]``.

        Returns:
            bool: ``True`` if ``value`` is within any interval (inclusive
                bounds); ``False`` otherwise.
        """
        for interval in intervalsList:
            if value >= interval[0] and value <= interval[1]:
                return True

        return False

    def __returnLinearInterpolationY(self, xValue, linearSeriesPoints):
        """Compute a linearly interpolated output value for a given input.

        Given a sorted list of ``[x, y]`` control points, returns the Y value
        corresponding to ``xValue`` using piecewise linear interpolation.
        Values outside the range of the control points are clamped to the Y
        value of the nearest endpoint.

        Used to map raw sensor values (ADC counts, dataref values) to
        hardware output ranges (PWM duty cycles, servo angles).

        Args:
            xValue (float): The input X value to interpolate.
            linearSeriesPoints (list[list[float, float]]): Sorted list of
                ``[x, y]`` control points, e.g.
                ``[[0.0, 0.0], [1023.0, 255.0]]``.

        Returns:
            float: The interpolated Y value, rounded to 5 decimal places.
                Returns ``None`` if ``linearSeriesPoints`` is empty.
        """
        nrPoints = len(linearSeriesPoints)
        if nrPoints>0:
            logger.debug('xValue: '+ str(xValue) +', linearSeriesPoints: '+ str(linearSeriesPoints))
            if xValue < linearSeriesPoints[0][0]:
                return linearSeriesPoints[0][1]


            for i in range(0, nrPoints):
                if i == nrPoints -1: # the xValue is over max point so we return corresponding y of max point
                    return linearSeriesPoints[i][1]

                elif linearSeriesPoints[i][0] <= xValue and linearSeriesPoints[i+1][0] >= xValue:
                    a = float(	float(linearSeriesPoints[i][1]-linearSeriesPoints[i+1][1])
                        /float(linearSeriesPoints[i][0]-linearSeriesPoints[i+1][0]))
                    b = float(	float(linearSeriesPoints[i][0]*linearSeriesPoints[i+1][1] - linearSeriesPoints[i][1]*linearSeriesPoints[i+1][0])
                        /float(linearSeriesPoints[i][0]-linearSeriesPoints[i+1][0]))

                    yValue = xValue*a + b
                    return round(yValue,5)

    def __returnPointsList(self, pointsString):
        """Parse a points string into a sorted list of ``[x, y]`` float pairs.

        Accepts a string in the format ``[x1,y1], [x2,y2], …, [xn,yn]``
        (spaces are optional; negative numbers are supported).  Uses a regex
        to extract individual ``[number,number]`` tokens, then converts each
        to a ``[float, float]`` pair and sorts the result in ascending order
        of the X value.

        This format is used for both interpolation mapping points (output
        components) and interval definitions (potentiometer command activation).

        Args:
            pointsString (str): Raw points string from the XML configuration,
                e.g. ``'[0,0],[512,127],[1023,255]'``.

        Returns:
            list[list[float, float]]: Sorted list of ``[x, y]`` pairs.
                Returns an empty list if no valid pairs are found.
        """
        pointsList = []
        logger.debug('Points list string: '+pointsString)
        pointsStringList = re.findall(r'\[[ -]*?[0-9]+.*?[0-9]*?[,]+[ -]*?[0-9]+.*?[0-9]*?[ ]*?\]',
                                        pointsString)	# find all points format [nr,nr]

        for pointString in pointsStringList:
            pointString = re.sub(r'[\[\] ]+', '', pointString)	#strip spaces, [ and ]

            valueStrings = pointString.split(',')

            if len(valueStrings) == 2:
                pointsList.append([ float(valueStrings[0]), float(valueStrings[1])])

        # let's order the table by ascending x of each pointString
        pointsList.sort(key=itemgetter(0))

        return pointsList
