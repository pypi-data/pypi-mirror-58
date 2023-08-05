============================================
Custom Tables for Item Mappings
============================================

The screen script solution does what we need but is limited in that the
item mappings are hard-coded.  The user cannot add new mappings themselves
and if there are many then keeping them in the source becomes unwieldy.

Enter Extender's Custom Tables.  They make it easy to store, retrieve, and
update tables specific to your customization in the database.

Assume for now that each Item will only ever map to one other.  We can define
a database table, ``OEADDLNE.VIITMMAP``, to allow the user to manage the 
mappings.

Designing the Table Schema
--------------------------

Before creating a table it needs a schema.  The correct fields and keys (which
are also indexes) need to be identified.  Every item only maps to one other,
we can use the trigger item as a key.

When thinking about keys, think about how you access the data.  If you always
use two fields together to retrieve from a table, be sure to add a compound key
on those fields.

We need the same fields as we had view script parameters, so the following
should do::

    Table name: VIITMMAP
    Fields:
        - TRIGITEM (str): item that triggers the new line
        - NEWITEM (str): the item to insert
        - QTYORDERED (bcd): the quantity ordered
    Keys:
        - (TRIGITEM, )


Creating the Table Schema
-------------------------

The table schema will be embedded in the module file.  You have two options
for creating it: interactively with the Custom Tables tool or writing it
by hand in the modules file.

Using Custom Tables
*******************

This is the best way to start.  Once you get the hang of it you can craft them
by hand. 

To use the Custom Tables tool, start by creating a module:

1. Navigate to Extender -> Setup -> Modules
2. Insert a new row using the module name (``OEADLNE``)

Define the custom table:

1. Navigate to Extender -> Setup -> Custom Tables
2. Set the table name to ``OEADDLNE.VIITMMAP``
3. Define the fields. Use ``accpacViewInfo`` or the extender enquiries to find
   the correct field names, finder information, and description lookups.
4. Add the key in the ``Keys`` tab.
5. Save the table.

Now that the table is defined you can export the module from the Modules screen
and the table definition will be included.

Crafting by Hand
****************

After a while you'll be able to write table definitions by hand.  To start, 
this is what is automatically generated on module export::

    [MODULE]
    id=OEADDLNE
    name=OEADDLNE
    desc=Add an OE Order Line after a particular item is added.
    company=2665093 Ontario Inc
    version=0.1.0
    website=https://2665093.ca

    [TABLE]
    name=OEADDLNE.VIITMMAP
    dbname=VIITMMAP

    [FIELD1]
    field=TRIGITEM
    datatype=1
    size=24
    mask=%24C
    desc=Trigger item number
    ftable=IC0310
    ffield=ITEMNO
    lookup=FMTITEMNO

    [FIELD2]
    field=NEWITEM
    datatype=1
    size=24
    mask=%24C
    desc=Item number to insert
    ftable=IC0310
    ffield=ITEMNO
    lookup=FMTITEMNO

    [FIELD3]
    field=QTYORDERED
    datatype=6
    size=10
    decimals=5
    desc=Quantity

    [KEY1]
    KEYNAME=TRIGITEM
    FIELD1=TRIGITEM
    allowdup=0

Simply add the ``SCRIPT`` block and we have a full module.

Adding Entries to the Table
---------------------------

Adding entries is easy using the Extender -> Setup -> Custom Table Editor.
Simply open the editor, open the ``OEADDLNE.VIITMMAP`` table, and start adding.

For now, try to add the item we know about, A1-103/0 -> A1-105/0@1.

Adding the Lookup to the Script
-------------------------------

Now we just need to replace out hard coded values with a lookup from our custom
table.  Custom tables are accessed through the view layer.  Instead of opening 
them based on the View ID (i.e. ``VI0107``), always access them by module
qualified table name. There is no guarantee that your table will always have 
the same roto, so don't use it.

Because ``TRIGITEM`` is our key field, we will use it to look up the mapping.
The lookup will go something like this::

    view = openView("OEADDLNE.VIITMMAP")
    view.recordClear()
    view.put("TRIGITEM", itemno)
    r = view.read()

Extender functions return 0 on success, so if ``r`` is 0 then there is a 
mapping for ``itemno`` and the view has read it in.  Any other return 
indicates that ``itemno`` is not a trigger item and no action is required.

.. code-block:: python

    from accpac import *

    class OeAddLineUI(UI):
        """A UI customization that monitors the order details for a trigger 
        item being inserted and adds a new line."""

        def __init__(self):
            super().__init__()

            # Open the data source 
            self.adsOEORDD = self.openDataSource("adsOEORDD")

            # Open the custom table.
            self.viitmmap = openView("OEADDLNE.VIITMMAP")

            # Assign the onAfter callback to the *function* 
            self.adsOEORDD.onAfterInsert = self.adsOEORDDonAfterInsert

            self.show()

        def get_trigger(self, itemno):
            """Get the trigger information for this item number from the table.

            :param itemno: item number to loopkup trigger information for
            :type itemno: str
            :rtype: list
            :returns:
                - If the item number is not in the map table: [] 
                - if the item number is in the table: [newitem, qtyordered]
            """

            self.viitmmap.recordClear()
            self.viitmmap.put("TRIGITEM", itemno)
            self.viitmmap.read()

            if r != 0:
                return []

            return [self.viitmmap.get("NEWITEM"), 
                    self.viitmmap.get("QTYORDERED"), ]
            


        def adsOEORDDonAfterInsert(self, result):
            """After updating, if the item is "A1-103/0", insert a new line."""

            # Check if the item matches an item in the custom table map :
            # trigger will be [newitem, qty] if it does, [] (False) if it
            # doesn't.
            trigger = self.get_trigger(me.get("ITEM"))
            if trigger:

                # Generate a new record in the view
                rc = me.recordClear()
                rg = me.recordGenerate()

                if rc != 0 or rg != 0:
                    showMessageBox("Failed to generate new line.")
                return

                # Populate the record
                pi = me.put("ITEM", trigger[0])
                pq = me.put("QTYORDERED", trigger[1])

                if pi != 0 or pq != 0:
                    showMessageBox("Failed to put values in new line.")
                    return

                # Save the record
                sv = me.insert()

                if sv != 0:
                    showMessageBox("Failed to save new line.")

            return None

    def main(*args, **kwargs):
        ui = OeAddLineUI()

Done.  The custom table is now intergated with the script.  The user can 
add and manage as many mappings as they'd like with the custom table
editor.

That's all for now, just a few things to close out...
