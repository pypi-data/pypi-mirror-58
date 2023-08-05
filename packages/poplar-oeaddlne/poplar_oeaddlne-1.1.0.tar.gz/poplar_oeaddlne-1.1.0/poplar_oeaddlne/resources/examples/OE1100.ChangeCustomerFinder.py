# OE1100
# Changes the customer number finder to ic items.
# Calls up normal customer finder on cancel of finder to IC items.
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
		self.getHostControlByCaption("Customer No.").setOnClick(self.onCustomerNoClick)
		self.dsH = self.openDataSource("adsOEORDH")
		self.show()

	def onCustomerNoClick(self, btnType):
		if btnType == 4:
			finder = Finder()
			finder.viewID = "IC0310"
			finder.returnFields = "1"
			finder.onOK = self.customer_finder_ok
			finder.onCancel = self.customer_finder_cancel
			finder.show(self)

	def customer_finder_ok(self, e):
		self.dsH.dsput("CUSTOMER", e)
		self.setButtonClickResultToCancelWithTabAway()

	def customer_finder_cancel(self):
		# If you don't want the normal finder to appear then you have two options:
		#    1) Don't set finder.onCancel
		#    2) Uncomment the next line
		#self.setButtonClickResultToCancel()
		self.setButtonClickResultToOK() # This causes the normal finder to appear
