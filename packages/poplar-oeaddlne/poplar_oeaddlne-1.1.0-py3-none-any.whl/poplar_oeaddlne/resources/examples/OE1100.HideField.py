# OE1100
# Hides to tracking no. field
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
		self.getHostControlByCaption("Tracking No.").hide()
		self.show()
