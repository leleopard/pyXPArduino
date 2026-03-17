"""
serialArduinoUtils.py
---------------------
Utility functions for detecting and identifying Arduino boards connected
via USB serial ports.

Uses the ``serial.tools.list_ports`` API to enumerate connected USB devices
and match them by serial number.
"""

import logging
import serial.tools.list_ports


def listArduinosSerial():
    """Return a list of all serial port objects currently available on the system.

    Wraps ``serial.tools.list_ports.comports()`` and returns the raw list of
    ``ListPortInfo`` objects.  Each object exposes attributes such as
    ``device``, ``description``, ``serial_number``, ``hwid``, ``vid``,
    ``pid``, and ``manufacturer``.

    Returns:
        list[ListPortInfo]: All currently detected serial ports.
    """
    return list(serial.tools.list_ports.comports())


def returnArduinoPort(serial_number):
    """Find the OS device port for an Arduino identified by its USB serial number.

    Iterates over all connected serial devices and returns the port string
    (e.g. ``'COM3'`` on Windows or ``'/dev/ttyUSB0'`` on Linux) for the
    device whose serial number matches ``serial_number``.

    Args:
        serial_number (str): The USB serial number of the Arduino board to
            locate (as reported by the OS).

    Returns:
        str | None: The port string if the Arduino is found, or ``None`` if
            no connected device matches the given serial number.
    """
    ard_PORT = None

    USB_device_list = listArduinosSerial()

    for p in USB_device_list:
        if serial_number == str(p.serial_number):
            ard_PORT = str(p.device)

    if ard_PORT == None:
        logging.warning('Arduino serial nr '+serial_number+' not connected')
    else:
        logging.debug('Arduino serial nr '+serial_number+' connected on PORT '+ ard_PORT)

    return ard_PORT
