import logging
import time
import serial

PORT = 'COM3'
BAUD = 115200

try:
	serialConnection = serial.Serial(PORT, BAUD)
	time.sleep(0.01)  
	# ensure there is no stale data in the buffer
	serialConnection.flushInput()  
	serialConnection.flushOutput()
	time.sleep(0.01)

except serial.SerialException as e:
	errorMsg =  str(e)
	logging.error ( "Serial exception, unable to open connection with Arduino: "+errorMsg)

buffer =""

while 1:
	
	bytesToRead = serialConnection.in_waiting
	if (bytesToRead>0):
		data = serialConnection.read(bytesToRead)		
		
		print('Received: '+data.decode(encoding = 'latin_1'))
	
	cmd = input("Enter command or 'exit':")
	# for Python 2
	# cmd = input("Enter command or 'exit':")
		# for Python 3
	if cmd == 'exit':
		serialConnection.close()
		exit()
	else:
		serialConnection.write(cmd.encode('ascii')+'\n\n'.encode())
		time.sleep(0.1)
		
	
	'''
	serialConnection.write("hello dsdsd\n".encode())
	time.sleep(0.1)
	bytesToRead = serialConnection.in_waiting
	if (bytesToRead>0):
		data = serialConnection.read(bytesToRead)		
		print("Arduino data: ", data, "data length", len(data))
		buffer += data.decode(encoding = 'latin_1')
		print("buffer: ", buffer)
	'''