import serial.tools.list_ports

def listArduinosSerial():
	return list(serial.tools.list_ports.comports())
	#for p in ports:
		#print (p)
	#	print (p.description,  p.serial_number, p.hwid, p.vid, p.pid, p.manufacturer)