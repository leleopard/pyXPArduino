import threading
import lib.arduinoSerial as ardSerial
import lib.serialArduinoUtils
import logging
import time
import re
from operator import itemgetter

logger = logging.getLogger('Arduino')

class Arduino(threading.Thread):
	
	## constructor 
	# @param PORT: port the arduino is connected to
	# @param BAUD: BAUD setting for the serial port - needs to be the same as how the arduino is configured
	#
	def __init__(self, ardSerialNumber, PORT, BAUD, XPUDPServer, arduinoXMLconfig):
		threading.Thread.__init__(self)
		self.running = True
		self.connected = False
		
		self.ardSerialNumber = ardSerialNumber
		self.ardXMLconfig = arduinoXMLconfig
		self.XPUDPServer = XPUDPServer
		
		# Initialise connection, first we will check that the Arduino with this serial nr is still connected on this port
		
		connected_PORT = lib.serialArduinoUtils.returnArduinoPort(ardSerialNumber)
		ardDataDict = self.ardXMLconfig.getArduinoData(self.ardSerialNumber)
		logger.debug("connected_PORT = "+ str(connected_PORT))
		if connected_PORT == None: # then the arduino is not connected, no point trying to get a serial connection going
			self.connected = False
			logger.error("Arduino serial "+self.ardSerialNumber+", name: "+ardDataDict['name']+", unable to connect on port "+PORT)
			
		else: # the arduino is connected, we will attempt to connect on the the PORT value found as the arduino could have been reconnected to another port
			self.serialConnection = ardSerial.ArduinoSerial(connected_PORT, BAUD)
			if self.serialConnection.connected == True:
				self.serialConnection.start()
				self.serialConnection.registerInputChangedCallback(self.inputChanged)
				
				self.ardXMLconfig.registerComponentAttributeChangedCallback(self.updateComponentList) # 
				time.sleep(0.01) 
				self.updateComponentList('*', '', self.ardSerialNumber, 'pin') # set the pins as switches on arduino
				self.ardXMLconfig.updateArduinoAttribute(self.ardSerialNumber, 'baud',str(BAUD))
				self.connected = True
				logger.info("Arduino serial "+self.ardSerialNumber+", name: "+ardDataDict['name']+", connected on port "+PORT)
			else:
				self.connected = False
				logger.error("Arduino serial "+self.ardSerialNumber+", name: "+ardDataDict['name']+", unable to connect on port "+PORT)
				
				
	##  run. Do not call - use the start() method to start the thread, which will call run() 
	# infinite loop sending / receiving data to the arduino 
	#
	def run(self):
		buffer =""
		startTime = time.time()
		
		while self.running:
			# obtain list of pwm outputs & associated actions
			if self.connected == True:
				self.__refreshOutputs('pwm')
				self.__refreshOutputs('servo')
				self.__refreshOutputs('dig_output')
			time.sleep(0.01) 
	
	## internal method, refreshes the outputs of the arduino if connected (queues commands on the arduinoSerial instance) - called in loop by the thread main loop
	# @param outputType 	the type of output to refresh ('pwm', 'servo' etc...) although not used at present
	#
	def __refreshOutputs(self, outputType):
		if self.connected == True:
			compList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, outputType)
			#logger.debug('refresh outputs for output type: '+str(outputType))
			for comp in compList:
				if comp['pin'] != '':
					compActions = self.ardXMLconfig.getComponentActions(self.ardSerialNumber, outputType, comp['pin'] )
					#print(compActions)
					for action in compActions:
						drefValue = self.XPUDPServer.getData(action['cmddref'] + "[" + action['index'] + "]")
						prevDrefValue = 0.0
						try:
							prevDrefValue = float(action['state'])
						except ValueError:
							pass
							#logger.warning('Unable to convert dref value, defaulting to 0.0')
						if abs(prevDrefValue - drefValue) > 0.01:
							action['state'] = str(drefValue)
							logger.debug(outputType+' XPLANE DREF value, DREF: '+action['cmddref']+' Value: '+str(drefValue))
							pointsList = self.__returnPointsList(action['setToValue'])
							outPWMvalue = self.__returnLinearInterpolationY(drefValue, pointsList)
							logger.debug('Out '+ outputType + ' value: '+ str(outPWMvalue))
							self.ardXMLconfig.updateComponentActions(self.ardSerialNumber, outputType, comp['pin'], compActions )
							
							try:
								self.serialConnection.sendOutputValue(comp['pin'], outputType, int(outPWMvalue))
							except:
								pass
							
	## if arduino connected, executes the commands and datarefs associated with a component connected to that pin when it changes state
	# will be called by the arduinoSerial connection when it receives a command from the arduino
	# @param inputType 	the arduino code for the input ('SW', 'POT'...)
	# @param pin	the number of the pin 
	# @param value	the value of the input on this pin - for a switch 0 or 1, for a pot 0-1023 etc...
	#
	def inputChanged(self, inputType, pin, value):
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
				rot_enc_state = 'up'
				if value < 0 :
					rot_enc_state = 'down'
					
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
							self.XPUDPServer.sendXPCmd(action ['cmddref'], sendContinuous)
						if action['action_type'] == 'cmd' and action['state'] != rot_enc_state and action['continuous'] == 'True': # suppress any continuous cmd
							self.XPUDPServer.stopSendingXPCmd(action ['cmddref'])
							
						if action['action_type'] == 'dref' and action['state'] == rot_enc_state:
							self.XPUDPServer.sendXPDref(action['cmddref'],action['index'],action['setToValue'])
							
	## gets the list of input and output components for this arduino of the type passed in argument, and initialises the arduino board pins 
	# @param componentType	the type of component to update, pass '*' to update all types. 
	# @param switchSerialNr		not used?
	# @param ardSerialNr		must provide this arduino's serial number - not sure why needed need to review?
	# @param attribute			has to be 'pin'
	#
	def updateComponentList(self, componentType, switchSerialNr, ardSerialNr, attribute):
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
	
	## stop the thread, call when exiting the application to cleanly close the connections
	#
	def quit(self):
		if self.connected == True:
			self.serialConnection.quit()
		self.running = False
		logger.info('Arduino thread stopped, ard serial nr'+self.ardSerialNumber)
	
	## returns True if value is in any of the intervals passed in the intervalsList, False otherwise 
	# @param value 	float value 
	# @param intervalsList 	in format [[x1,x2], ... [xn, xn+1]]
	#
	def __isValueInIntervals(self, value, intervalsList):
		for interval in intervalsList:
			if value >= interval[0] and value <= interval[1]:
				return True
		
		return False
	
	def __returnLinearInterpolationY(self, xValue, linearSeriesPoints):
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
					return yValue
	
	## parses a string of points in format [x1,y1],[x2,y2],...[xn,yn] and returns a list of points sorted by their x value in format [[x float1,y float1], ...[x floatn,y floatn]]
	# @param pointsString 	the string of points to parse
	#
	def __returnPointsList(self, pointsString):
		pointsList = []
		logger.debug('Points list string: '+pointsString)
		pointsStringList = re.findall('\[[ -]*?[0-9]+.*?[0-9]*?[,]+[ -]*?[0-9]+.*?[0-9]*?[ ]*?\]', 
										pointsString)	# find all points format [nr,nr]
		
		for pointString in pointsStringList:
			pointString = re.sub('[\[\] ]+', '', pointString)	#strip spaces, [ and ]
			#print("interval string stripped of []: ", pointString)
			
			valueStrings = pointString.split(',')
			
			if len(valueStrings) == 2:
				#print("valueStrings: ", valueStrings)
				pointsList.append([ float(valueStrings[0]), float(valueStrings[1])])
		
		# let's order the table by ascending x of each pointString
		
		pointsList.sort(key=itemgetter(0))
				
		
		return pointsList
	
	
