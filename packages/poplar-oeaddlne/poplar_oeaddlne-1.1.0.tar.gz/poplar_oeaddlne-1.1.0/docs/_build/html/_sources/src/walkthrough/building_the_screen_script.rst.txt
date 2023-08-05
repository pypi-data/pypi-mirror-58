======================================
Building the Screen Script
======================================

A screen script it is.  It will attach to the ``OE1100`` Order Entry
screen. On insert of a new detail line, it needs to:

1. Check if the operation was successful.
2. Check if the item matches "A1-103/0".
3. Generate a new record in the view.
4. Populate the record with the Item "A1-105/0" Qty 1.
5. Save the record.

Import accpac and Scaffold
--------------------------

All scripts start the same, import all members of ``accpac.py``:

.. code-block:: python

    from accpac import *

.. note:: 

    Importing ``*`` is generally not a good idea, you don't know what is being
    pulled into the namespace.  You can import only the things you need, plus
    some extras, with a little trial and error.

Because this is a screen script, we must create a new instance of the
``accpac.UI`` class, initialize its parent, and tell it to ``.show()`` itself.
To get a custom UI or change going, create a subclass.

.. code-block:: python

    from accpac import *

    class OeAddLineUI(UI):
        """A UI customization that monitors the order details for a trigger 
        item being inserted and adds a new line."""

        def __init__(self):
            super().__init__()
            self.show()

    def main(*args, **kwargs):
        ui = OeAddLineUI()

When working with screens Extender exposes ``accpac.UIDatasource`` objects. 
These act very similar to views. They allow access to the data sources 
underlying the current screen.  Data sources are always composed with one 
another, making coordinated access easy.

Datasources are opened using their unique ``Module Name``. Module names
can be found using the RotoID for the program (O/E Order Entry in our case -
``OE1100``) and looking up the details in ``accpacInfo``.

A little digging reveals that the datasource module id for Order Details is
``adsOEORDD``.  Open a datasource using ``UI.openDataSource(module_id)``.

.. code-block:: python

    from accpac import *

    class OeAddLineUI(UI):
        """A UI customization that monitors the order details for a trigger 
        item being inserted and adds a new line."""

        def __init__(self):
            super().__init__()

            # Open the data source 
            self.adsOEORDD = self.openDataSource("adsOEORDD")
            self.show()

    def main(*args, **kwargs):
        ui = OeAddLineUI()

Now we need to decide which events to listen to, do we need to check the record
before or after insert?  Before the operation occurs we can't know whether it 
was successful and it may fail.  If we were to act before a successful 
operation we may create new lines when the triggering line failed.  

``onAfter`` seems the correct choice.  Assign a call back function to the 
``onAfterInsert`` attribute of the ``adsOEORDD`` datasource.

.. code-block:: python

    from accpac import *

    class OeAddLineUI(UI):
        """A UI customization that monitors the order details for a trigger 
        item being inserted and adds a new line."""

        def __init__(self):
            super().__init__()

            # Open the data source 
            self.adsOEORDD = self.openDataSource("adsOEORDD")

            # Assign the onAfter callback to the *function* 
            self.adsOEORDD.onAfterInsert = self.adsOEORDDonAfterInsert

            self.show()

        def adsOEORDDonAfterInsert(self, result):
            """After updating, if the item is "A1-103/0", insert a new line."""
            # Check if the item matches

            # Generate a new record in the view

            # Populate the record

            # Save the record
            pass

    def main(*args, **kwargs):
        ui = OeAddLineUI()

Implement the onAfter call
--------------------------

The ``accpac.UIDatasource.onAfterInsert`` callback does not receive arguments
and is only triggered on a successful insert.  Now we need to see if the item
matches.  Use the ``.get(field)`` method on the datasource to get the current
value.  Field names can be found by looking them up using the Extender View
Info Inquiry or using the Sage ``accpacViewInfo`` utility.

.. code-block:: python

    from accpac import *

    class OeAddLineUI(UI):
        """A UI customization that monitors the order details for a trigger 
        item being inserted and adds a new line."""

        def __init__(self):
            super().__init__()

            # Open the data source 
            self.adsOEORDD = self.openDataSource("adsOEORDD")

            # Assign the onAfter callback to the *function* 
            self.adsOEORDD.onAfterInsert = self.adsOEORDDonAfterInsert

            self.show()

        def adsOEORDDonAfterInsert(self, result):
            """After updating, if the item is "A1-103/0", insert a new line."""

            # Check if the item matches
            if me.get("ITEM") == "A1-103/0":

            # Generate a new record in the view

            # Populate the record

            # Save the record
            pass

    def main(*args, **kwargs):
        ui = OeAddLineUI()

Generating a new line is generally accomplished by running two operations on
the datasource.  The first, ``.recordClear()`` resets the state of the
datasource.  The second, ``.recordGenerate()``, creates a new record in the
datasource. Both return 0 when successful.

What should happen if these operations fail?  There is always a silent option,
but then the user may be confused as to why the line doesn't isn't created when
they expect it to. 

Extender provides a number of ways to notify.  The first is using the 
``showMessage(str)``, ``showWarning(str)``, ``showError(str)`` method.  These 
put messages on the error stack for Sage to display. They may not be displayed 
immediately, which can be helpful for situtations where errors may occur in 
bulk (such as during an import).  They also provide levels and a familiar
interace.

The second is to use ``showMessageBox(str)`` which will pop up a dialog 
immediately. This is generally a better option for things the user needs to
know now and for any debugging you need.  Show a message box to the user on
failure.

.. code-block:: python

    from accpac import *

    class OeAddLineUI(UI):
        """A UI customization that monitors the order details for a trigger 
        item being inserted and adds a new line."""

        def __init__(self):
            super().__init__()

            # Open the data source 
            self.adsOEORDD = self.openDataSource("adsOEORDD")

            # Assign the onAfter callback to the *function* 
            self.adsOEORDD.onAfterInsert = self.adsOEORDDonAfterInsert

            self.show()

        def adsOEORDDonAfterInsert(self, result):
            """After updating, if the item is "A1-103/0", insert a new line."""

            # Check if the item matches
            if me.get("ITEM") == "A1-103/0":

                # Generate a new record in the view
                rc = me.recordClear()
                rg = me.recordGenerate()

                if rc != 0 or rg != 0:
                    showMessageBox("Failed to generate new line.")
                return

                # Populate the record

                # Save the record
            pass

    def main(*args, **kwargs):
        ui = OeAddLineUI()

Now we just need to populate the record and save it. Set fields in the
current record by using ``.put(field, value)``.  Once populated,
use ``.insert()`` to add write it to the database.  These operations
also return 0 on success.

.. code-block:: python

    from accpac import *

    class OeAddLineUI(UI):
        """A UI customization that monitors the order details for a trigger 
        item being inserted and adds a new line."""

        def __init__(self):
            super().__init__()

            # Open the data source 
            self.adsOEORDD = self.openDataSource("adsOEORDD")

            # Assign the onAfter callback to the *function* 
            self.adsOEORDD.onAfterInsert = self.adsOEORDDonAfterInsert

            self.show()

        def adsOEORDDonAfterInsert(self, result):
            """After updating, if the item is "A1-103/0", insert a new line."""

            # Check if the item matches
            if me.get("ITEM") == "A1-103/0":

                # Generate a new record in the view
                rc = me.recordClear()
                rg = me.recordGenerate()

                if rc != 0 or rg != 0:
                    showMessageBox("Failed to generate new line.")
                return

                # Populate the record
                pi = me.put("ITEM", "A1-105/0")
                pq = me.put("QTYORDERED", 1)

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

And there you have it.  A view script that does exactly what we need.  
Are there any improvements to be had?  

Add Parameters
--------------

What if the customer wants to change the items?  Instead of "A1-103/0" 
triggering they may want "A1-900/G" to be the trigger.  What if they wanted
to add a quantity of 5 instead of 1?  At present, they'd need to change the 
script because the items and quantity are hard coded.

View scripts support up to 4 user provided parameters of up to 250 characters, 
so 1000 characters of arguments to play with. They are exposed by ``accpac`` as
``Parameter1``, ``Parameter2``, ``Parameter3``, ``Parameter4``.

Unfortunately, screens scripts do not allow user provided parameters.  We will
see another solution later, when we add custom tables.

Testing
-------

Screen scripts must follow a specific naming convention and have a particular
structure.  The Roto ID of the screen being customized must be present in
one of the first two ``.`` delineated parts of the filename:

- ``OE1100.COMPANY.script_name.py``: good
- ``COMPANY.OE1100.script_name.py``: good
- ``COMPANY-script_name-OE1100.py``: bad

The file must also start with a single line comment that includes the
Roto ID::

    # OE1100
    # ... The rest of my script.

With the file named correctly and the comment in place, time for testing.  Fire
up your favourite database and install the script in the Extender -> Setup ->
Scripts screen.

There is no need to configure screen scripts, if they are installed whey will
be loaded when the screen is loaded.  It is best to restart the Sage desktop
after installing but before testing your customization.


