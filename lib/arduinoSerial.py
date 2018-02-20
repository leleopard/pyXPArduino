import threading
import sys
import logging
import time
import serial
import os, getpass
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

logger = logging.getLogger('arduinoSerial')

class ArduinoSerial(threading.Thread):

	COMP_PIN_CMDS = {'switch' 			: "SW_PINS:",
					'potentiometer' 	: "POT_PINS:",
					'pwm' 				: "PWM_PINS:",
					'rot_encoder' 		: "ROTENC_PINS:",
					'dig_output' 		: "DIGOUT_PINS:",
					'servo'				: "SERVO_PINS:"
					}

	OUTPUT_TYPE_CMDS = {'pwm' 				: "PWM:",
						'servo'				: "SERVO:",
						'dig_output'		: "DIGOUT:"
						}

	## constructor, will attempt to open a serial connection to the Arduino
	# @param PORT: port the arduino is connected to
	# @param BAUD: BAUD setting for the serial port - needs to be the same as how the arduino is configured
	#
	def __init__(self, PORT, BAUD, XPUDPServer = None):
		threading.Thread.__init__(self)
		self.arduinoReady = False
		self.arduinoFirmwareVersion = ''
		self.running = True
		self.queuedCommands = []
		self.inputCallbacks = []
		self.ardStateChangedCallbacks = []

		self.connected = False	# are we connected (serial connection successful) to the arduino
		logging.info("Ardserial running as user: "+getpass.getuser())
		logger.info("Initialising serial Arduino connection on port: "+ str(PORT)+ ", BAUD: "+ str(BAUD))
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


	## register a function to be called when an input changes state
	# @param callbackFunction 	the function to be called when the switch changes state
	#
	def registerInputChangedCallback(self, callbackFunction):
		self.inputCallbacks.append(callbackFunction)

	def registerArduinoStateChangedCallback(self, callbackFunction):
		"""
		Register callback to be called when the Arduino changes state. After initialisation, the Arduino board will send a message signaling it is ready to accept commands, and the version number of the firmware it is running

		:param callbackFunction: function that will be called when the state (True for arduino ready or False) or the version of the firmware (string) has changed. Your function will be passed 2 parameters: the state (bool) and the version nr (string)

		"""
		self.ardStateChangedCallbacks.append(callbackFunction)

	def sendOutputValue(self, pin, outputType, value):
		if self.arduinoReady == True:
			logger.debug('serial connection, sending output value '+ str(value) + ' for output type ' + outputType)
			command = self.OUTPUT_TYPE_CMDS[outputType]+pin+':'+str(value)+';'
			self.queuedCommands.append(command)
			logger.debug ("Queuing output command: "+ command)

	def sendPinList(self, componentType, pinList):
		if self.serialConnection != None:
			logger.info('arduinoSerial::sending pin list to arduino' + str(pinList))
			if len(pinList)>0: # only send if there are any pins!
				command = self.COMP_PIN_CMDS[componentType]

				for pin in pinList:
					command += pin
					command += ':'
				command = command[:-1]
				command += ';'

				self.queuedCommands.append(command)
				logger.debug ("Queuing command: "+ command)


	##--------------------------------------------------------------------------------------------------------------------
	# run. Do not call - use the start() method to start the thread, which will call run()
	# infinite loop sending / receiving data to the arduino
	#
	#--------------------------------------------------------------------------------------------------------------------
	def run(self):
		buffer =""
		startTime = time.time()
		lastTime = time.time()

		for callback in self.ardStateChangedCallbacks:
			callback(self.arduinoReady, self.arduinoFirmwareVersion)

		while self.running and self.serialConnection!=None:
			time_running = time.time() - startTime
			current_time = time.time()
			#if current_time-lastTime > 0.5:
			#	logger.info('ard serial running')
			#	lastTime = current_time

			# send commands
			if self.arduinoReady == True :
			#time_running >= 1.5:
				if len(self.queuedCommands) >0:
					logger.debug('command queue: '+str(self.queuedCommands))
				for command in self.queuedCommands:
					self.serialConnection.write(command.encode())
					time.sleep(0.02) # leave time for arduino to process to transmit
				self.queuedCommands = []

			data = self.serialConnection.read(self.serialConnection.in_waiting)
			#data = self.serialConnection.read(200)

			if len(data) > 0:
				#logger.error("")
				logger.debug("Arduino data ("+ str( len(data)) +" chars): "+ str(data) )
				buffer += data.decode(encoding = 'latin_1')
				#logger.debug ("buffer: " + buffer)

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

	##
	def __processArduinoCmd(self, buffer):
		logger.debug ("Process arduino command: "+ buffer)
		#logging.debug("Processing arduino command, command id: "+buffer[0:4])
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
					#logger.debug('calling callback'+ callback)
						callback(command_elems[0], pin, value)
					logger.debug("Input "+command_elems[0]+ " on pin"+ command_elems[1]+ " Value: "+ command_elems[2])



	## quit - Call to stop the thread
	#
	def quit(self):
		self.running = False
		if self.serialConnection!=None:
			self.serialConnection.close()
		self.arduinoReady == False
		self.arduinoFirmwareVersion = ''
		for callback in self.ardStateChangedCallbacks:
			callback(self.arduinoReady, self.arduinoFirmwareVersion)
		logger.info("Arduino Connection on port " + self.PORT + " stopped...")
