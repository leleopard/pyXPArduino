import logging
import serial.tools.list_ports

def listArduinosSerial():
	return list(serial.tools.list_ports.comports())
	#for p in ports:
		#print (p)
	#	print (p.description,  p.serial_number, p.hwid, p.vid, p.pid, p.manufacturer)

## returns the port as a string for the arduino with serial number provided in argument, if not found returns None
#
def returnArduinoPort(serial_number):
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
