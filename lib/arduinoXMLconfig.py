#!/usr/bin/env python

import xml.etree.ElementTree as ET

INPUT_OUTPUT_TAGS = ["switches", "potentiometers", "rot_encoders", "leds", "pwms"]
INPUT_OUTPUT_TAGS_ACTIONS = {"switches":'Add switch', 
							 "potentiometers":'Add potentiometer', 
							 "rot_encoders":'Add rotary encoder', 
							 "leds":'Add LED', 
							 "pwms":'Add PWM'}
class arduinoConfig():

	def __init__(self, ardXMLconfigFile):
		self.tree = ET.parse(ardXMLconfigFile)
		self.root = self.tree.getroot()
		
		for child in self.root:
			print (child.tag, child.attrib)
	
	
	def addInputOutput(self, arduinoSerialNr, inputOutputType):
		print("Add InOutput type ",inputOutputType, "to Arduino serial nr:", arduinoSerialNr)
		ardTag = self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']")[0]
		inputOutputTag = ardTag.findall(".//"+inputOutputType)[0]
		switch = ET.SubElement(inputOutputTag, "switch")
		switch.set('id', arduinoSerialNr+'1')
		
		ET.dump(self.root)
		#print(self.tree)
		#print(self.root.findall(".//arduino[@serial_nr='"+arduinoSerialNr+"']"))