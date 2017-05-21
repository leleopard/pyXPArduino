
import lib.arduinoSerial as ardSerial
import logging
import time
import re
from operator import itemgetter

class Arduino():
	
	##--------------------------------------------------------------------------------------------------------------------
	# constructor 
	# @param PORT: port the arduino is connected to
	# @param BAUD: BAUD setting for the serial port - needs to be the same as how the arduino is configured
	#
	#--------------------------------------------------------------------------------------------------------------------
	def __init__(self, ardSerialNumber, PORT, BAUD, XPUDPServer, arduinoXMLconfig):
		
		self.ardSerialNumber = ardSerialNumber
		self.ardXMLconfig = arduinoXMLconfig
		self.XPUDPServer = XPUDPServer
		self.serialConnection = ardSerial.ArduinoSerial(PORT, BAUD)
		self.serialConnection.start()
		self.serialConnection.registerInputChangedCallback(self.inputChanged)
		
		self.ardXMLconfig.registerComponentAttributeChangedCallback(self.updateComponentList) # 
		time.sleep(0.01) 
		self.updateComponentList('*', '', self.ardSerialNumber, 'pin') # set the pins as switches on arduino
	
	## executes the commands and datarefs associated with a switch connected to that pin when it changes state
	#
	def inputChanged(self, inputType, pin, value):
		logging.info("ARD CLASS ard input changed callback, input Type: "+inputType+ ", pin" + str(pin) + " value:" + str(value))
		if inputType == 'SW':
			switch_state = 'on'
			if value == 0 :
				switch_state = 'off'
				
			logging.info('updating switch state to value:' + switch_state)
			compID = self.ardXMLconfig.getComponentAttribute( self.ardSerialNumber,'switch', pin, 'id')
			self.ardXMLconfig.updateComponentAttribute(compID, 'switch', 'state', switch_state)
			
			for action in self.ardXMLconfig.getComponentActions(self.ardSerialNumber, 'switch', pin):
				if action['cmddref']!= None:
					logging.info ("action type: "+ action['action_type']
									+ " action state: "+action['state'] 
									+ "switch state: " + switch_state
									+ " action: " + action ['cmddref'] )
					if action['action_type'] == 'cmd' and action['state'] == switch_state:
						self.XPUDPServer.sendXPCmd(action ['cmddref'])
						
					if action['action_type'] == 'dref' and action['state'] == switch_state:
						self.XPUDPServer.sendXPDref(action['cmddref'],action['index'],action['setToValue'])
		
		if inputType == 'POT':
			state = str(value)
			compID = self.ardXMLconfig.getComponentAttribute(self.ardSerialNumber, 'potentiometer', pin, 'id')
			self.ardXMLconfig.updateComponentAttribute(compID, 'potentiometer', 'state', state)
			
			for action in self.ardXMLconfig.getComponentActions(self.ardSerialNumber, 'potentiometer', pin):
				if action['cmddref']!= None:
					logging.info ("action type: "+ action['action_type']
									+ " action state: "+action['state'] 
									+ "pot state: " + state
									+ " action: " + action ['cmddref'] )
					
					if action['action_type'] == 'dref' :
						logging.info('DREF set to value:'+action['setToValue'])
						pointsList = self.__returnPointsList(action['setToValue'])
						logging.info('Points list: ' + str(pointsList))
						if len(pointsList) > 0:
							outValue = self.__returnLinearInterpolationY(float(state), pointsList)
							
							logging.info('Output value to XP DREF: ' +str(outValue))
							self.XPUDPServer.sendXPDref(action['cmddref'],action['index'],outValue)
					
					if action['action_type'] == 'cmd' :
						logging.info('CMD state:'+action['state'])
						intervalsList = self.__returnPointsList(action['state'])
						logging.info('Intervals list: ' + str(intervalsList))
						if len(intervalsList) > 0:
							if self.__isValueInIntervals(float(state), intervalsList):
								logging.info('Send XPlane CMD : ' +action['cmddref'])
								self.XPUDPServer.sendXPCmd(action['cmddref'])
							
	##
	# @param componentType	the type of component to update, pass '*' to update all types. 
	def updateComponentList(self, componentType, switchSerialNr, ardSerialNr, attribute):
		if ardSerialNr == self.ardSerialNumber and attribute == 'pin': # only update pins if this is us and the attribute that has changed is pin
			if componentType == '*' or componentType == 'switch':
				switchList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'switch')
				switchPinList = []
				
				for switch in switchList:
					if switch['pin'] != '':
						switchPinList.append(switch['pin'])
				logging.info ('Ard serial '+ self.ardSerialNumber+ 'switch pin list: ' + str(switchPinList))
				self.serialConnection.sendPinList('switch', switchPinList)
			
			if componentType == '*' or componentType == 'potentiometer':
				potList = self.ardXMLconfig.getComponentList(self.ardSerialNumber, 'potentiometer')
				potPinList = []
				
				for pot in potList:
					if pot['pin'] != '':
						potPinList.append(pot['pin'])
				logging.info ('Ard serial '+ self.ardSerialNumber+ 'pot pin list: ' + str(potPinList))
				self.serialConnection.sendPinList('potentiometer', potPinList)
			
	
		
	def quit(self):
		self.serialConnection.quit()
	
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
		if xValue < linearSeriesPoints[0][0]: 
			return linearSeriesPoints[0][1]
		
		nrPoints = len(linearSeriesPoints)
		
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
		logging.info('Points list string: '+pointsString)
		pointsStringList = re.findall('\[[ ]*?[0-9]+.*?[0-9]*?[,]+[ ]*?[0-9]+.*?[0-9]*?[ ]*?\]', 
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
	
	
