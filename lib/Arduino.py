
import lib.arduinoSerial as ardSerial
import logging
import time

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
		self.serialConnection.registerSwitchChangedCallback(self.switchChanged)
		
		self.ardXMLconfig.setSwitchDataChangedCallback(self.updateSwitchList) # 
		time.sleep(0.01) 
		self.updateSwitchList('', self.ardSerialNumber, 'pin') # set the pins as switches on arduino
	
	## executes the commands and datarefs associated with a switch connected to that pin when it changes state
	#
	def switchChanged(self, pin, value):
		logging.info("ARD CLASS ard switch changed callback, pin" + str(pin) + " value:" + str(value))
		switch_state = 'on'
		if value == 0 :
			switch_state = 'off'
		
		switchID = self.ardXMLconfig.getSwitchAttribute(self.ardSerialNumber, pin, 'id')
		self.ardXMLconfig.updateSwitchAttribute(switchID, 'state', switch_state)
		
		for action in self.ardXMLconfig.getSwitchActions(self.ardSerialNumber, pin):
			logging.info ("action type: "+ action['action_type']
							+ " action state: "+action['switch_state'] 
							+ "switch state: " + switch_state
							+ " action: " + action ['cmddref'] )
			if action['action_type'] == 'cmd' and action['switch_state'] == switch_state:
				self.XPUDPServer.sendXPCmd(action ['cmddref'])
				
			if action['action_type'] == 'dref' and action['switch_state'] == switch_state:
				self.XPUDPServer.sendXPDref(action['cmddref'],action['index'],action['setToValue'])
		
	
	def updateSwitchList(self, switchSerialNr, ardSerialNr, attribute):
		if ardSerialNr == self.ardSerialNumber and attribute == 'pin': # only update pins if this is us and the attribute that has changed is pin
			switchList = self.ardXMLconfig.getSwitchList(self.ardSerialNumber)
			switchPinList = []
			
			for switch in switchList:
				if switch['pin'] != '':
					switchPinList.append(switch['pin'])
					
			logging.info ('Ard serial '+ self.ardSerialNumber+ 'switch pin list: ' + str(switchPinList))
			self.serialConnection.sendSwitchPinList(switchPinList)
		
	def quit(self):
		self.serialConnection.quit()
	
