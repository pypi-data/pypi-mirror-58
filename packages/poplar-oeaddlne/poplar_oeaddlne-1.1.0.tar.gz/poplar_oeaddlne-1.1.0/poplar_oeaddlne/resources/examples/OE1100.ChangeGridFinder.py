# OE1100
# Changes the item number finder.
# 
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
		self.grid = self.getHostControlByCaption("avlOEORDDdetail1")
		self.grid.setOnFinder(self.onGridFinder)
		self.show()

	def onGridFinder(self, fieldName, caption):
		finder = Finder()
		finder.viewID = "IC0310"
		finder.returnFields = "1"
		finder.onOK = self.finder_ok
		finder.onCancel = self.finder_cancel
		finder.show(self)

	def finder_ok(self, e):
		self.grid.endEdit(e)

	def finder_cancel(self):
		self.grid.preventFinder()
