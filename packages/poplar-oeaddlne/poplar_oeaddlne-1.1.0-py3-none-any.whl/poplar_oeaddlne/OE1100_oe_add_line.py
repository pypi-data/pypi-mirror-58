# OE1100
"""
Insert a new OE line following the insert of a line with a particular item.

This script does not work (by design) - why not?

Part of an introductory training to Extender.  Learn more at
https://poplar_addoelne.rtfd.io.

| author: Chris Binckly

| email: chris@2665093.ca

| copyright: 2665093 Ontario Inc., 2019

This file is provided under a Creative Commons 4 Sharealike license.
See https://creativecommons.org/licenses/by-sa/4.0/ for details.
"""
try:
    from accpac import *
except ImportError:
    UI = object
    # Outside the Extender env this fails, allow it to pass for sphinx/unittest
    pass

ITEM = "A1-103/0"
"""The item number that triggers the new line."""

NEW_ITEM_NUM = "A1-105/0"
"""The item number to insert."""

NEW_ITEM_QTY = 10
"""The item quantity to insert."""

NEW_ITEM_LINETYPE = 1 # Regular Item
"""The item line type to insert."""

def main(args):
    """Executed by VI when the screen is loaded. Create our UI."""
    AddOELneUI()

class AddOeLneUI(UI):
    """A UI that monitors the order details and inserts a new line.

    This UI class makes no changes to the OE1100 screen, it simply
    monitors and writes to the Data Sources connected to it.
    """
    def __init__(self):
        super().__init__()

        # Open the order details data source
        self.adsOEORDD = self.openDataSource("adsOEORDD")

        # Assign the AfterInsert callback function
        self.adsOEORDD.onAfterInsert = self.adsOEORDDonAfterInsert

        # The UI must be shown, even though it doesn't change visuals.
        self.show()

    def adsOEORDDonAfterInsert(self):
        """If the item inserted was ``ITEM``, add a new line.

        :raises: None
        :rtype: None
        """
        # Get the item number that was inserted.
        item = self.adsOEORDD.get("ITEM")

        if item.strip() == ITEM:
            # showMessageBox("Item {} inserted".format(ITEM))

            # Generate a new record.
            rg = self.adsOEORDD.recordGenerate()
            if rg != 0:
                showMessageBox("Unable to generate new record.")
                return

            # Put the values for ``NEW_ITEM``
            pi = self.adsOEORDD.put("ITEM", NEW_ITEM_NUM)
            pq = self.adsOEORDD.put("QTYORDERED", NEW_ITEM_QTY)
            pl = self.adsOEORDD.put("LINETYPE", 1)
            if sum([pi, pq, pl, ]) > 0:
                showMessageBox("Unable to generate new record.")
                return

            # Insert it
            i = self.adsOEORDD.insert()
            if i != 0:
                showMessageBox("Unable to insert record.")

