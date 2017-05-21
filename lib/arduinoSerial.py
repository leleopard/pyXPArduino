import threading
import sys
import logging
import time
import serial
from struct import *

##--------------------------------------------------------------------------------------------------------------------
# class ArduinoSerial
#
# Allows to send and receive data to an arduino over the serial port 
#
# The class is inherited from the Threading module, and will run as its own thread when started
# Simple Example:
#
# @code 
# import ArduinoSerial
# ArduinoSerial = ArduinoSerial.ArduinoSerial(("COM3",115200)
# ArduinoSerial.start()
# @endcode
#
# you should call the quit() method when exiting your main python programme
#
#--------------------------------------------------------------------------------------------------------------------

class ArduinoSerial(threading.Thread):
	
	COMP_PIN_CMDS = {'switch' : "SW_PINS:",
	'potentiometer' : "POT_PINS:" 
	}
	
	##--------------------------------------------------------------------------------------------------------------------
	# constructor 
	# @param PORT: port the arduino is connected to
	# @param BAUD: BAUD setting for the serial port - needs to be the same as how the arduino is configured
	#
	#--------------------------------------------------------------------------------------------------------------------
	def __init__(self, PORT, BAUD, XPUDPServer = None):
		threading.Thread.__init__(self)
		self.running = True
		logging.info("Initialising serial Arduino connection on port: "+ str(PORT)+ ", BAUD: "+ str(BAUD))
		self.serialConnection = None
		
		try:
			self.serialConnection = serial.Serial(PORT, BAUD, 
												serial.EIGHTBITS, serial.PARITY_NONE, 	#bytesize=EIGHTBITS, parity=PARITY_NONE
												serial.STOPBITS_ONE, 						#stopbits=STOPBITS_ONE, 
												None, False, 				#timeout=None, xonxoff=False,
												False, None, 			# rtscts=False, write_timeout=None,
												False, )								#dsrdtr=False,
			self.XPUDPServer = XPUDPServer
			
			time.sleep(0.01)  
			# ensure there is no stale data in the buffer
			self.serialConnection.flushInput()  

		except serial.SerialException as e:
			errorMsg =  str(e)
			logging.error ( "Serial exception, unable to open connection with Arduino: "+errorMsg)
		time.sleep(0.001) # leave time for the arduino to boot up
		
		self.queuedCommands = []
		
		self.inputCallbacks = []
	
	## register a function to be called when an input changes state
	# @param callbackFunction 	the function to be called when the switch changes state
	#
	def registerInputChangedCallback(self, callbackFunction):
		self.inputCallbacks.append(callbackFunction)
	
	def sendPinList(self, componentType, pinList):
		if self.serialConnection != None:
			logging.info('arduinoSerial::sending pin list to arduino' + str(pinList))
			
			command = self.COMP_PIN_CMDS[componentType]
						
			for pin in pinList:
				command += pin
				command += ':'
			command = command[:-1]
			command += '\n'
			
			self.queuedCommands.append(command)
			logging.info ("Queuing command: "+ command)
			#self.serialConnection.write(command.encode())
			
			#time.sleep(0.01) # leave time for chars to transmit
	
	
	##--------------------------------------------------------------------------------------------------------------------
	# run. Do not call - use the start() method to start the thread, which will call run() 
	# infinite loop sending / receiving data to the arduino 
	#
	#--------------------------------------------------------------------------------------------------------------------
	def run(self):
		buffer =""
		startTime = time.time()
		
		while self.running and self.serialConnection!=None:
			time_running = time.time() - startTime
			
			# send commands
			if time_running >= 1.5:
				for command in self.queuedCommands:
					self.serialConnection.write(command.encode())
					#time.sleep(0.01) # leave time for chars to transmit
				self.queuedCommands = []
			
			data = self.serialConnection.read(self.serialConnection.in_waiting)		
			#data = self.serialConnection.read(200)		
			
			if len(data) > 0:
				#logging.error("")
				#logging.warning("Arduino data: "+ str(data) + "data length" + str( len(data)) )
				buffer += data.decode(encoding = 'latin_1')
				logging.info ("buffer: " + buffer)
				
				if ';' in buffer: # we have at least one valid command
					commands = buffer.split(';')
					buffer = commands[len(commands)-1] 	# we can now empty the buffer
					commands.pop() # remove the last element in the list which is an incomplete command
					for elem in commands:
						self.__processArduinoCmd(elem)  # we should now have a complete command from arduino to process
					
				else:
					commands = []
				logging.info('commands: ' + str(commands))
				
					
			time.sleep(0.00001)	
			
	## 
	def __processArduinoCmd(self, buffer):
		logging.info ("Process arduino command: "+ buffer)
		#logging.debug("Processing arduino command, command id: "+buffer[0:4])
		if buffer [0:4] == 'CMND':
			command = buffer[5:len(buffer)-1]
			logging.debug("i see a command"+ command+'\0')
			
			self.XPUDPServer.sendXPCmd(command+'\0')
		
		elif buffer [0:4] == 'DREF':
			dataref = buffer[5:len(buffer)-1]
						
			logging.debug("i see a dataref"+ dataref+'\0')
			
			self.XPUDPServer.sendXPDref(dataref+'\0')
		
		else:
			command_elems = buffer.split(":")
			if (command_elems[0] == 'SW' or command_elems[0] == 'POT') and len(command_elems) == 3:
				value = None
				pin = None
				try:
					pin = int(command_elems[1])
					value = int(command_elems[2])
				except ValueError:
					logging.error("Error in reading input command from Arduino")
					logging.error("Command: " + buffer)
				logging.info('callbacks:'+ str(self.inputCallbacks))
				
				if value is not None:
					for callback in self.inputCallbacks:
					#logging.info('calling callback'+ callback)
						callback(command_elems[0], pin, value)
					logging.info("Input "+command_elems[0]+ " on pin"+ command_elems[1]+ " Value: "+ command_elems[2])
				
					
		
	##--------------------------------------------------------------------------------------------------------------------
	# quit. Call to stop the thread 
	#
	#--------------------------------------------------------------------------------------------------------------------
	def quit(self):
		self.running = False
		if self.serialConnection!=None:
			self.serialConnection.close()
		logging.info("Arduino Connection stopped...")

