from pySTGraphics import pyXPPanel
from pySTGraphics import OpenGL3lib
from pySTGraphics import graphicsGL3 as graphics
from pySTGraphics import conversionFunctions
#from pySTGraphics import fonts
import os
import pyxpudpserver as XPUDP


working_dir = os.path.dirname(os.path.abspath(__file__))
std6_orig = [170,670]
ZOOM_STD6 =  0.97
std6_xgrid = 300
std6_ygrid = 300
ASI_pos = [std6_orig[0],std6_orig[1]]
ALT_pos = [std6_orig[0]+std6_xgrid*2,std6_orig[1]]
standardInstrumentSize = (300,300)

UDPconfigFile = os.path.join(working_dir,'config/UDPSettings.xml')

class C172_AirspeedIndicator(graphics.Container):
	
	def __init__(self,position, size, batchImageRenderer, texture, zoom = 1.0, name = "C172_AirspeedIndicator"):
		graphics.Container.__init__(self,batchImageRenderer, position, (size[0]*zoom, size[1]*zoom), name)
		
		self.testMode = False
		self.batchImageRenderer = batchImageRenderer
		self.layer = 0
		
		#------------------------------------------------------------------------------------------
		#	Airspeed Indicator
		#------------------------------------------------------------------------------------------
		self.airspeedBackground = 	graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [300,300],	[0				,2048-300*2		],"background")
		self.airspeedNeedle = 		graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [40,300],	[300*2+ 130		,2048-300*6		],"airspeedNeedle")
		self.airspeedNeedle.resize([40*zoom,300*zoom])
		self.airspeedBezel = 		graphics.ImagePanel(texture, self.batchImageRenderer,self.layer, [0,0], [310,310],	[300*4	,2048-300*6-10	],"airspeedBezel")
		self.airspeedBezel.resize([310*zoom,310*zoom])

		self.airspeedNeedle.enableRotation((3,0), [ [0,0],
			[40,30],
			[50,50],
			[60,70],
			[70,90],
			[80,115],
			[90,140.5],
			[95,151],
			[100,162.5],
			[105,174],
			[110,185],
			[115,196],
			[120,207.5],
			[130,222.5],
			[140,237.5],
			[160,267.5],
			[200,317.5]])
			
		self.addItem(self.airspeedBackground)
		self.addItem(self.airspeedNeedle,[0,0],False)
		self.addItem(self.airspeedBezel,[0,0],False)
		
	def draw(self):
		
		super(C172_AirspeedIndicator,self).draw()

class C172_Altimeter(graphics.Container):
	
	def __init__(self,position, size, batchImageRenderer, texture, zoom = 1.0, name = "C172_DirectionalGyro"):
		graphics.Container.__init__(self,batchImageRenderer, position, (size[0]*zoom, size[1]*zoom), name)
		
		self.testMode = False
		self.batchImageRenderer = batchImageRenderer
		self.layer = 0
		
		#------------------------------------------------------------------------------------------
		#	Altimeter
		#------------------------------------------------------------------------------------------
		self.altimeterBlackBackground = 	graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [300,300],	[300		,2048-300*2		],"altimeterBlackBackground")
		self.altimeterHgWheel = 			graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [300,300],	[300*2		,2048-300*2		],"altimeterHgWheel")
		self.altimeterMbWheel = 			graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [300,300],	[300*2		,2048-300*3		],"altimeterMbWheel")
		self.altimeterBackground = 			graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [300,300],	[300		,2048-300*3		],"altimeterBackground")
		self.altimeter10kNeedle =			graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [300,300],	[300*3		,2048-300*3		],"altimeter10kNeedle")
		self.altimeter1kNeedle = 			graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [40,300],	[130		,2048-300*6		],"altimeter1kNeedle")
		self.altimeter1kNeedle.resize([40*zoom,300*zoom])
		self.altimeter100sNeedle =			graphics.ImagePanel(texture, self.batchImageRenderer, self.layer, [0,0], [40,300],	[430		,2048-300*6		],"altimeter100sNeedle")
		self.altimeter100sNeedle.resize([40*zoom,300*zoom])
		
		self.altimeterBezel = 				graphics.ImagePanel(texture, self.batchImageRenderer,self.layer, [0,0], [310,310],	[300*4	,2048-300*6-10	],"altimeterBezel")
		self.altimeterBezel.resize([310*zoom,310*zoom])

		self.altimeterMbWheel.enableRotation ((7,0),[ [945,165.5],[1000,0.5],[1050,-149.5]],conversionFunctions.convertINtomb)
		self.altimeterHgWheel.enableRotation ((7,0),[ [28,154],[29.5,-0.5],[31.1,-165.1]])
		self.altimeter100sNeedle.enableRotation ("sim/cockpit2/gauges/indicators/altitude_ft_pilot",[ [0,0],[1.0,360]], conversionFunctions.return100s)
		self.altimeter1kNeedle.enableRotation ("sim/cockpit2/gauges/indicators/altitude_ft_pilot",[ [0,0],[1.0,360]], conversionFunctions.return1000s)
		self.altimeter10kNeedle.enableRotation ("sim/cockpit2/gauges/indicators/altitude_ft_pilot",[ [0,0],[1.0,360]], conversionFunctions.return10000s)

		self.addItem(self.altimeterBlackBackground)
		self.addItem(self.altimeterHgWheel)
		self.addItem(self.altimeterMbWheel)
		self.addItem(self.altimeterBackground)
		self.addItem(self.altimeter10kNeedle)
		self.addItem(self.altimeter1kNeedle,[0,0],False)
		self.addItem(self.altimeter100sNeedle,[0,0],False)
		self.addItem(self.altimeterBezel,[0,0],False)

		
	def draw(self):
		
		super(C172_Altimeter,self).draw()


def drawInstruments():
    airspeedIndicator.draw()
    altimeter.draw()
    altimeterConfigFile.draw()

XPUDP.pyXPUDPServer.initialiseUDPXMLConfig(UDPconfigFile)
XPUDP.pyXPUDPServer.start()

panel = pyXPPanel.pyXPPanel("./config/configGraphics.ini", 5, XPUDP.pyXPUDPServer)
panel.setDrawCallback(drawInstruments)

standard6Texture = 	os.path.join(working_dir, 'instruments/textures/c172_text_standard6.png')

airspeedIndicator = C172_AirspeedIndicator	(ASI_pos,			standardInstrumentSize, panel.batchImageRenderer, 	standard6Texture, ZOOM_STD6,"airspeedIndicator")	#calibrated
altimeter = 		C172_Altimeter	(ALT_pos,			standardInstrumentSize, panel.batchImageRenderer, 	standard6Texture, ZOOM_STD6,"")	#calibrated

altimeterConfigFile = graphics.Container(panel.batchImageRenderer)
altimeterConfigFile.configureFromFile(os.path.join(working_dir, 'instruments/C172_Altimeter.xml'))

print("alti name" + str(altimeterConfigFile.getName()))

print("alti size" + str(altimeterConfigFile.getSize()))
print("alti position" + str(altimeterConfigFile.getPosition()))


panel.run()


XPUDP.pyXPUDPServer.quit()



