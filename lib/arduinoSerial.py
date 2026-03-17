"""
arduinoSerial.py
----------------
Serial communication layer between pyXPArduino and an Arduino board.

:class:`ArduinoSerial` runs as a dedicated background thread.  It opens a
serial port, resets the Arduino via the DTR line, and then enters a
read/write loop:

* **Outbound** — commands queued by :meth:`ArduinoSerial.sendPinList` and
  :meth:`ArduinoSerial.sendOutputValue` are flushed to the serial port once
  the Arduino has signalled it is ready.
* **Inbound** — raw bytes from the Arduino are accumulated into a text buffer,
  split on the ``';'`` delimiter, and dispatched to
  :meth:`ArduinoSerial.__processArduinoCmd`.

Serial protocol summary
~~~~~~~~~~~~~~~~~~~~~~~
All messages are plain ASCII terminated with ``';'``.

Inbound (Arduino → PC):

* ``READY;``                 — board has booted and is ready
* ``VERSION:<ver>;``         — firmware version string
* ``SW:<pin>:<value>;``      — switch state change (value 0 or 1)
* ``POT:<pin>:<value>;``     — potentiometer value change (0–1023)
* ``ROTENC:<pin>:<value>;``  — rotary encoder step (+N or −N)

Outbound (PC → Arduino):

* ``SW_PINS:<p1>:<p2>:…;``       — configure switch pins
* ``POT_PINS:<p1>:…;``           — configure potentiometer pins
* ``PWM_PINS:<p1>:…;``           — configure PWM output pins
* ``ROTENC_PINS:<p1>,<p2>,<s>;`` — configure encoder pins + steps/notch
* ``DIGOUT_PINS:<p1>:…;``        — configure digital output pins
* ``SERVO_PINS:<p1>:…;``         — configure servo pins
* ``PWM:<pin>:<value>;``         — set PWM duty cycle
* ``SERVO:<pin>:<value>;``       — set servo position
* ``DIGOUT:<pin>:<value>;``      — set digital output state

Example usage::

    import ArduinoSerial
    ard = ArduinoSerial.ArduinoSerial("COM3", 115200)
    ard.start()
    # … later …
    ard.quit()
"""

import threading
import sys
import logging
import time
import serial
import os, getpass
from struct import *

logger = logging.getLogger('arduinoSerial')


class ArduinoSerial(threading.Thread):
    """Background thread managing serial I/O with a single Arduino board.

    One instance is created per connected Arduino.  The thread opens the
    serial port in ``__init__``, then :meth:`run` loops continuously reading
    inbound data and flushing outbound command queues.

    Attributes:
        arduinoReady (bool): ``True`` once the Arduino has sent its ``READY``
            message and is accepting commands.
        arduinoFirmwareVersion (str): Firmware version string reported by the
            Arduino, e.g. ``'1.2'``.
        connected (bool): ``True`` if the serial port was opened successfully.
        running (bool): Controls the main loop; set to ``False`` by
            :meth:`quit` to stop the thread.
        queuedCommands (list[str]): Buffer of outbound command strings waiting
            to be written to the serial port.
        PORT (str): The OS port identifier this instance is bound to.
    """

    #: dict[str, str]: Maps component type names to the Arduino pin-list
    #: command prefixes used when configuring hardware pins.
    COMP_PIN_CMDS = {'switch' 			: "SW_PINS:",
                    'potentiometer' 	: "POT_PINS:",
                    'pwm' 				: "PWM_PINS:",
                    'rot_encoder' 		: "ROTENC_PINS:",
                    'dig_output' 		: "DIGOUT_PINS:",
                    'servo'				: "SERVO_PINS:"
                    }

    #: dict[str, str]: Maps output component type names to the Arduino value
    #: command prefixes used when sending output values.
    OUTPUT_TYPE_CMDS = {'pwm' 				: "PWM:",
                        'servo'				: "SERVO:",
                        'dig_output'		: "DIGOUT:"
                        }

    def __init__(self, PORT, BAUD, XPUDPServer=None):
        """Open a serial connection to an Arduino and prepare the I/O thread.

        Performs the following initialisation sequence:

        1. Opens ``PORT`` at ``BAUD`` with 8N1 framing.
        2. Pulses DTR low then high to trigger the Arduino hardware reset /
           bootloader entry sequence.
        3. Flushes any stale bytes from the input buffer.
        4. Waits 500 ms for the Arduino to finish booting.

        If the port cannot be opened a :class:`serial.SerialException` is
        caught, ``connected`` is set to ``False``, and an error is logged —
        the thread can still be *started* but will exit its loop immediately.

        Args:
            PORT (str): OS serial port identifier, e.g. ``'COM3'`` or
                ``'/dev/ttyUSB0'``.
            BAUD (int | str): Baud rate.  Must match the rate compiled into the
                Arduino firmware.
            XPUDPServer (optional): Reference to the pyXPUDPServer instance.
                Only required when the legacy ``CMND``/``DREF`` inbound
                message types are used (not used in normal operation).
        """
        threading.Thread.__init__(self)
        self.arduinoReady = False
        self.arduinoFirmwareVersion = ''
        self.running = True
        self.queuedCommands = []
        self.inputCallbacks = []
        self.ardStateChangedCallbacks = []

        self.connected = False	# are we connected (serial connection successful) to the arduino
        logger.debug("Ardserial running as user: "+getpass.getuser())
        logger.debug("Initialising serial Arduino connection on port: "+ str(PORT)+ ", BAUD: "+ str(BAUD))
        self.serialConnection = None
        self.PORT = PORT

        try:
            self.serialConnection = serial.Serial(PORT, BAUD,
                                                serial.EIGHTBITS, serial.PARITY_NONE, 	#bytesize=EIGHTBITS, parity=PARITY_NONE
                                                serial.STOPBITS_ONE, 						#stopbits=STOPBITS_ONE,
                                                None, False, 				#timeout=None, xonxoff=False,
                                                False, None, 			# rtscts=False, write_timeout=None,
                                                False, )								#dsrdtr=False,
            #reset arduino
            self.serialConnection.setDTR(False) # Drop DTR
            time.sleep(0.022)
            self.serialConnection.setDTR(True)  # UP the DTR back

            self.XPUDPServer = XPUDPServer

            time.sleep(0.01)
            # ensure there is no stale data in the buffer
            self.serialConnection.flushInput()
            self.connected = True

        except serial.SerialException as e:
            errorMsg =  str(e)
            self.connected = False
            logger.error ( "Serial exception, unable to open connection with Arduino: "+errorMsg)

        time.sleep(0.5) # leave time for the arduino to boot up

    def registerInputChangedCallback(self, callbackFunction):
        """Register a callback to be notified when an Arduino input changes state.

        The callback is invoked by :meth:`__processArduinoCmd` whenever a
        ``SW``, ``POT``, or ``ROTENC`` message is received from the Arduino.

        Args:
            callbackFunction (callable): Function with signature
                ``(inputType: str, pin: int, value: int) -> None``
                where *inputType* is ``'SW'``, ``'POT'``, or ``'ROTENC'``.
        """
        self.inputCallbacks.append(callbackFunction)

    def registerArduinoStateChangedCallback(self, callbackFunction):
        """Register a callback to be notified when the Arduino ready-state changes.

        After booting, the Arduino sends a ``READY`` message.  This callback
        is also fired when the firmware version string is received, and again
        on :meth:`quit` so callers can update UI indicators.

        Args:
            callbackFunction (callable): Function with signature
                ``(ready: bool, firmwareVersion: str) -> None``.
        """
        self.ardStateChangedCallbacks.append(callbackFunction)

    def sendOutputValue(self, pin, outputType, value):
        """Queue an output-value command to be sent to the Arduino.

        The command is only queued (not sent immediately); it is flushed to
        the serial port on the next iteration of the :meth:`run` loop, but
        only if the Arduino has already signalled it is ready.

        Args:
            pin (str): Arduino pin number as a string, e.g. ``'9'``.
            outputType (str): One of ``'pwm'``, ``'servo'``, or
                ``'dig_output'``.
            value (int): The value to set on the pin (0–255 for PWM,
                0–180 for servo, 0/1 for digital output).
        """
        if self.arduinoReady == True:
            logger.debug('serial connection, sending output value '+ str(value) + ' for output type ' + outputType)
            command = self.OUTPUT_TYPE_CMDS[outputType]+pin+':'+str(value)+';'
            self.queuedCommands.append(command)
            logger.debug ("Queuing output command: "+ command)

    def sendPinList(self, componentType, pinList):
        """Queue a pin-configuration command to send the active pin list to the Arduino.

        Builds a ``<PREFIX>:<pin1>:<pin2>:…;`` command string and appends it
        to the outbound queue.  Nothing is sent if ``pinList`` is empty.

        For rotary encoders, each entry in ``pinList`` should already be the
        combined string ``'<pinA>,<pinB>,<stepsPerNotch>'``.

        Args:
            componentType (str): Component type key — one of ``'switch'``,
                ``'potentiometer'``, ``'pwm'``, ``'rot_encoder'``,
                ``'dig_output'``, or ``'servo'``.
            pinList (list[str]): Ordered list of pin identifiers to activate
                for this component type.
        """
        if self.serialConnection != None:
            logger.debug('arduinoSerial::sending pin list to arduino' + str(pinList))
            if len(pinList)>0: # only send if there are any pins!
                command = self.COMP_PIN_CMDS[componentType]

                for pin in pinList:
                    command += pin
                    command += ':'
                command = command[:-1]
                command += ';'

                self.queuedCommands.append(command)
                logger.debug ("Queuing command: "+ command)

    def run(self):
        """Main thread loop — reads inbound serial data and flushes outbound commands.

        Do **not** call this method directly.  Use :meth:`threading.Thread.start`
        to launch the thread; Python will call :meth:`run` automatically.

        Loop behaviour:

        * If the Arduino is ready and there are queued commands, each command
          is written to the serial port with a 20 ms inter-command delay to
          allow the Arduino firmware time to process each one.
        * Any available bytes are read from the port, decoded as ``latin-1``,
          and appended to an internal text buffer.
        * Complete messages (delimited by ``';'``) are extracted from the
          buffer and passed to :meth:`__processArduinoCmd`.
        * The loop sleeps 1 ms between iterations to avoid busy-waiting.

        The loop exits when :attr:`running` is set to ``False`` (via
        :meth:`quit`) or the serial connection is ``None``.
        """
        buffer =""
        startTime = time.time()
        lastTime = time.time()

        for callback in self.ardStateChangedCallbacks:
            callback(self.arduinoReady, self.arduinoFirmwareVersion)

        while self.running and self.serialConnection!=None:
            time_running = time.time() - startTime
            current_time = time.time()

            # send commands
            if self.arduinoReady == True :
                if len(self.queuedCommands) >0:
                    logger.debug('command queue: '+str(self.queuedCommands))
                for command in self.queuedCommands:
                    self.serialConnection.write(command.encode())
                    time.sleep(0.02) # leave time for arduino to process to transmit
                self.queuedCommands = []

            data = self.serialConnection.read(self.serialConnection.in_waiting)

            if len(data) > 0:
                logger.debug("Arduino data ("+ str( len(data)) +" chars): "+ str(data) )
                buffer += data.decode(encoding = 'latin_1')

                if ';' in buffer: # we have at least one valid command
                    commands = buffer.split(';')
                    buffer = commands[len(commands)-1] 	# we can now empty the buffer
                    commands.pop() # remove the last element in the list which is an incomplete command
                    for elem in commands:
                        self.__processArduinoCmd(elem)  # we should now have a complete command from arduino to process

                else:
                    commands = []
                logger.debug('commands: ' + str(commands))


            time.sleep(0.001)

    def __processArduinoCmd(self, buffer):
        """Parse and dispatch a single complete command received from the Arduino.

        Called by :meth:`run` for each ``';'``-terminated message.  Recognised
        message types:

        * ``READY``        — marks the Arduino as ready; fires state callbacks.
        * ``VERSION:<v>``  — stores firmware version; fires state callbacks.
        * ``SW:<pin>:<v>`` — switch state; fires input callbacks.
        * ``POT:<pin>:<v>``— potentiometer value; fires input callbacks.
        * ``ROTENC:<pin>:<v>`` — encoder step; fires input callbacks.
        * ``CMND:<cmd>``   — legacy direct X-Plane command passthrough.
        * ``DREF:<dref>``  — legacy direct X-Plane dataref passthrough.

        Unknown or malformed messages are silently ignored (logged at DEBUG).

        Args:
            buffer (str): A single message string with the trailing ``';'``
                already stripped.
        """
        logger.debug ("Process arduino command: "+ buffer)
        if buffer [0:5] == 'READY':
            logger.info("Arduino is ready")
            self.arduinoReady = True
            for callback in self.ardStateChangedCallbacks:
                callback(self.arduinoReady, self.arduinoFirmwareVersion)

        if buffer [0:4] == 'CMND':
            command = buffer[5:len(buffer)-1]
            logger.debug("i see a command"+ command+'\0')

            self.XPUDPServer.sendXPCmd(command+'\0')

        elif buffer [0:4] == 'DREF':
            dataref = buffer[5:len(buffer)-1]

            logger.debug("i see a dataref"+ dataref+'\0')

            self.XPUDPServer.sendXPDref(dataref+'\0')

        else:
            command_elems = buffer.split(":")
            if command_elems[0] == 'VERSION':
                self.arduinoFirmwareVersion = command_elems[1]
                logger.info("Arduino is running firmware version "+self.arduinoFirmwareVersion)
                for callback in self.ardStateChangedCallbacks:
                    callback(self.arduinoReady, self.arduinoFirmwareVersion)

            if (command_elems[0] == 'SW' or command_elems[0] == 'POT' or command_elems[0] == 'ROTENC') and len(command_elems) == 3:
                value = None
                pin = None
                try:
                    pin = int(command_elems[1])
                    value = int(command_elems[2])
                except ValueError:
                    logger.error("Error in reading input command from Arduino")
                    logger.error("Command: " + buffer)
                logger.debug('callbacks:'+ str(self.inputCallbacks))

                if value is not None:
                    for callback in self.inputCallbacks:
                        callback(command_elems[0], pin, value)
                    logger.debug("Input "+command_elems[0]+ " on pin"+ command_elems[1]+ " Value: "+ command_elems[2])

    def quit(self):
        """Stop the serial thread and close the serial port cleanly.

        Sets :attr:`running` to ``False`` to exit the :meth:`run` loop, closes
        the serial port if it is open, resets the firmware version string, and
        fires all registered state-changed callbacks so that UI components can
        update their connection indicators.

        Call this method when the application is shutting down or when
        disconnecting the Arduino.
        """
        self.running = False
        if self.serialConnection!=None:
            self.serialConnection.close()
        self.arduinoReady == False  # NOTE: BUG-01 — should be = not ==
        self.arduinoFirmwareVersion = ''
        for callback in self.ardStateChangedCallbacks:
            callback(self.arduinoReady, self.arduinoFirmwareVersion)
        logger.info("Arduino Connection on port " + self.PORT + " stopped...")
