"""
arduinoXMLconfig.py
-------------------
XML-based configuration manager for Arduino boards and their components.

:class:`arduinoConfig` is the single source of truth for the hardware
configuration at runtime.  It parses an XML file on disk into an
ElementTree, exposes CRUD operations for Arduino boards and individual
input/output components, and notifies registered observers via callbacks
whenever attributes change.

XML structure overview::

    <arduinoConfig>
        <arduino name="…" serial_nr="…" port="…" baud="…" …>
            <inputs description="Inputs">
                <switches description="Switches">
                    <switch id="…" name="…" pin="…" state="on">
                        <action state="on" action_type="cmd" …>sim/cmd/foo</action>
                    </switch>
                </switches>
                <potentiometers …> … </potentiometers>
                <rot_encoders …> … </rot_encoders>
            </inputs>
            <outputs description="Outputs">
                <dig_outputs …> … </dig_outputs>
                <pwms …> … </pwms>
                <servos …> … </servos>
            </outputs>
        </arduino>
    </arduinoConfig>

Module-level constants
~~~~~~~~~~~~~~~~~~~~~~
* :data:`ARD_BAUD` — supported baud rates.
* :data:`DIG_IO_PINS` — available digital I/O pin numbers for the Mega 2560.
* :data:`POT_PINS` — analog input pin numbers (A0–A15).
* :data:`PWM_PINS` — PWM-capable pin numbers.
* :data:`SERVO_PINS` — servo-capable pin numbers.
* :data:`INPUT_OUTPUT_TAGS` — XML tag names for input/output category containers.
* :data:`INPUT_OUTPUT_ELEMS_TAGS` — XML tag names for individual component elements.
* :data:`INPUT_OUTPUT_TAGS_REF` — metadata dict mapping container tags to UI labels
  and child element tag names.
"""

#!/usr/bin/env python

import xml.etree.ElementTree as ET
import logging
logger = logging.getLogger('arduinoXMLconfig')

#: list[str]: Supported Arduino serial baud rates, in ascending order.
ARD_BAUD = ['9600', '19200', '38400', '57600', '74880', '115200', '230400', '250000']

#: list[str]: XML container tag names for input/output category nodes.
INPUT_OUTPUT_TAGS = ["switches", "potentiometers", "rot_encoders", "dig_outputs", "pwms", "servos"]

#: list[str]: XML element tag names for individual component nodes.
INPUT_OUTPUT_ELEMS_TAGS = ["switch", "potentiometer", "rot_encoder", "dig_output", "pwm", "servo"]

#: dict[str, dict]: Metadata for each input/output container tag.
#: Each entry maps a container tag name to a dict with keys:
#:   ``'add_action'`` — the UI menu label for adding a component, and
#:   ``'child_tag'``  — the XML tag used for individual component elements.
INPUT_OUTPUT_TAGS_REF = {"switches":        {'add_action':'Add switch','child_tag':'switch'},
                        "potentiometers":    {'add_action':'Add potentiometer','child_tag':'potentiometer'},
                        "rot_encoders":        {'add_action':'Add rotary encoder','child_tag':'rot_encoder'},
                        "dig_outputs":        {'add_action':'Add digital output','child_tag':'dig_output'},
                        "pwms":                {'add_action':'Add PWM','child_tag':'pwm'},
                        "servos":            {'add_action':'Add servo','child_tag':'servo'}}

#: list[str]: Available digital I/O pin numbers for the Arduino Mega 2560.
#: Pins 2, 3, 5 are excluded (reserved for Timer 3 / PWM).
#: Pins 0–13 are excluded (reserved for serial comms, PWM, and servos).
DIG_IO_PINS = ['', '14','15', '16', '17', '18', '19', '20', '21', #COMMS PINS AS DIO
                '22','23','24','25','26','27','28','29','30','31','32','33','34','35',
                '36','37','38','39','40','41','42','43','44','45','46','47',
                '48','49','50','51','52','53']

#: list[str]: Analog input pin numbers (A0–A15) represented as ``'0'``–``'15'``.
POT_PINS = ['', '0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

#: list[str]: PWM-capable digital pin numbers on the Mega 2560.
#: Pins 2, 3, 5 are removed (Timer 3 — reserved).
PWM_PINS = ['','4','6','7','8','9','10']

#: list[str]: Servo-capable pin numbers.
SERVO_PINS = ['','11', '12', '13']


class arduinoConfig():
    """Manages the Arduino hardware configuration stored in an XML file.

    Provides load, save, and CRUD operations for Arduino boards and their
    input/output components.  Registered observer callbacks are fired
    whenever attributes change so that the UI and Arduino threads can react
    without polling.

    Attributes:
        componentAttributeChangedCallbacks (list[callable]): Functions called
            when a component attribute is updated.  Signature:
            ``(componentType, compSerialNr, ardSerialNr, attribute) -> None``.
        arduinoAttributeChangedCallbacks (list[callable]): Functions called
            when an Arduino-level attribute is updated.  Signature:
            ``(ardSerialNr, attribute) -> None``.
        fileLoadedStatusCallbacks (list[callable]): Functions called when the
            config file load status changes.  Signature:
            ``(loaded: bool) -> None``.
        configFileLoaded (bool): ``True`` if a valid config file is currently
            loaded into memory.
        root (xml.etree.ElementTree.Element): Root element of the parsed XML
            tree.  Available only after a successful :meth:`loadConfigFile`.
        tree (xml.etree.ElementTree.ElementTree): The full parsed XML tree.
        ardXMLconfigFile (str): Path of the currently loaded config file.
    """

    def __init__(self):
        """Initialise the config manager with empty callback lists and no loaded file."""
        self.componentAttributeChangedCallbacks = []
        self.arduinoAttributeChangedCallbacks = []
        self.fileLoadedStatusCallbacks = []
        self.configFileLoaded = False

    def loadConfigFile(self, ardXMLconfigFile):
        """Parse an XML configuration file and load it into memory.

        On success, :attr:`configFileLoaded` is set to ``True`` and the
        ElementTree is available via :attr:`tree` and :attr:`root`.  On
        failure (file not found, malformed XML, or ``None`` path) the flag is
        set to ``False`` and an error is logged.

        All registered :attr:`fileLoadedStatusCallbacks` are called with the
        resulting status regardless of success or failure.

        Args:
            ardXMLconfigFile (str | None): Absolute or relative path to the
                Arduino XML configuration file.  Pass ``None`` to trigger the
                "no file specified" error path.
        """
        if ardXMLconfigFile is not None:
            try:
                self.tree = ET.parse(ardXMLconfigFile)
                self.root = self.tree.getroot()
                self.ardXMLconfigFile = ardXMLconfigFile
                self.configFileLoaded = True

            except:
                logger.error('Error while loading arduino config file', exc_info=True)
                self.configFileLoaded = False
        else:
            logger.error('No arduino config file specified, please create a new one or open an existing one')

        for callback in self.fileLoadedStatusCallbacks:
            callback(self.configFileLoaded)

    def registerFileLoadedStatusCallback(self, callback):
        """Register a callback to be notified when the config file load status changes.

        Args:
            callback (callable): Function with signature ``(loaded: bool) -> None``.
        """
        self.fileLoadedStatusCallbacks.append(callback)

    def createConfigFile(self, ardXMLconfigFile):
        """Create a new, empty Arduino XML configuration file on disk.

        Writes the minimal valid XML skeleton ``<arduinoConfig></arduinoConfig>``
        to the specified path, overwriting any existing file.  The file is
        **not** automatically loaded — call :meth:`loadConfigFile` afterwards.

        Args:
            ardXMLconfigFile (str): Destination file path.
        """
        config_file = open(ardXMLconfigFile, "w")
        config_file.write("<arduinoConfig></arduinoConfig>")
        config_file.close()

    def addInputOutput(self, arduinoSerialNr, inputOutputType):
        """Add a new input/output component of the given type to an Arduino.

        Appends a new child element under the appropriate container tag (e.g.
        ``<switches>``), assigning it a unique ID in the format
        ``<containerTag>_<serialNr>-<index>`` and a default name.

        The new component is given an empty ``pin`` attribute and ``state``
        set to ``'on'``.  The configuration is **not** automatically saved to
        disk — call :meth:`saveToXMLfile` when ready.

        Args:
            arduinoSerialNr (str): Serial number of the target Arduino.
            inputOutputType (str): Container tag name, e.g. ``'switches'``,
                ``'potentiometers'``, ``'pwms'``, etc.
        """
        if self.configFileLoaded == True:
            logger.debug("Add InOutput type "+str(inputOutputType)+ " to Arduino serial nr: "+str(arduinoSerialNr))
            ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
            inputOutputTag = ardTag.findall(".//"+inputOutputType)[0]
            # find all existing items under this tag
            items = list(inputOutputTag.iter(INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag']))
            highest_index = 0
            for item in items:
                item_id = str(item.attrib['id'])
                tokens = item_id.split("-")
                index = int(tokens[1])
                if index>= highest_index:
                    highest_index = index +1


            inputoutput = ET.SubElement(inputOutputTag,INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag'])
            inputoutput.set('id', inputOutputTag.tag+"_"+arduinoSerialNr+"-"+str(highest_index))
            inputoutput.set('name', INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag']+" "+str(highest_index))
            inputoutput.set('pin', '')
            inputoutput.set('state', 'on')

    def addArduino(self, port, name, description, serial_number, manufacturer):
        """Add a new Arduino board entry to the configuration.

        Creates an ``<arduino>`` element with all required attributes and the
        full input/output sub-tree (inputs → switches, potentiometers,
        rot_encoders; outputs → dig_outputs, pwms, servos).  The default baud
        rate is set to ``'57600'``.

        The configuration is **not** automatically saved to disk.

        Args:
            port (str): Serial port the Arduino is connected to, e.g.
                ``'COM3'`` or ``'/dev/ttyUSB0'``.
            name (str): Human-readable display name.
            description (str): Board description (e.g. ``'Arduino Mega 2560'``).
            serial_number (str): USB serial number used as the unique
                identifier throughout the application.
            manufacturer (str): Manufacturer string reported by the OS.
        """
        if self.configFileLoaded == True:
            logger.info('Adding Arduino: port: %s, name: %s, description: %s, serial nr: %s, manufacturer: %s', port, name, description, serial_number, manufacturer)
            ardTag = ET.SubElement(self.root, 'arduino')
            ardTag.set('port', port)
            ardTag.set('name', name)
            ardTag.set('description', description)
            ardTag.set('serial_nr', serial_number)
            ardTag.set('manufacturer', manufacturer)
            ardTag.set('baud', '57600')
            ardTag.set('connected', '')

            inputTag = ET.SubElement(ardTag, 'inputs')
            inputTag.set('description', 'Inputs')

            outputTag = ET.SubElement(ardTag, 'outputs')
            outputTag.set('description', 'Outputs')

            switchesTag = ET.SubElement(inputTag, 'switches')
            switchesTag.set('description', 'Switches')
            potentiometersTag = ET.SubElement(inputTag, 'potentiometers')
            potentiometersTag.set('description', 'Potentiometers')
            rot_encodersTag = ET.SubElement(inputTag, 'rot_encoders')
            rot_encodersTag.set('description', 'Rotary Encoders')

            digOutputsTag = ET.SubElement(outputTag, 'dig_outputs')
            digOutputsTag.set('description', 'Digital Outputs')
            pwmsTag = ET.SubElement(outputTag, 'pwms')
            pwmsTag.set('description', 'PWMs')
            servosTag = ET.SubElement(outputTag, 'servos')
            servosTag.set('description', 'Servos')
        else:
            logger.warning("No config file loaded, please create config file first")

    def removeArduino(self, arduinoSerialNr):
        """Remove an Arduino and all its components from the configuration.

        Locates the ``<arduino>`` element by serial number and removes it from
        the XML tree.  The configuration is **not** automatically saved to disk.

        Args:
            arduinoSerialNr (str): Serial number of the Arduino to remove.
        """
        if self.configFileLoaded == True:
            ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
            self.root.remove(ardTag)
        else:
            logger.warning("No config file loaded, please create config file first")

    def getArduinoList(self):
        """Return a list of all Arduino boards defined in the configuration.

        Returns:
            list[dict]: One dict per Arduino with keys ``'port'``, ``'baud'``,
                ``'name'``, ``'description'``, ``'serial_nr'``, and
                ``'manufacturer'``.  Returns an empty list if no config file
                is loaded or no ``<arduino>`` elements are found.
        """
        ardList = []
        if self.configFileLoaded == True:
            ardTags = self.root.findall(".//arduino")

            if len(ardTags) > 0: # arduino has been found
                for ardTag in ardTags:
                    ardDict = {'port': ardTag.attrib['port'],
                            'baud': ardTag.attrib['baud'],
                            'name': ardTag.attrib['name'],
                            'description': ardTag.attrib['description'],
                            'serial_nr': ardTag.attrib['serial_nr'],
                            'manufacturer': ardTag.attrib['manufacturer']}
                    ardList.append(ardDict)
            return ardList
        else:
            logger.warning("No config file loaded, please create config file first")
            return ardList

    def removeInputOutput(self, arduinoSerialNr, inputOutputID):
        """Remove a single input/output component from an Arduino.

        Finds the component by its unique ID attribute and removes it from its
        parent container element.  The configuration is **not** saved automatically.

        Args:
            arduinoSerialNr (str): Serial number of the owning Arduino.
            inputOutputID (str): Unique component ID (``id`` XML attribute),
                e.g. ``'switches_A1B2C3-0'``.
        """
        if self.configFileLoaded == True:
            logger.debug("Remove InOutput ID ",inputOutputID, "from Arduino serial nr:", arduinoSerialNr)
            ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
            inputOutputTag = ardTag.findall(".//*[@id='"+inputOutputID+"']")[0]
            logger.debug("ID to remove found: ", inputOutputTag.attrib['id'])
            parent = ardTag.findall(".//*[@id='"+inputOutputID+"']/..")[0]
            parent.remove(inputOutputTag)
        else:
            logger.warning("No config file loaded, please create config file first")

    def saveToXMLfile(self):
        """Persist the current in-memory configuration tree to the XML file on disk.

        Writes to the path stored in :attr:`ardXMLconfigFile` (set during the
        last successful :meth:`loadConfigFile` call).
        """
        if self.configFileLoaded == True:
            self.tree.write(self.ardXMLconfigFile)
        else:
            logger.warning("No config file loaded, please create config file first")

    def getComponentActions(self, arduinoSerialNr, componentType, pin):
        """Return the list of actions configured for a component identified by pin.

        Searches for a component of ``componentType`` on the given ``pin``
        belonging to ``arduinoSerialNr``, and returns all of its child
        ``<action>`` elements as dicts.

        Args:
            arduinoSerialNr (str): Serial number of the Arduino board.
            componentType (str): Component type tag, e.g. ``'switch'``,
                ``'potentiometer'``, ``'rot_encoder'``.
            pin (str | int): Pin number to look up.

        Returns:
            list[dict]: One dict per action with keys:

            * ``'state'`` (str) — trigger state, e.g. ``'on'``, ``'off'``,
              ``'up'``, ``'down'``.
            * ``'action_type'`` (str) — ``'cmd'`` or ``'dref'``.
            * ``'cmddref'`` (str) — X-Plane command or dataref string.
            * ``'index'`` (str) — array index for dataref actions (default ``'0'``).
            * ``'setToValue'`` (str) — value to write to the dataref or
              interpolation point string (default ``'0.0'``).
            * ``'continuous'`` (str) — ``'True'`` or ``'False'``.

            Returns an empty list if the Arduino or component is not found.
        """
        actionsList = []
        if self.configFileLoaded == True:
            ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
            if len(ardTags) > 0: # arduino has been found
                compTag = ardTags[0].findall(".//"+componentType+"[@pin='"+str(pin)+"']")
                if len(compTag) > 0: # component has been found
                    actions = list(compTag[0].iter('action'))

                    for action in actions:
                        index = '0'
                        setToValue = '0.0'
                        continuous = 'False'
                        cmddref = ''
                        if action.text != None:
                            cmddref = action.text

                        try:
                            index = action.attrib['index']
                            setToValue = action.attrib['setToValue']
                            continuous = action.attrib['continuous']
                        except:
                            pass
                        actionsList.append({'state': action.attrib['state'],
                                            'action_type': action.attrib['action_type'],
                                            'cmddref': cmddref,
                                            'index': index,
                                            'setToValue': setToValue,
                                            'continuous': continuous})
        else:
            logger.warning("No config file loaded, please create config file first")

        return actionsList

    def getComponentAttribute(self, arduinoSerialNr, componentType, pin, attribute):
        """Return a single attribute value for a component identified by pin.

        Args:
            arduinoSerialNr (str): Serial number of the Arduino.
            componentType (str): Component type tag, e.g. ``'switch'``.
            pin (str | int): Pin number of the component.
            attribute (str): Name of the XML attribute to retrieve.

        Returns:
            str: The attribute value, or ``''`` if the Arduino or component
                is not found, or if the attribute does not exist.
        """
        if self.configFileLoaded == True:
            ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
            if len(ardTags) > 0: # arduino has been found
                compTag = ardTags[0].findall(".//"+componentType+"[@pin='"+str(pin)+"']")
                if len(compTag) > 0: # component has been found
                    return compTag[0].attrib[attribute]
            return ''
        else:
            logger.warning("No config file loaded, please create config file first")

        return ''

    def getComponentList(self, arduinoSerialNr, componentType):
        """Return all components of a given type belonging to an Arduino.

        Args:
            arduinoSerialNr (str): Serial number of the Arduino.
            componentType (str): Component type tag, e.g. ``'switch'``,
                ``'potentiometer'``, ``'pwm'``, ``'servo'``,
                ``'dig_output'``, ``'rot_encoder'``.

        Returns:
            list[dict]: One dict per component with keys:

            * ``'name'`` (str) — display name.
            * ``'id'`` (str) — unique component ID.
            * ``'pin'`` (str) — primary pin number, or ``''`` if unset.
            * ``'pin2'`` (str) — secondary pin (rotary encoders), or ``''``.
            * ``'stepsPerNotch'`` (str) — encoder steps per detent, or ``''``.
            * ``'state'`` (str) — last known state.

            Returns an empty list if the Arduino is not found or the config is
            not loaded.
        """
        compList = []
        if self.configFileLoaded == True:
            ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
            if len(ardTags) > 0: # arduino has been found
                compTags = ardTags[0].findall(".//"+componentType)
                for compTag in compTags:
                    pin =''
                    if 'pin' in compTag.attrib:
                        pin = compTag.attrib['pin']
                    pin2 =''
                    if 'pin2' in compTag.attrib:
                        pin2 = compTag.attrib['pin2']
                    stepsPerNotch = ''
                    if 'stepsPerNotch' in compTag.attrib:
                        stepsPerNotch = compTag.attrib['stepsPerNotch']

                    compList.append({'name': compTag.attrib['name'],
                                    'id': compTag.attrib['id'],
                                    'pin': pin,
                                    'pin2': pin2,
                                    'stepsPerNotch': stepsPerNotch,
                                    'state': compTag.attrib['state']})
        else:
            logger.warning("No config file loaded, please create config file first")

        return compList

    def getComponentData(self, compSerialNr, componentType):
        """Return the full data dict for a component identified by its unique ID.

        Unlike :meth:`getComponentList` (which searches by Arduino serial
        number), this method searches the entire tree by component ID and
        returns all attributes plus the full actions list.

        Args:
            compSerialNr (str): Unique component ID (``id`` XML attribute).
            componentType (str): Component type tag, e.g. ``'switch'``,
                ``'rot_encoder'``.

        Returns:
            dict | None: A dict with keys ``'name'``, ``'id'``, ``'pin'``,
                ``'pin2'``, ``'stepsPerNotch'``, ``'state'``,
                ``'acceleration'``, ``'multiplier'``, and ``'actions'``
                (list of action dicts as described in :meth:`getComponentActions`).
                Returns ``None`` if the component is not found or no config
                file is loaded.
        """
        if self.configFileLoaded == True:
            compTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']")
            if len(    compTag) > 0: # comp has been found
                pin =''
                pin2 = ''
                stepsPerNotch = '4'
                acceleration = 'False'
                multiplier = '1.0'
                if 'pin' in compTag[0].attrib:
                    pin = compTag[0].attrib['pin']
                if 'pin2' in compTag[0].attrib:
                    pin2 = compTag[0].attrib['pin2']
                if 'stepsPerNotch' in compTag[0].attrib:
                    stepsPerNotch = compTag[0].attrib['stepsPerNotch']
                if 'acceleration' in compTag[0].attrib:
                    acceleration = compTag[0].attrib['acceleration']
                if 'multiplier' in compTag[0].attrib:
                    multiplier = compTag[0].attrib['multiplier']


                actions = list(compTag[0].iter('action'))
                actionsList = []
                for action in actions:
                    index = '0'
                    setToValue = '0.0'
                    continuous = 'False'
                    try:
                        index = action.attrib['index']
                        setToValue = action.attrib['setToValue']
                        continuous = action.attrib['continuous']
                    except:
                        pass

                    actionsList.append({'state': action.attrib['state'],
                                        'action_type': action.attrib['action_type'],
                                        'cmddref': action.text,
                                        'index': index,
                                        'setToValue': setToValue,
                                        'continuous': continuous})
                compDict = {'name': compTag[0].attrib['name'],
                        'id': compTag[0].attrib['id'],
                        'pin': pin,
                        'pin2': pin2,
                        'stepsPerNotch': stepsPerNotch,
                        'state': compTag[0].attrib['state'],
                        'acceleration': acceleration,
                        'multiplier': multiplier,
                        'actions': actionsList}

                return compDict
            else:
                return None
        else:
            logger.warning("No config file loaded, please create config file first")
            return None

    def registerComponentAttributeChangedCallback(self, callback):
        """Register a callback to be notified when any component attribute changes.

        Args:
            callback (callable): Function with signature
                ``(componentType: str, compSerialNr: str, ardSerialNr: str,
                attribute: str) -> None``.
        """
        self.componentAttributeChangedCallbacks.append(callback)

    def registerArduinoAttributeChangedCallback(self, callback):
        """Register a callback to be notified when any Arduino-level attribute changes.

        Args:
            callback (callable): Function with signature
                ``(ardSerialNr: str, attribute: str) -> None``.
        """
        self.arduinoAttributeChangedCallbacks.append(callback)

    def updateComponentActions(self, arduinoSerialNr, componentType, pin, actionsList):
        """Replace all actions for a component with the provided list.

        Removes all existing ``<action>`` child elements from the component and
        replaces them with new elements built from ``actionsList``.  Typically
        called by :class:`~lib.Arduino.Arduino` after reading updated dataref
        values so the ``state`` field stays current.

        Args:
            arduinoSerialNr (str): Serial number of the Arduino.
            componentType (str): Component type tag, e.g. ``'pwm'``.
            pin (str | int): Pin number identifying the component.
            actionsList (list[dict]): New list of action dicts.  Each dict
                must contain at minimum ``'state'``, ``'action_type'``, and
                ``'cmddref'``.  Optional keys are ``'index'`` and
                ``'setToValue'``.
        """
        ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
        if len(ardTags) > 0: # arduino has been found
            compTag = ardTags[0].findall(".//"+componentType+"[@pin='"+str(pin)+"']")
            if len(compTag) > 0: # switch has been found

                for action in list(compTag[0]): # first remove all actions
                    compTag[0].remove(action)

                for action in actionsList:
                    actionTag = ET.SubElement(compTag[0], 'action')
                    actionTag.set('state', action['state'])
                    actionTag.set('action_type', action['action_type'])
                    try:
                        actionTag.set('index', action['index'])
                        actionTag.set('setToValue', action['setToValue'])
                    except:
                        pass
                    actionTag.text = action['cmddref']

    def updateComponentData(self, compSerialNr, componentType, compData, actions=[]):
        """Update a component's attributes and replace its actions in the XML tree.

        Updates the ``id``, ``name``, ``pin``, and optionally ``pin2``,
        ``stepsPerNotch``, ``acceleration``, and ``multiplier`` attributes,
        then replaces all ``<action>`` children with those from ``actions``.

        .. note::
            BUG-02 — the XPath expression used to locate the parent Arduino
            element on line 371 contains extra dots and will always return an
            empty list, causing an ``IndexError`` when the ardSerialNr lookup
            is attempted.

        Args:
            compSerialNr (str): Current unique ID of the component to update.
            componentType (str): Component type tag, e.g. ``'switch'``,
                ``'rot_encoder'``.
            compData (dict): Dict of updated attributes.  Required keys:
                ``'id'``, ``'name'``, ``'pin'``.  Optional keys: ``'pin2'``,
                ``'stepsPerNotch'``, ``'acceleration'``, ``'multiplier'``.
            actions (list[dict], optional): Replacement action list.  Each
                dict must contain ``'state'``, ``'action_type'``, ``'cmddref'``,
                and optionally ``'continuous'``, ``'index'``, ``'setToValue'``.
                Defaults to an empty list (removes all existing actions).

        Returns:
            int: Returns ``-1`` if the component is not found or no config
                file is loaded; otherwise implicitly returns ``None``.
        """
        if self.configFileLoaded == True:
            logger.debug('Update Component Data, type: '+componentType)
            compTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']")
            if len(compTag) > 0: # component has been found
                #find the switch arduino parent element
                ardTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']......")
                ardSerialNr = ardTag[0].attrib['serial_nr']

                self.updateComponentAttribute(compSerialNr, componentType,'id', compData['id'])
                self.updateComponentAttribute(compSerialNr, componentType,'name', compData['name'])
                self.updateComponentAttribute(compSerialNr, componentType,'pin', compData['pin'])
                if 'pin2' in compData: # test if 2nd pin provided
                    self.updateComponentAttribute(compSerialNr, componentType,'pin2', compData['pin2'])
                if 'stepsPerNotch' in compData: # test if stepsPerNotch provided
                    self.updateComponentAttribute(compSerialNr, componentType,'stepsPerNotch', compData['stepsPerNotch'])
                if 'acceleration' in compData: # test if acceleration provided
                    self.updateComponentAttribute(compSerialNr, componentType,'acceleration', compData['acceleration'])
                if 'multiplier' in compData: # test if multiplier provided
                    self.updateComponentAttribute(compSerialNr, componentType,'multiplier', compData['multiplier'])

                for action in list(compTag[0]): # first remove all actions
                    compTag[0].remove(action)

                for action in actions:
                    actionTag = ET.SubElement(compTag[0], 'action')
                    actionTag.set('state', action['state'])
                    actionTag.set('action_type', action['action_type'])
                    try:
                        actionTag.set('continuous', action['continuous'])
                    except:
                        actionTag.set('continuous', '')
                    try:
                        actionTag.set('index', action['index'])
                    except:
                        actionTag.set('index', '')
                    try:
                        actionTag.set('setToValue', action['setToValue'])
                    except:
                        actionTag.set('setToValue', '')
                    actionTag.text = action['cmddref']

            else:
                return -1
        else:
            logger.warning("No config file loaded, please create config file first")
            return -1

    def updateComponentAttribute(self, compSerialNr, componentType, attribute, attributeValue):
        """Update a single attribute of a component and notify observers.

        If the attribute does not already exist on the element it is created
        (backward-compatibility for new attributes added in later versions).
        Observers are only notified if the value actually changes.

        .. note::
            BUG-02 — the XPath expression used to locate the parent Arduino
            element contains extra dots and will always fail with an
            ``IndexError``.  The ``ardSerialNr`` lookup on the following line
            is therefore unreachable in the current code.

        Args:
            compSerialNr (str): Unique component ID.
            componentType (str): Component type tag, e.g. ``'switch'``.
            attribute (str): Name of the XML attribute to update.
            attributeValue (str): New value for the attribute.

        Returns:
            int: Returns ``-1`` if the component is not found or no config
                file is loaded; otherwise implicitly returns ``None``.
        """
        if self.configFileLoaded == True:
            logger.debug('Update component attribute: '+compSerialNr+' attribute: ' +attribute+' value:'+attributeValue )
            compTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']")
            if len(compTag) > 0: # component has been found
                #find the component arduino parent element
                ardTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']......")
                ardSerialNr = ardTag[0].attrib['serial_nr']
                if attribute not in compTag[0].attrib: # this attribute does not exist so lets create it
                    compTag[0].set(attribute, '')
                if compTag[0].attrib[attribute] != attributeValue: # then the value has changed and must be updated
                    compTag[0].set(attribute, attributeValue)
                    # and we notify all callbacks of this attribute change
                    for callback in self.componentAttributeChangedCallbacks:
                        callback(componentType, compSerialNr,ardSerialNr, attribute)
            else:
                return -1
        else:
            logger.warning("No config file loaded, please create config file first")
            return -1

    def getArduinoData(self, arduinoSerialNr):
        """Return a full attribute dict for an Arduino board.

        Dynamically creates any missing runtime attributes (``'connected'``,
        ``'firmware_version'``, ``'ard_status'``) in the element if they are
        absent — this ensures backward compatibility with config files saved
        by older versions of the application.

        Args:
            arduinoSerialNr (str): Serial number of the Arduino to retrieve.

        Returns:
            dict | None: Dict with keys ``'port'``, ``'baud'``, ``'name'``,
                ``'description'``, ``'serial_nr'``, ``'manufacturer'``,
                ``'connected'``, ``'firmware_version'``, and ``'ard_status'``.
                Returns ``None`` if the Arduino is not found or no config file
                is loaded.
        """
        if self.configFileLoaded == True:
            ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
            if len(ardTags) > 0: # arduino has been found
                if 'connected' not in ardTags[0].attrib: # this attribute does not exist so lets create it
                    ardTags[0].set('connected', '')
                if 'firmware_version' not in ardTags[0].attrib: # this attribute does not exist so lets create it
                    ardTags[0].set('firmware_version', '')
                if 'ard_status' not in ardTags[0].attrib: # this attribute does not exist so lets create it
                    ardTags[0].set('ard_status', '')

                ardDict = {'port': ardTags[0].attrib['port'],
                        'baud': ardTags[0].attrib['baud'],
                        'name': ardTags[0].attrib['name'],
                        'description': ardTags[0].attrib['description'],
                        'serial_nr': ardTags[0].attrib['serial_nr'],
                        'manufacturer': ardTags[0].attrib['manufacturer'],
                        'connected': ardTags[0].attrib['connected'],
                        'firmware_version': ardTags[0].attrib['firmware_version'],
                        'ard_status': ardTags[0].attrib['ard_status']}

                return ardDict
            else:
                return None
        else:
            logger.warning("No config file loaded, please create config file first")
            return None

    def updateArduinoData(self, arduinoSerialNr, ardData):
        """Update the editable attributes of an Arduino and notify observers.

        Compares each attribute in ``ardData`` against the current XML value
        and only writes (and fires callbacks for) attributes that have actually
        changed.  Handles: ``'port'``, ``'baud'``, ``'name'``,
        ``'description'``, ``'serial_nr'``, ``'manufacturer'``.

        Args:
            arduinoSerialNr (str): Serial number of the Arduino to update.
            ardData (dict): Dict of new values.  Must contain the keys listed
                above.

        Returns:
            int: Returns ``-1`` if the Arduino is not found or no config file
                is loaded; otherwise implicitly returns ``None``.
        """
        if self.configFileLoaded == True:
            logger.debug("updating arduino data for arduino serial nr %s, data: %s",arduinoSerialNr, ardData)
            ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
            if len(ardTags) > 0: # arduino has been found
                if ardTags[0].attrib['port'] != ardData['port']:
                    ardTags[0].set('port', ardData['port'])
                    for callback in self.arduinoAttributeChangedCallbacks:
                        callback(arduinoSerialNr, 'port')

                if ardTags[0].attrib['baud'] != ardData['baud']:
                    ardTags[0].set('baud', ardData['baud'])
                    for callback in self.arduinoAttributeChangedCallbacks:
                        callback(arduinoSerialNr, 'baud')

                if ardTags[0].attrib['name'] != ardData['name']:
                    ardTags[0].set('name', ardData['name'])
                    for callback in self.arduinoAttributeChangedCallbacks:
                        callback(arduinoSerialNr, 'name')

                if ardTags[0].attrib['description'] != ardData['description']:
                    ardTags[0].set('description', ardData['description'])
                    for callback in self.arduinoAttributeChangedCallbacks:
                        callback(arduinoSerialNr, 'description')

                if ardTags[0].attrib['serial_nr'] != ardData['serial_nr']:
                    ardTags[0].set('serial_nr', ardData['serial_nr'])
                    for callback in self.arduinoAttributeChangedCallbacks:
                        callback(arduinoSerialNr, 'serial_nr')

                if ardTags[0].attrib['manufacturer'] != ardData['manufacturer']:
                    ardTags[0].set('manufacturer', ardData['manufacturer'])
                    for callback in self.arduinoAttributeChangedCallbacks:
                        callback(arduinoSerialNr, 'manufacturer')
            else :
                return -1
        else:
            logger.warning("No config file loaded, please create config file first")
            return -1

    def updateArduinoAttribute(self, arduinoSerialNr, attribute, attributeValue):
        """Set a single attribute on an Arduino element and notify observers.

        Unlike :meth:`updateArduinoData`, this method unconditionally sets the
        value without comparing to the previous one, making it suitable for
        runtime-only attributes such as ``'connected'``, ``'ard_status'``,
        and ``'firmware_version'`` that are not user-editable.

        If the attribute does not yet exist on the element it is created
        (backward compatibility).

        Args:
            arduinoSerialNr (str): Serial number of the Arduino to update.
            attribute (str): XML attribute name to set.
            attributeValue (str): New value.

        Returns:
            int: Returns ``-1`` if the Arduino is not found or no config file
                is loaded; otherwise implicitly returns ``None``.
        """
        if self.configFileLoaded == True:
            ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
            if len(ardTags) > 0: # arduino has been found
                ardTags[0].set(attribute, attributeValue)
                for callback in self.arduinoAttributeChangedCallbacks:
                    callback(arduinoSerialNr, attribute)
            else :
                return -1
        else:
            logger.warning("No config file loaded, please create config file first")
            return -1
