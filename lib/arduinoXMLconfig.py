#!/usr/bin/env python

import xml.etree.ElementTree as ET

INPUT_OUTPUT_TAGS = ["switches", "potentiometers", "rot_encoders", "leds", "pwms"]

class arduinoConfig():

	def __init__(self, ardXMLconfigFile):
		self.tree = ET.parse(ardXMLconfigFile)
		self.root = self.tree.getroot()
		
		for child in self.root:
			print (child.tag, child.attrib)
	