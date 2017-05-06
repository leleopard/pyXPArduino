#!/usr/bin/env python

import xml.etree.ElementTree as ET

INPUT_OUTPUT_TAGS = ["switches", "potentiometers", "rot_encoders", "leds", "pwms"]
INPUT_OUTPUT_ELEMS_TAGS = ["switch", "potentiometer", "rot_encoder", "led", "pwm"]
INPUT_OUTPUT_TAGS_REF = {"switches":		{'add_action':'Add switch','child_tag':'switch'}, 
						"potentiometers":	{'add_action':'Add potentiometer','child_tag':'potentiometer'}, 
						"rot_encoders":		{'add_action':'Add rotary encoder','child_tag':'rot_encoder'}, 
						"leds":				{'add_action':'Add LED','child_tag':'led'}, 
						"pwms":				{'add_action':'Add PWM','child_tag':'pwm'}}
						
DIG_IO_PINS = ['22','23','24','25','26','27','28','29','30','31','32','33','34','35',
				'36','37','38','39','40','41','42','43','44','45','46','47',
				'48','49','50','51','52','53']
class arduinoConfig():

	def __init__(self, ardXMLconfigFile):
		self.tree = ET.parse(ardXMLconfigFile)
		self.root = self.tree.getroot()
		self.ardXMLconfigFile = ardXMLconfigFile
		
		for child in self.root:
			print (child.tag, child.attrib)
	
	
	def addInputOutput(self, arduinoSerialNr, inputOutputType):
		print("Add InOutput type ",inputOutputType, "to Arduino serial nr:", arduinoSerialNr)
		ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
		inputOutputTag = ardTag.findall(".//"+inputOutputType)[0]
		# find all existing items under this tag
		items = list(inputOutputTag.iter(INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag']))
		highest_index = 0
		for item in items:
			index = int(str(item.attrib['id'])[-1:])
			if index>= highest_index:
				highest_index = index +1
				
		
		switch = ET.SubElement(inputOutputTag,INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag'])
		switch.set('id', inputOutputTag.tag+"_"+arduinoSerialNr+"_"+str(highest_index))
		switch.set('name', INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag']+" "+str(highest_index))
		
		ET.dump(self.root)
	
	def addArduino(self, port, name, description, serial_number, manufacturer):
		ardTag = ET.SubElement(self.root, 'arduino')
		ardTag.set('port', port)
		ardTag.set('name', name)
		ardTag.set('description', description)
		ardTag.set('serial_nr', serial_number)
		ardTag.set('manufacturer', manufacturer)
		
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
		
		ledsTag = ET.SubElement(outputTag, 'leds')
		ledsTag.set('description', 'LEDs')
		pwmsTag = ET.SubElement(outputTag, 'pwms')
		pwmsTag.set('description', 'PWMs')
		
	def removeArduino(self, arduinoSerialNr):
		ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
		self.root.remove(ardTag)
		
	def removeInputOutput(self, arduinoSerialNr, inputOutputID):
		print("Remove InOutput ID ",inputOutputID, "from Arduino serial nr:", arduinoSerialNr)
		ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
		inputOutputTag = ardTag.findall(".//*[@id='"+inputOutputID+"']")[0]
		print("ID to remove found: ", inputOutputTag.attrib['id'])
		parent = ardTag.findall(".//*[@id='"+inputOutputID+"']/..")[0]
		parent.remove(inputOutputTag)
		
		ET.dump(self.root)
	
	def saveToXMLfile(self):
		self.tree.write(self.ardXMLconfigFile)
		
	## find switch by serial number, returns a dictionary with its attribute values or None if not found.
	#
	def getSwitchData(self, switchSerialNr):
		switchTag = self.root.findall(".//switch[@id='"+switchSerialNr+"']")
		if len(switchTag) > 0: # switch has been found
			pin =''
			if 'pin' in switchTag[0].attrib: 
				pin = switchTag[0].attrib['pin']
			actions = list(switchTag[0].iter('action'))
			print("actions:", len(actions))
			actionsList = []
			for action in actions:
				print('action:',action)
				actionsList.append({'switch_state': action.attrib['switch_state'], 
									'action_type': action.attrib['action_type'], 
									'cmddref': action.text})
			switchDict = {'name': switchTag[0].attrib['name'],
					'id': switchTag[0].attrib['id'],
					'pin': pin, 
					'actions': actionsList}
			
			return switchDict
		else:
			return None
	
	## updates switch data - id, name, arduino pin, and replace actions with those passed in parameter
	# @param switchSerialNr  the id of the switch to update
	# @param switchData  dictionary formatted as {'id': 'id123', 'name': 'myname', 'pin': 'arduino pin nr'}
	# @param switchActions  list of dictionaries, one per action, each formatted as {'switch_state': 'on' or 'off', 'action_type': 'cmd' or 'dref, 'cmddref': 'command or dataref string'}
	
	def updateSwitchData(self, switchSerialNr, switchData, switchActions = []):
		switchTag = self.root.findall(".//switch[@id='"+switchSerialNr+"']")
		if len(switchTag) > 0: # switch has been found
			switchTag[0].set('id', switchData['id'])
			switchTag[0].set('name', switchData['name'])
			switchTag[0].set('pin', switchData['pin'])
		
			for action in list(switchTag[0]): # first remove all actions
				switchTag[0].remove(action)
				
			for action in switchActions:
				actionTag = ET.SubElement(switchTag[0], 'action')
				actionTag.set('switch_state', action['switch_state'])
				actionTag.set('action_type', action['action_type'])
				actionTag.text = action['cmddref']
				
		else:
			return -1
	
	## find arduino by serial number, returns a dictionary with its attribute values or None if not found.
	# 
	def getArduinoData(self, arduinoSerialNr):
		ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
		if len(ardTags) > 0: # arduino has been found
			ardDict = {'port': ardTags[0].attrib['port'],
					'name': ardTags[0].attrib['name'],
					'description': ardTags[0].attrib['description'],
					'serial_nr': ardTags[0].attrib['serial_nr'],
					'manufacturer': ardTags[0].attrib['manufacturer']}
			return ardDict
		else:
			return None
			
	def updateArduinoData(self, arduinoSerialNr, ardData):
		ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
		if len(ardTags) > 0: # arduino has been found
			ardTags[0].set('port', ardData['port'])
			ardTags[0].set('name', ardData['name'])
			ardTags[0].set('description', ardData['description'])
			ardTags[0].set('serial_nr', ardData['serial_nr'])
			ardTags[0].set('manufacturer', ardData['manufacturer'])
			
			
		else :
			return -1
			