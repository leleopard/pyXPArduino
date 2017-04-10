#!/usr/bin/env python
#importing wx files
import wx
import gui
import XPArduinoDialogManageArduinos

import lib.serialArduinoUtils

 
#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class XPArduinoFrame(gui.mainFrame):
	#constructor
	def __init__(self,parent):
		#initialize parent class
		gui.mainFrame.__init__(self,parent)
		
		self.pickArduinoDialog = XPArduinoDialogManageArduinos.XPArduinoDialogManageArduinos(self)
		
		#self.ardTreeImageList = ImageList()
		self.arduinoDict = {}
		self.refreshArduinoTree()
		
		self.arduinoIcon = wx.Icon("Resources/ardIcon.png", wx.BITMAP_TYPE_PNG)
		self.inputIcon = wx.Icon("Resources/inputIcon.png", wx.BITMAP_TYPE_PNG)
		self.outputIcon = wx.Icon("Resources/outputIcon.png", wx.BITMAP_TYPE_PNG)
		
	def refreshArduinoTree(self):
		self.Arduino_dataViewTreeCtrl.DeleteAllItems()
		for arduino in self.arduinoDict:
			# insert Arduino tree element
			self.arduinoDict[arduino]['ardTreeElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(wx.dataview.NullDataViewItem,
																									self.arduinoDict[arduino]['Name'])
			# insert Inputs	tree elems																					
			self.arduinoDict[arduino]['ardTreeInputsElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(self.arduinoDict[arduino]['ardTreeElem'], 'Inputs')
			self.arduinoDict[arduino]['ardTreeSwitchesElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(self.arduinoDict[arduino]['ardTreeInputsElem'], 'Switches')
			self.arduinoDict[arduino]['ardTreePotsElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(self.arduinoDict[arduino]['ardTreeInputsElem'], 'Potentiometers')
			self.arduinoDict[arduino]['ardTreeRotEncsElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(self.arduinoDict[arduino]['ardTreeInputsElem'], 'Rotary Encoders')
			
			# insert Outputs tree elems
			self.arduinoDict[arduino]['ardTreeOutputsElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(self.arduinoDict[arduino]['ardTreeElem'], 'Outputs',-1,1)
			self.arduinoDict[arduino]['ardTreeLEDElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(self.arduinoDict[arduino]['ardTreeOutputsElem'], 'LED')
			self.arduinoDict[arduino]['ardTreePWMElem'] = self.Arduino_dataViewTreeCtrl.AppendContainer(self.arduinoDict[arduino]['ardTreeOutputsElem'], 'PWM Outputs')
			
			self.Arduino_dataViewTreeCtrl.Expand(self.arduinoDict[arduino]['ardTreeElem'])
			self.Arduino_dataViewTreeCtrl.SetItemIcon(self.arduinoDict[arduino]['ardTreeElem'], self.arduinoIcon)
			
			self.Arduino_dataViewTreeCtrl.Expand(self.arduinoDict[arduino]['ardTreeInputsElem'])
			self.Arduino_dataViewTreeCtrl.SetItemIcon(self.arduinoDict[arduino]['ardTreeInputsElem'], self.inputIcon)
			
			self.Arduino_dataViewTreeCtrl.Expand(self.arduinoDict[arduino]['ardTreeOutputsElem'])
			self.Arduino_dataViewTreeCtrl.SetItemIcon(self.arduinoDict[arduino]['ardTreeOutputsElem'], self.outputIcon)
			
	
	def addArduinoBoard(self,event):
		self.pickArduinoDialog.refreshArduinoList()
		self.pickArduinoDialog.ShowModal()
		
		
	def exitApp(self, event):
		exit()

		

	
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
app = wx.App(False)
 
frame = XPArduinoFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()