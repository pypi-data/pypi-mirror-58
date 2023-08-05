======================================
Building the View Script
======================================

A view script it is.  It will attach to the ``OE0500`` Order Headers 
detail view. On insert it needs to:

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

Now we need to decide which events to listen to, do we need to check the record
before or after insert?  Before the operation occurs we can't know whether it 
was successful and it may fail.  If we were to act before a successful 
operation we may create new lines when the triggering line failed.  

``onAfter`` seems the correct choice.  Add the appropriate method with the
correct signature.  The :py:mod:`poplar_oeaddlne.resources.all_view_calls` is a
good place to start.

.. code-block:: python

    from accpac import *

    def onAfterInsert(result):
        """After updating, if the item is "A1-103/0", insert a new line."""

        # Check if the operation was successful

        # Check if the item matches

        # Generate a new record in the view

        # Populate the record

        # Save the record
        pass


Implement the onAfter call
--------------------------

The docs for 
:py:meth:`poplar_oeaddlne.resources.all_view_calls.onAfterInsert` tell
us that the ``result`` argument contains 0 if the insert succeeded and that the
function doesn't need to return.

Once we have checked the result, we need to see if the item matches.  Use the
special view object ``me`` exposed by ``accpac`` to access the current record
in the view and use ``me.get(field)`` to retrive the item number inserted.

Field names can be found by looking them up using the Extender View Info
Inquiry or using the Sage ``accpacViewInfo`` utility.

.. code-block:: python

    from accpac import *

    def onAfterInsert(result):
        """After updating, if the item is "A1-103/0", insert a new line."""

        # Check if the operation was successful
        if result != 0:
            return

        # Check if the item matches
        if me.get("ITEM") == "A1-103/0":

            # Generate a new record in the view

            # Populate the record

            # Save the record

Generating a new line is generally accomplished by running two operations on
the view.  The first, ``.recordClear()`` resets the state of the view.  The
second, ``.recordGenerate()``, creates a new record in the view. Both return
0 when successful.

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

    def onAfterInsert(result):
        """After updating, if the item is "A1-103/0", insert a new line."""

        # Check if the operation was successful
        if result != 0:
            return

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

Now we just need to populate the record and save it. Set fields in the
current record by using ``.put(field, value)``.  Once populated,
use ``.insert()`` to add write it to the database.  These operations
also return 0 on success.

.. code-block:: python

    from accpac import *

    def onAfterInsert(result):
        """After updating, if the item is "A1-103/0", insert a new line."""

        # Check if the operation was successful
        if result != 0:
            return

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

Let's change the script to accept parameters from the user.

.. code-block:: python

    """OE0500_oe_add_line.py

    Parameters
    ----------

        - Parameter1: Item number to trigger new line
        - Parameter2: Item number to set in new line
        - Parameter3: Item quantity to set.
    """
    from accpac import *
    # from accpac import (me, 
    #                     Parameter1, Parameter2, Parameter3, 
    #                     showMessageBox, )

    def onAfterInsert(result):
        """After updating, if the item is Parameter1, insert a new line."""

        # Check if the operation was successful
        if result != 0:
            return

        # Check if the item matches
        if me.get("ITEM") == Parameter1:

            # Generate a new record in the view
            rc = me.recordClear()
            rg = me.recordGenerate()

            if rc != 0 or rg != 0:
                showMessageBox("Failed to generate new line.")
                return

            # Populate the record
            pi = me.put("ITEM", Parameter2)
            pq = me.put("QTYORDERED", Parameter3)

            if pi != 0 or pq != 0:
                showMessageBox("Failed to put values in new line.")
                return

            # Save the record
            sv = me.insert()

            if sv != 0:
                showMessageBox("Failed to save new line.")

        return None

Testing
-------

Time for testing.  Fire up your favourite database and install the script in 
the Extender -> Setup -> Scripts screen.

Configure it by attaching it to the ``OE0500`` view in the Extender -> Setup ->
View Events, Scripts and Workflow.



