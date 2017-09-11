import logging
import xml.etree.ElementTree as ET

from PyQt5 import QtCore, QtGui, QtWidgets
import gui.xpudpconfigdialog as xpudpconfigdialog
import lib.XPlaneUDPServer as XPUDP


class pyXPUDPConfigDialog(QtWidgets.QDialog, xpudpconfigdialog.Ui_Dialog):
	def __init__(self, XMLconfigFile):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		
		self.ardXMLconfigFile = XMLconfigFile
		self.tree = ET.parse(self.ardXMLconfigFile)
		self.root = self.tree.getroot()
		
		self.refreshForm()
		
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.updateUDPStatusLabel)
		self.timer.start(500)
		
		#XPUDP.pyXPUDPServer
	
	def exec(self):
		self.refreshForm()
		return(super().exec())
	
	def updateUDPStatusLabel(self):
		self.UDPStatusLabel.setText(XPUDP.pyXPUDPServer.statusMsg)
	
	def buttonBoxClicked(self, button):
		logging.debug('button box clicked')
		print(button)
		
		if button == self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply):
			logging.debug('apply clicked')
			self.restartUDPServer()
		
	def refreshForm(self):
		IPTag = self.root.findall(".//IP")
		XPIPTag = self.root.findall(".//XPIP")
		XPCompNameTag = self.root.findall(".//XPComputerName")
		RedirectUDPtrafficTag = self.root.findall(".//RedirectUDPtraffic")
		IPRedirectTag = self.root.findall(".//RedirectIP")
		
		try:
			self.IP_Address_LineEdit.setText(IPTag[0].attrib['address'])
			self.IP_Port_LineEdit.setText(IPTag[0].attrib['port'])
			self.XPIP_Address_LineEdit.setText(XPIPTag[0].attrib['address'])
			self.XPIP_Port_LineEdit.setText(XPIPTag[0].attrib['port'])
			self.XP_ComputerName_LineEdit.setText(XPCompNameTag[0].attrib['network_name'])
			state = RedirectUDPtrafficTag[0].attrib['state']
			if state == 'True':
				self.XP_RedirectTraffic_checkBox.setChecked(True)
				self.RedIP_Address_LineEdit.setText(IPRedirectTag[0].attrib['address'])
				self.RedIP_Port_LineEdit.setText(IPRedirectTag[0].attrib['port'])
				self.RedIP_Address_LineEdit.setEnabled(True)
				self.RedIP_Port_LineEdit.setEnabled(True)
			else:
				self.XP_RedirectTraffic_checkBox.setChecked(False)
				self.RedIP_Address_LineEdit.setText('')
				self.RedIP_Port_LineEdit.setText('')
				self.RedIP_Address_LineEdit.setEnabled(False)
				self.RedIP_Port_LineEdit.setEnabled(False)
				
		except:
			logging.error('error while retrieving xml data', exc_info=True)
	
	def redirectCheckboxStateChanged(self):
		if self.XP_RedirectTraffic_checkBox.isChecked() == True:
			self.RedIP_Address_LineEdit.setEnabled(True)
			self.RedIP_Port_LineEdit.setEnabled(True)
		else:
			self.RedIP_Address_LineEdit.setEnabled(False)
			self.RedIP_Port_LineEdit.setEnabled(False)
	
	def restartUDPServer(self):
		Address =(self.IP_Address_LineEdit.text(), int(self.IP_Port_LineEdit.text()))
		XPAddress =(self.XPIP_Address_LineEdit.text(), int(self.XPIP_Port_LineEdit.text()))
		XPComputerName = self.XP_ComputerName_LineEdit.text()
		
		XPUDP.pyXPUDPServer.restart(Address, XPAddress, XPComputerName)
		
		if self.XP_RedirectTraffic_checkBox.isChecked() == True:
			RedIPAddress = (self.RedIP_Address_LineEdit.text(), int(self.RedIP_Port_LineEdit.text()))
			XPUDP.pyXPUDPServer.enableRedirectUDPtoXP(RedIPAddress, XPAddress)
		else:
			XPUDP.pyXPUDPServer.disableRedirectUDPtoXP()
		
		
		
	def saveToXMLfile(self):
		IPTag = self.root.findall(".//IP")
		XPIPTag = self.root.findall(".//XPIP")
		XPCompNameTag = self.root.findall(".//XPComputerName")
		RedirectUDPtrafficTag = self.root.findall(".//RedirectUDPtraffic")
		IPRedirectTag = self.root.findall(".//RedirectIP")
		
		IPTag[0].set('address', self.IP_Address_LineEdit.text())
		IPTag[0].set('port', self.IP_Port_LineEdit.text())
		XPIPTag[0].set('address', self.XPIP_Address_LineEdit.text())
		XPIPTag[0].set('port', self.XPIP_Port_LineEdit.text())
		XPCompNameTag[0].set('network_name', self.XP_ComputerName_LineEdit.text())
		
		state = self.XP_RedirectTraffic_checkBox.isChecked()
		if state == True:
			RedirectUDPtrafficTag[0].set('state', 'True')
			IPRedirectTag[0].set('address', self.RedIP_Address_LineEdit.text())
			IPRedirectTag[0].set('port', self.RedIP_Port_LineEdit.text())
		else:
			RedirectUDPtrafficTag[0].set('state', 'False')
			IPRedirectTag[0].set('address', '')
			IPRedirectTag[0].set('port', '')
		
		self.tree.write(self.ardXMLconfigFile)
		