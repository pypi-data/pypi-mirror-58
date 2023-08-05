# OE1100
# Adds a freight button. Pressing it adds a TF miscellaneous charge line.
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
		self.getControlInfoByCaption("form|Prepayment...", self.onControlInfo)
		self.show()

	def onControlInfo(self, info):
		f = info.find("form")

		b = info.findByCaption("Prepayment...")

		ctrl = self.addButton("btnFreight", "Add Freight")
		ctrl.height = b.height #345
		ctrl.left = b.left + b.width + 150 #5200
		ctrl.top = b.top - f.height #-315-250
		ctrl.width = 1340
		ctrl.disable()
		self.btnFreight = ctrl
		ctrl.onClick = self.btnFreight_Click

		self.dsH = self.openDataSource("adsOEORDH")
		self.dsD = self.openDataSource("adsOEORDD")
		self.dsH.onAfter = self.dsH_onAfter

		self.show()

	def dsH_onAfter(self, eventName, fieldName, value):
		if eventName == "FETCH" or eventName.startswith("GO") or eventName == "READ":
			self.btnFreight.enable()
		if eventName == "INIT":
			self.btnFreight.disable()
		if eventName == "PUT" and fieldName == "CUSTOMER":
			self.btnFreight.enable()

	def btnFreight_Click(self):
		self.dsD.recordGenerate()
		self.dsD.put("LINETYPE", 2)
		self.dsD.put("MISCCHARGE", "TF")
		self.dsD.insert()

		self.getHostControl("avlOEORDDdetail1").refreshData()
