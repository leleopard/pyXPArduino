#!/usr/bin/env python

import xml.etree.ElementTree as ET
import logging

ARD_BAUD = ['9600', '19200', '38400', '57600', '74880', '115200', '230400', '250000']

INPUT_OUTPUT_TAGS = ["switches", "potentiometers", "rot_encoders", "dig_outputs", "pwms", "servos"]
INPUT_OUTPUT_ELEMS_TAGS = ["switch", "potentiometer", "rot_encoder", "dig_output", "pwm", "servo"]
INPUT_OUTPUT_TAGS_REF = {"switches":		{'add_action':'Add switch','child_tag':'switch'},
						"potentiometers":	{'add_action':'Add potentiometer','child_tag':'potentiometer'},
						"rot_encoders":		{'add_action':'Add rotary encoder','child_tag':'rot_encoder'},
						"dig_outputs":		{'add_action':'Add digital output','child_tag':'dig_output'},
						"pwms":				{'add_action':'Add PWM','child_tag':'pwm'},
						"servos":			{'add_action':'Add servo','child_tag':'servo'}}

DIG_IO_PINS = ['22','23','24','25','26','27','28','29','30','31','32','33','34','35',
				'36','37','38','39','40','41','42','43','44','45','46','47',
				'48','49','50','51','52','53']

POT_PINS = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

PWM_PINS = ['2','3','4','5','6','7','8','9','10','11','12','13']

class arduinoConfig():

	def __init__(self, ardXMLconfigFile):
		self.tree = ET.parse(ardXMLconfigFile)
		self.root = self.tree.getroot()
		self.ardXMLconfigFile = ardXMLconfigFile

		self.componentAttributeChangedCallbacks = []
		#for child in self.root:
		#	print (child.tag, child.attrib)

	def addInputOutput(self, arduinoSerialNr, inputOutputType):
		logging.debug("Add InOutput type ",inputOutputType, "to Arduino serial nr:", arduinoSerialNr)
		ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
		inputOutputTag = ardTag.findall(".//"+inputOutputType)[0]
		# find all existing items under this tag
		items = list(inputOutputTag.iter(INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag']))
		highest_index = 0
		for item in items:
			index = int(str(item.attrib['id'])[-1:])
			if index>= highest_index:
				highest_index = index +1


		inputoutput = ET.SubElement(inputOutputTag,INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag'])
		inputoutput.set('id', inputOutputTag.tag+"_"+arduinoSerialNr+"_"+str(highest_index))
		inputoutput.set('name', INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag']+" "+str(highest_index))
		#if INPUT_OUTPUT_TAGS_REF[inputOutputTag.tag]['child_tag'] == 'switch':
		inputoutput.set('pin', '')
		inputoutput.set('state', 'on')

		ET.dump(self.root)


	def addArduino(self, port, name, description, serial_number, manufacturer):
		ardTag = ET.SubElement(self.root, 'arduino')
		ardTag.set('port', port)
		ardTag.set('name', name)
		ardTag.set('description', description)
		ardTag.set('serial_nr', serial_number)
		ardTag.set('manufacturer', manufacturer)
		ardTag.set('baud', '115200')

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

		digOutputsTag = ET.SubElement(outputTag, 'dig_outputs')
		digOutputsTag.set('description', 'Digital Outputs')
		pwmsTag = ET.SubElement(outputTag, 'pwms')
		pwmsTag.set('description', 'PWMs')
		servosTag = ET.SubElement(outputTag, 'servos')
		servosTag.set('description', 'Servos')

	def removeArduino(self, arduinoSerialNr):
		ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
		self.root.remove(ardTag)

	def getArduinoList(self):
		ardTags = self.root.findall(".//arduino")
		ardList = []
		if len(ardTags) > 0: # arduino has been found
			for ardTag in ardTags:
				ardDict = {'port': ardTag.attrib['port'],
						'baud': ardTag.attrib['baud'],
						'name': ardTag.attrib['name'],
						'description': ardTag.attrib['description'],
						'serial_nr': ardTag.attrib['serial_nr'],
						'manufacturer': ardTag.attrib['manufacturer']}
				ardList.append(ardDict)
			return ardList
		else:
			return ardList

	def removeInputOutput(self, arduinoSerialNr, inputOutputID):
		logging.debug("Remove InOutput ID ",inputOutputID, "from Arduino serial nr:", arduinoSerialNr)
		ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
		inputOutputTag = ardTag.findall(".//*[@id='"+inputOutputID+"']")[0]
		logging.debug("ID to remove found: ", inputOutputTag.attrib['id'])
		parent = ardTag.findall(".//*[@id='"+inputOutputID+"']/..")[0]
		parent.remove(inputOutputTag)

		ET.dump(self.root)

	def saveToXMLfile(self):
		self.tree.write(self.ardXMLconfigFile)


	## find actions for component by component type, pin and arduino serial number, returns a list of actions.
	# @return list of actions in form [{'state': action.attrib['state'],
	#									'action_type': action.attrib['action_type'],
	#									'cmddref': action.text}]
	def getComponentActions(self, arduinoSerialNr, componentType, pin):
		actionsList = []
		ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
		if len(ardTags) > 0: # arduino has been found
			compTag = ardTags[0].findall(".//"+componentType+"[@pin='"+str(pin)+"']")
			if len(compTag) > 0: # component has been found
				actions = list(compTag[0].iter('action'))

				for action in actions:
					#logging.debug('getComponentActions::action:'+str(action.text))

					index = '0'
					setToValue = '0.0'
					continuous = 'False'
					cmddref = ''
					if action.text != None:
						cmddref = action.text

					try:
						index = action.attrib['index']
						setToValue = action.attrib['setToValue']
						continuous = action.attrib['continuous']
					except:
						pass
					actionsList.append({'state': action.attrib['state'],
										'action_type': action.attrib['action_type'],
										'cmddref': cmddref,
										'index': index,
										'setToValue': setToValue,
										'continuous': continuous})

		return actionsList

	## update actions for component by component type, pin and arduino serial number.
	# @param actionsList list of actions in form [{'state': action.attrib['state'],
	#									'action_type': action.attrib['action_type'],
	#									'cmddref': action.text}]
	def updateComponentActions(self, arduinoSerialNr, componentType, pin, actionsList):
		ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
		if len(ardTags) > 0: # arduino has been found
			compTag = ardTags[0].findall(".//"+componentType+"[@pin='"+str(pin)+"']")
			if len(compTag) > 0: # switch has been found

				for action in list(compTag[0]): # first remove all actions
					compTag[0].remove(action)

				for action in actionsList:
					actionTag = ET.SubElement(compTag[0], 'action')
					actionTag.set('state', action['state'])
					actionTag.set('action_type', action['action_type'])
					try:
						actionTag.set('index', action['index'])
						actionTag.set('setToValue', action['setToValue'])
					except:
						pass
					actionTag.text = action['cmddref']



	## returns the attribute value for a component searching by component type, pin and arduino serial number.
	# @return attribute or '' if not found
	def getComponentAttribute(self, arduinoSerialNr, componentType, pin, attribute):
		ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
		if len(ardTags) > 0: # arduino has been found
			compTag = ardTags[0].findall(".//"+componentType+"[@pin='"+str(pin)+"']")
			if len(compTag) > 0: # component has been found
				return compTag[0].attrib[attribute]

		return ''

	## return list of components for a given arduino, search by arduino serial ID and component type.
	# @return list of components in form [{'name': switchTag.attrib['name'],
	#									'id': switchTag.attrib['id'],
	#									'pin': pin,
	#									'state': compTag.attrib['state']}]
	def getComponentList(self, arduinoSerialNr, componentType):
		compList = []
		ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
		if len(ardTags) > 0: # arduino has been found
			compTags = ardTags[0].findall(".//"+componentType)
			for compTag in compTags:
				pin =''
				if 'pin' in compTag.attrib:
					pin = compTag.attrib['pin']
				compList.append({'name': compTag.attrib['name'],
								'id': compTag.attrib['id'],
								'pin': pin,
								'state': compTag.attrib['state']})

		return compList


	## find component by serial number, returns a dictionary with its attribute values or None if not found.
	# @param compSerialNr	the ID of the component
	# @param componentType the type of component: 'switch', 'potentiometer', 'rot_encoder', 'led', 'pwm'
	#
	def getComponentData(self, compSerialNr, componentType):
		compTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']")
		if len(compTag) > 0: # comp has been found
			pin =''
			if 'pin' in compTag[0].attrib:
				pin = compTag[0].attrib['pin']
			actions = list(compTag[0].iter('action'))
			#print("actions:", len(actions))
			actionsList = []
			for action in actions:
				#print('action:',action)

				index = '0'
				setToValue = '0.0'
				continuous = 'False'
				try:
					index = action.attrib['index']
					setToValue = action.attrib['setToValue']
					continuous = action.attrib['continuous']
				except:
					pass

				actionsList.append({'state': action.attrib['state'],
									'action_type': action.attrib['action_type'],
									'cmddref': action.text,
									'index': index,
									'setToValue': setToValue,
									'continuous': continuous})
			compDict = {'name': compTag[0].attrib['name'],
					'id': compTag[0].attrib['id'],
					'pin': pin,
					'state': compTag[0].attrib['state'],
					'actions': actionsList}

			return compDict
		else:
			return None


	## register a callback function to be called when a component attribute has changed data is updated
	# @param callback 	callback function, it will be passed componentType, compSerialNr,ardSerialNr, attribute
	#
	def registerComponentAttributeChangedCallback(self, callback):
		self.componentAttributeChangedCallbacks.append(callback)


	## updates component data - id, name, arduino pin, and replace actions with those passed in parameter
	# @param compSerialNr  the id of the component to update
	# @param componentType the type of component: 'switch', 'potentiometer', 'rot_encoder', 'led', 'pwm'
	# @param switchData  dictionary formatted as {'id': 'id123', 'name': 'myname', 'pin': 'arduino pin nr'}
	# @param switchActions  list of dictionaries, one per action, each formatted as {'switch_state': 'on' or 'off', 'action_type': 'cmd' or 'dref, 'cmddref': 'command or dataref string'}
	#
	def updateComponentData(self, compSerialNr, componentType, switchData, switchActions = []):
		logging.debug('Update Component Data, type: '+componentType)
		compTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']")
		if len(compTag) > 0: # component has been found
			#find the switch arduino parent element
			ardTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']......")
			ardSerialNr = ardTag[0].attrib['serial_nr']
			#logging.debug (ardTag)
			#logging.debug ('ARD serial nr: '+ardTag[0].attrib['serial_nr'])

			self.updateComponentAttribute(compSerialNr, componentType,'id', switchData['id'])
			self.updateComponentAttribute(compSerialNr, componentType,'name', switchData['name'])
			self.updateComponentAttribute(compSerialNr, componentType,'pin', switchData['pin'])

			for action in list(compTag[0]): # first remove all actions
				compTag[0].remove(action)

			for action in switchActions:
				actionTag = ET.SubElement(compTag[0], 'action')
				actionTag.set('state', action['state'])
				actionTag.set('action_type', action['action_type'])
				try:
					actionTag.set('continuous', action['continuous'])
				except:
					actionTag.set('continuous', '')
				try:
					actionTag.set('index', action['index'])
				except:
					actionTag.set('index', '')
				try:
					actionTag.set('setToValue', action['setToValue'])
				except:
					actionTag.set('setToValue', '')
				actionTag.text = action['cmddref']

		else:
			return -1

	## updates component attribute
	# @param compSerialNr  the id of the component to update
	# @param componentType the type of component: 'switch', 'potentiometer', 'rot_encoder', 'led', 'pwm'
	# @param attribute the attribute of the component to update
	# @param attributeValue   the value to set the attribute to
	#
	def updateComponentAttribute(self, compSerialNr, componentType, attribute, attributeValue):
		logging.debug('Update component attribute: '+compSerialNr+' attribute: ' +attribute+' value:'+attributeValue )
		compTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']")
		if len(compTag) > 0: # component has been found
			#print("component found")
			#find the component arduino parent element
			ardTag = self.root.findall(".//"+componentType+"[@id='"+compSerialNr+"']......")
			ardSerialNr = ardTag[0].attrib['serial_nr']
			if compTag[0].attrib[attribute] != attributeValue: # then the value has changed and must be updated
				compTag[0].set(attribute, attributeValue)
				# and we notify all callbacks of this attribute change
				for callback in self.componentAttributeChangedCallbacks:
					callback(componentType, compSerialNr,ardSerialNr, attribute)

		else:
			return -1

	## find arduino by serial number, returns a dictionary with its attribute values or None if not found.
	# @param arduinoSerialNr  the serial number of the arduino
	#
	def getArduinoData(self, arduinoSerialNr):
		ardTags = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")
		if len(ardTags) > 0: # arduino has been found
			ardDict = {'port': ardTags[0].attrib['port'],
					'baud': ardTags[0].attrib['baud'],
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
			ardTags[0].set('baud', ardData['baud'])
			ardTags[0].set('name', ardData['name'])
			ardTags[0].set('description', ardData['description'])
			ardTags[0].set('serial_nr', ardData['serial_nr'])
			ardTags[0].set('manufacturer', ardData['manufacturer'])


		else :
			return -1
