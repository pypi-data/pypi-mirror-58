# OE1100
# This adds two new fields and two tabs to the O/E order entry screen.
###################################################################################################################################################
# Copyright 2018 Orchid Systems 
# -----------------------------
# Permitted for use with Orchid Systems Modules only.
# The code is supplied on an "as is" basis for training and demonstration purposes only and is not supported by Orchid Systems.
# If this code is deployed in a live production environment it is the responsibility of the End User to ensure 
# that it is operating as required.
###################################################################################################################################################

from accpac import *

def main(args):
	MyUI()

class MyUI(UI):
	def __init__(self):
		UI.__init__(self)
		self.createScreen()

	def createScreen(self):
		self.getControlInfo("form|fecOEORDH_ShipTrackNo|stbOrderEntry", self.onControlInfo)
		self.getHostControl("stbOrderEntry").setOnClick(self.onTabClick)
		self.getHostControl("stbOrderEntry").addTab("Mandatory Field", self.onTab1Added)
		self.getHostControl("stbOrderEntry").addTab("Shipping Details", self.onTab2Added)
		self.show()

	def onTab1Added(self, tabIndex):
		self.tab1 = tabIndex
		pass
		

	def onTab2Added(self, tabIndex):
		self.tab2 = tabIndex
		pass

	def onControlInfo(self, info):
		f = info.find("form")

		b = info.findByCaption("Tracking No.")
		tab = info.find("stbOrderEntry")

		self.dsH = self.openDataSource("adsOEORDH")
		self.dsHO = self.openDataSource("dsOEORDHO")

		f = self.addUIField("ID")
		f.controlType = "DATETIME"
		f.fieldType = "DATE"
		f.setValue("20180524")
		f.caption = "Date Control"
		f.left = tab.left + b.left + b.width + 150
		f.top = tab.top + b.top
		self.myField = f

		f = self.addUIField("ID2")
		f.controlType = "DATETIME"
		f.fieldType = "DATE"
		f.setValue("20180524")
		f.caption = "Shipping Date"
		f.left = tab.left + 150
		f.top = tab.top + 450
		f.hide()
		self.myField2 = f

		f = self.addUIField("OptApproved")
		f.controlType = "EDIT"
		f.fieldType = "STRING"
		f.caption = "Approved"
		f.left = tab.left + 150
		f.top = tab.top + 450
		f.size = 3
		f.onChange = self.onChange_myOpField
		f.hide()
		self.myOptField = f
		
		self.show()

	def onTabClick(self, tab):
		if tab == 0:
			self.myField.show()
		else:
			self.myField.hide()
			
		if tab == self.tab1:
			self.myOptField.show()
			self.fillOptFieldValue("APPROVED")
		else:
			self.myOptField.hide()
			
		if tab == self.tab2:
			self.myField2.show()
		else:
			self.myField2.hide()

		return None
		
	def onChange_myOpField(self, oldValue, newValue):
		
		self.dsHO.put("OPTFIELD", "APPROVED")
		if self.dsHO.read() == 0:
			self.dsHO.put("VALUE", newValue)
			self.dsHO.update()
			self.dsHO.refreshFields()
			
	def fillOptFieldValue(self, optFld):

		self.dsHO.put("OPTFIELD", "APPROVED")
		if self.dsHO.read() == 0:
			optVal = self.dsHO.get("VALUE")
			self.myOptField.setValue(optVal)
	
	