import logging

from PyQt5 import QtCore, QtGui, QtWidgets
import gui.instrumentEditForm as instrumentEditForm
import gui.pyXPdatarefCommandEditWidget as pyXPdatarefCommandEditWidget

import lib.XPrefData as XPrefData
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPpickXPDatarefDialog as pyXPpickXPDatarefDialog

from pySTGraphics import pyXPPanel
from pySTGraphics import OpenGL3lib
from pySTGraphics import graphicsGL3 as graphics
from pySTGraphics import conversionFunctions

import pyxpudpserver as XPUDP

class pyXPinstrumentEditForm(QtWidgets.QWidget, instrumentEditForm.Ui_instrumentEditForm):
    nameUpdated = QtCore.pyqtSignal(str,str)
    pinUpdated = QtCore.pyqtSignal(str)

    def __init__(self,widget, graphicsConfigFile, actionSave):
        super(self.__class__, self).__init__(widget)
        self.repopulating = True
        self.graphicsConfigFile = graphicsConfigFile
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.panel = pyXPPanel.pyXPPanel(self.graphicsConfigFile, 5) 
        
        self.componentCurrentName = ''
        
        self.repopulating = False


    def show(self, instrumentPath = None):
        self.repopulating = True
        
        if(instrumentPath == None) :
            pass
        else:
            self.instrumentPath = instrumentPath
            self.instrument = graphics.Container(self.instrumentPath)
            self.refreshInstrumentAttributes()
            
        logging.info("show instrument form, selected instrument path: %s", self.instrumentPath)
        
        self.refreshComponentsTableWidget()
        self.instrComponentEditPane.hide()
        
        self.repopulating = False
        super().show()
    
    def refreshComponentsTableWidget(self):
        self.componentsTable.setRowCount(0)
        
        components = self.instrument.containerConfig.getComponents()
        
        for component in components:
            index = self.componentsTable.rowCount()
            self.componentsTable.insertRow(index)
            item = QtWidgets.QTableWidgetItem(component['name'])
            self.componentsTable.setItem(index,0, item)
        self.componentsTable.resizeRowsToContents()
        self.componentsTable.resizeColumnsToContents()
    
    def refreshComponentConfigView(self):
        self.repopulating = True
        items = self.componentsTable.selectedItems()
        if len(items) > 0:
            item = items[0]
            logging.info("Refresh component name: %s", item.text())
            
            componentConfig = self.instrument.containerConfig.getComponentConfig(item.text())
            
            if componentConfig != None:
                self.lineEdit_compName.setText(componentConfig['name'])
                self.componentCurrentName = componentConfig['name']
                
                self.spinBox_layer.setValue(int(componentConfig['layer']))
                
                self.checkBox_maintainProportions.setChecked(componentConfig['maintainProportions'])
                self.checkBox_resizetoinstrument.setChecked(componentConfig['resizeToContainer'])
                
                self.spinBox_posx.setValue(int(componentConfig['position'][0]))
                self.spinBox_posy.setValue(int(componentConfig['position'][1]))
                
                self.spinBox_textclipw.setValue(int(componentConfig['cliprect'][0]))
                self.spinBox_textcliph.setValue(int(componentConfig['cliprect'][1]))
                
                self.lineEdit_textureFile.setText(componentConfig['texture'])
                
                self.spinBox_textorigx.setValue(int(componentConfig['origin'][0]))
                self.spinBox_textorigy.setValue(int(componentConfig['origin'][1]))
                
            self.instrComponentEditPane.show()
        self.repopulating = False
    
    def updateComponentConfig(self):
        if self.repopulating == False:
            configDict = {'texture': self.lineEdit_textureFile.text(),
                          'layer' : self.spinBox_layer.value(),
                          'position' : [self.spinBox_posx.value(), self.spinBox_posy.value()],
                          'cliprect' : [self.spinBox_textclipw.value(), self.spinBox_textcliph.value()],
                          'origin' : [self.spinBox_textorigx.value(), self.spinBox_textorigy.value()],
                          'name' : self.lineEdit_compName.text(),
                          'maintainProportions' : self.checkBox_maintainProportions.isChecked(),
                          'resizeToContainer' : self.checkBox_resizetoinstrument.isChecked()
                          
                        }
            self.instrument.containerConfig.updateComponentConfig(self.componentCurrentName, 'ImagePanel', configDict)
            self.instrument.containerConfig.saveToFile()
            
            component = self.instrument.getItemByName(self.componentCurrentName)
            if component != None:
                component.name = configDict['name']
                component.setPosition(configDict['position'])
            
            self.componentCurrentName = configDict['name']
        
    
    def refreshInstrumentAttributes(self):
        self.nameLineEdit.setText(self.instrument.containerConfig.getPanelConfig()['name'])
        size = self.instrument.containerConfig.getPanelConfig()['size']
        self.instrWidthSpinbox.setValue(int(size[0]))
        self.instrHeightSpinbox.setValue(int(size[1]))
        
    
    def updateInstrumentConfig(self):
        size = [self.instrWidthSpinbox.value(),
                    self.instrHeightSpinbox.value()]
        self.panel.setWindowSize(size[0],size[1])
        self.instrument.setPosition([0,0])
        self.instrument.resize(size)
        
        self.instrument.containerConfig.updatePanelConfig( [size[0]/2,size[1]/2], size, self.nameLineEdit.text())
        self.instrument.containerConfig.saveToFile()
        
    def run(self):
        logging.info("Running instrument, filepath: %s", self.instrumentPath)
        
        self.panel.initialise()
      
        self.instrument.initialise(self.panel.batchImageRenderer)
        
        size = self.instrument.getSize()
        self.instrument.setPosition([size[0]/2,size[1]/2])
        self.panel.setWindowSize(size[0],size[1])
        self.panel.setDrawCallback(self.instrument.draw)
        self.panel.run()
        #self.instrument.batchImageRenderer = None
        #del self.instrument
        #del self.panel

    def hide(self):
        '''self.SWON_CMDS_TABLE.setRowCount(0)
        self.SWOFF_CMDS_TABLE.setRowCount(0)
        self.SWON_DREFS_TABLE.setRowCount(0)
        self.SWOFF_DREFS_TABLE.setRowCount(0)'''
        super().hide()
    '''
    def updateStateWidget(self, componentType, componentID, ardSerialNr = None, attribute = 'state'):
        logging.debug ('Update switch widget'+componentType)
        if componentType == 'switch' and componentID == self.componentID and attribute == 'state':
            componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)
            state = componentData['state']
            if state == 'on':
                self.switchStateButton.setChecked(True)
            else:
                self.switchStateButton.setChecked(False)

    def activateSave(self):
        if self.repopulating == False:
            self.actionSave.setEnabled(True)

    def testOnCommands(self):
        for i in range(0, self.SWON_CMDS_TABLE.rowCount()):
            item = self.SWON_CMDS_TABLE.item(i,0)
            actioncmddref = ''
            if item != None:
                actioncmddref = self.SWON_CMDS_TABLE.item(i,0).text()
                XPUDP.pyXPUDPServer.sendXPCmd(actioncmddref)

    def testOffCommands(self):
        for i in range(0, self.SWOFF_CMDS_TABLE.rowCount()):
            item = self.SWOFF_CMDS_TABLE.item(i,0)
            actioncmddref = ''
            if item != None:
                actioncmddref = self.SWOFF_CMDS_TABLE.item(i,0).text()
                XPUDP.pyXPUDPServer.sendXPCmd(actioncmddref)

    def testOnDatarefs(self):
        for i in range(0, self.SWON_DREFS_TABLE.rowCount()):
            item = self.SWON_DREFS_TABLE.item(i,0)
            actioncmddref = ''
            if item != None:
                actioncmddref = self.SWON_DREFS_TABLE.item(i,0).text()

                index = '0'
                setToValue = '0.0'

                item2 = self.SWON_DREFS_TABLE.item(i,1)
                if item2 != None:
                    index = self.SWON_DREFS_TABLE.item(i,1).text()

                item2 = self.SWON_DREFS_TABLE.item(i,2)
                if item2 != None:
                    setToValue = self.SWON_DREFS_TABLE.item(i,2).text()

                XPUDP.pyXPUDPServer.sendXPDref(actioncmddref, index, setToValue)

    def testOffDatarefs(self):
        for i in range(0, self.SWOFF_DREFS_TABLE.rowCount()):
            item = self.SWOFF_DREFS_TABLE.item(i,0)
            actioncmddref = ''
            if item != None:
                actioncmddref = self.SWOFF_DREFS_TABLE.item(i,0).text()

                index = '0'
                setToValue = '0.0'

                item2 = self.SWOFF_DREFS_TABLE.item(i,1)
                if item2 != None:
                    index = self.SWOFF_DREFS_TABLE.item(i,1).text()

                item2 = self.SWOFF_DREFS_TABLE.item(i,2)
                if item2 != None:
                    setToValue = self.SWOFF_DREFS_TABLE.item(i,2).text()

                XPUDP.pyXPUDPServer.sendXPDref(actioncmddref, index, setToValue)

    def updateXMLdata(self):
        if self.repopulating == False:
            actions = []
            index = 0
            for i in range(0, self.SWON_CMDS_TABLE.rowCount()):
                actioncmddref = self.SWON_CMDS_TABLE.cellWidget(i,0).lineEdit.text()

                action_continuous = 'False'
                if self.SWON_CMDS_TABLE.item(i,1) != None:
                    if self.SWON_CMDS_TABLE.item(i,1).checkState() == QtCore.Qt.Checked:
                        action_continuous = 'True'

                actions.append({'state':'on',
                              'action_type':'cmd',
                              'cmddref':actioncmddref,
                              'continuous':action_continuous})
                index = i

            for i in range(0, self.SWOFF_CMDS_TABLE.rowCount()):
                actioncmddref = self.SWOFF_CMDS_TABLE.cellWidget(i,0).lineEdit.text()

                action_continuous = 'False'
                if self.SWOFF_CMDS_TABLE.item(i,1) != None:
                    if self.SWOFF_CMDS_TABLE.item(i,1).checkState() == QtCore.Qt.Checked:
                        action_continuous = 'True'

                actions.append({'state':'off',
                              'action_type':'cmd',
                              'cmddref':actioncmddref,
                              'continuous':action_continuous})

            for i in range(0, self.SWON_DREFS_TABLE.rowCount()):
                actioncmddref = self.SWON_DREFS_TABLE.cellWidget(i,0).lineEdit.text()

                item = self.SWON_DREFS_TABLE.item(i,1)
                drefIndex = ''
                if item != None:
                    drefIndex = self.SWON_DREFS_TABLE.item(i,1).text()

                item = self.SWON_DREFS_TABLE.item(i,2)
                setToValue = ''
                if item != None:
                    setToValue = self.SWON_DREFS_TABLE.item(i,2).text()

                action_continuous = 'False'
                item = self.SWON_DREFS_TABLE.item(i,3)
                if item != None:
                    if self.SWON_DREFS_TABLE.item(i,3).checkState() == QtCore.Qt.Checked:
                        action_continuous = 'True'

                actions.append({'state':'on',
                              'action_type':'dref',
                              'cmddref':actioncmddref,
                              'index':drefIndex,
                              'setToValue':  setToValue,
                              'continuous':action_continuous })
                index = i

            for i in range(0, self.SWOFF_DREFS_TABLE.rowCount()):
                actioncmddref = self.SWOFF_DREFS_TABLE.cellWidget(i,0).lineEdit.text()

                item = self.SWOFF_DREFS_TABLE.item(i,1)
                drefIndex = ''
                if item != None:
                    drefIndex = self.SWOFF_DREFS_TABLE.item(i,1).text()

                item = self.SWOFF_DREFS_TABLE.item(i,2)
                setToValue = ''
                if item != None:
                    setToValue = self.SWOFF_DREFS_TABLE.item(i,2).text()

                action_continuous = 'False'
                item = self.SWOFF_DREFS_TABLE.item(i,3)
                if item != None:
                    if self.SWOFF_DREFS_TABLE.item(i,3).checkState() == QtCore.Qt.Checked:
                        action_continuous = 'True'

                actions.append({'state':'off',
                              'action_type':'dref',
                              'cmddref':actioncmddref,
                              'index':drefIndex,
                              'setToValue':  setToValue,
                              'continuous':action_continuous })
                index = i

            self.ardXMLconfig.updateComponentData(self.componentID, self.componentType,
                                                                {'id':self.IDlineEdit.text(),
                                                                'name':self.nameLineEdit.text(),
                                                                'pin':self.PIN_comboBox.currentText()},
                                                                actions)

            self.nameUpdated.emit(self.IDlineEdit.text(), self.nameLineEdit.text())
            self.actionSave.setEnabled(True)

    def updatePin(self):
        self.pinUpdated.emit(self.IDlineEdit.text())

    def addSwitchOnCommand(self):
        index = self.SWON_CMDS_TABLE.rowCount()
        self.SWON_CMDS_TABLE.insertRow(index)
        editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWON_CMDS_TABLE)
        editWidget.lineEdit.setText('')
        editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
        editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
        self.SWON_CMDS_TABLE.setCellWidget(index,0, editWidget)

        check_state = QtCore.Qt.Unchecked
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(check_state)
        self.SWON_CMDS_TABLE.setItem(index,1, item)
        self.SWON_CMDS_TABLE.resizeColumnsToContents()
        self.SWON_CMDS_TABLE.resizeRowsToContents()
        self.SWON_CMDS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    def rmSwitchOnCommand(self):
        row = self.SWON_CMDS_TABLE.currentRow()
        self.SWON_CMDS_TABLE.removeRow(row)
        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    def addSwitchOnDataref(self):
        index = self.SWON_DREFS_TABLE.rowCount()
        self.SWON_DREFS_TABLE.insertRow(index)
        editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWON_DREFS_TABLE)
        editWidget.lineEdit.setText('')
        editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
        editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
        self.SWON_DREFS_TABLE.setCellWidget(index,0, editWidget)

        item = QtWidgets.QTableWidgetItem('0')
        self.SWON_DREFS_TABLE.setItem(index,1, item)
        item = QtWidgets.QTableWidgetItem('0.0')
        self.SWON_DREFS_TABLE.setItem(index,2, item)

        check_state = QtCore.Qt.Unchecked
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(check_state)
        self.SWON_DREFS_TABLE.setItem(index,3, item)
        self.SWON_DREFS_TABLE.resizeColumnsToContents()
        self.SWON_DREFS_TABLE.resizeRowsToContents()
        self.SWON_DREFS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    def rmSwitchOnDataref(self):
        row = self.SWON_DREFS_TABLE.currentRow()
        self.SWON_DREFS_TABLE.removeRow(row)
        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    def addSwitchOffCommand(self):
        index = self.SWOFF_CMDS_TABLE.rowCount()
        self.SWOFF_CMDS_TABLE.insertRow(index)
        editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWOFF_CMDS_TABLE)
        editWidget.lineEdit.setText('')
        editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
        editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
        self.SWOFF_CMDS_TABLE.setCellWidget(index,0, editWidget)

        check_state = QtCore.Qt.Unchecked
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(check_state)
        self.SWOFF_CMDS_TABLE.setItem(index,1, item)

        self.SWOFF_CMDS_TABLE.resizeColumnsToContents()
        self.SWOFF_CMDS_TABLE.resizeRowsToContents()
        self.SWOFF_CMDS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    def rmSwitchOffCommand(self):
        row = self.SWOFF_CMDS_TABLE.currentRow()
        self.SWOFF_CMDS_TABLE.removeRow(row)
        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    def addSwitchOffDataref(self):
        index = self.SWOFF_DREFS_TABLE.rowCount()
        self.SWOFF_DREFS_TABLE.insertRow(index)
        editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWOFF_DREFS_TABLE)
        editWidget.lineEdit.setText('')
        editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
        editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
        self.SWOFF_DREFS_TABLE.setCellWidget(index,0, editWidget)

        item = QtWidgets.QTableWidgetItem('0')
        self.SWOFF_DREFS_TABLE.setItem(index,1, item)
        item = QtWidgets.QTableWidgetItem('0.0')
        self.SWOFF_DREFS_TABLE.setItem(index,2, item)

        check_state = QtCore.Qt.Unchecked
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(check_state)
        self.SWOFF_DREFS_TABLE.setItem(index,3, item)

        self.SWOFF_DREFS_TABLE.resizeColumnsToContents()
        self.SWOFF_DREFS_TABLE.resizeRowsToContents()
        self.SWOFF_DREFS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    def rmSwitchOffDataref(self):
        row = self.SWOFF_DREFS_TABLE.currentRow()
        self.SWOFF_DREFS_TABLE.removeRow(row)
        self.updateXMLdata()
        self.actionSave.setEnabled(True)

    ##
    #
    def editXPCommand(self):
        callingQwidgetButton = self.sender()
        parentitem = callingQwidgetButton.parent()
        text = parentitem.lineEdit.text()

        self.pickXPCommandDialog.commandLineEdit.setText(text)

        returnCode = self.pickXPCommandDialog.exec()

        if returnCode == 1: # command selected
            parentitem.lineEdit.setText(self.pickXPCommandDialog.commandLineEdit.text())
            self.updateXMLdata()
            self.actionSave.setEnabled(True)

    ##
    #
    def editXPDataref(self):
        callingQwidgetButton = self.sender()

        parentitem = callingQwidgetButton.parent()
        parenttable = parentitem.parentTable
        logging.debug("parent table: "+str(parenttable))
        index = parenttable.indexAt(parentitem.pos())
        row = index.row()
        logging.debug("edit XP dataref row: "+str(row))
        text = parentitem.lineEdit.text()

        self.pickXPDatarefDialog.datarefLineEdit.setText(text)

        returnCode = self.pickXPDatarefDialog.exec()

        if returnCode == 1: # command selected
            dataref = self.pickXPDatarefDialog.datarefLineEdit.text()
            parentitem.lineEdit.setText(dataref)

            # default index to 0
            item = QtWidgets.QTableWidgetItem('0')
            parenttable.setItem(row, 1, item)

            # default Set to value to 0.0
            item = QtWidgets.QTableWidgetItem('0.0')
            parenttable.setItem(row, 2, item)


            # retrieve dref data
            drefList = XPrefData.getXPDatarefList(None, dataref)
            if len(drefList) > 0: # we have found the dataref
                item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
                parenttable.setItem(row, 4, item)

                item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
                parenttable.setItem(row, 5, item)

            parenttable.resizeColumnsToContents()
            parenttable.setColumnWidth(0,self.DREFCMD_COLSIZE)

            self.updateXMLdata()
            self.actionSave.setEnabled(True)
            '''
