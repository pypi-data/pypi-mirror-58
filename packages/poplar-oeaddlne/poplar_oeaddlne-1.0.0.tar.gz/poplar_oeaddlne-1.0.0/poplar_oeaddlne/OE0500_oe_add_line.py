"""
Insert a new OE line following the insert of a line with a particular item.

This script does not work (by design) - why not?

Part of an introductory training to Extender.  Learn more at
https://poplar_addoelne.rtfd.io.

Parameters:

- Parameter1: Item number to trigger insert after.
- Parameter2: Item number to insert
- Parameter3: Item

| author: Chris Binckly

| email: chris@2665093.ca

| copyright: 2665093 Ontario Inc., 2019

This file is provided under a Creative Commons 4 Sharealike license.
See https://creativecommons.org/licenses/by-sa/4.0/ for details.
"""
try:
    from accpac import *
except ImportError:
    # Outside the Extender env this fails, allow it to pass for sphinx/unittest
    pass

def onOpen():
    """onOpen of the script, take no action."""
    return Continue

def onAfterInsert(result):
    """After a line with item ``Parameter1`` is entered, insert line with item
    ``Parameter2``.

    Triggered after an insert of an OE Detail line. If the insert was
    successful and the item in the line is the same as that provided in
    ``Parameter1``, a new line is added with:

    - ``LINETYPE``: 1 - standard item line
    - ``ITEM``: ``Parameter2``
    - ``QTYORDERED``: ``Parameter3``
    """

    #showMessageBox("Inserted new line {}".format(me.get("ITEM")))

    if result == 0 and me.get("ITEM") == Parameter1:

        # Clear the view and generate a new record.
        rc = oeordd.recordClear()
        rg = me.recordGenerate()
        if sum([rc, rg, ]) > 0:
            showMessageBox("Unable to generate new record.")
            return Continue

        # Put the values from the paramters
        pl = me.put("LINETYPE", 1)
        pi = me.put("ITEM", Parameter2)
        pq = me.put("QTYORDERED", Parameter3)
        if sum([pi, pq, pl, ]) > 0:
            showMessageBox("Unable to generate new record.")
            return Continue

        # Insert the new line
        i = me.insert()
        if i != 0:
            showMessageBox("Unable to insert record.")

    return Continue
