"""
This script shows all the entry points that you can use when writing a script for a view.
It doesn't actually do anything useful.

Copyright 2015 Orchid Systems

Updated 2019 2665093 Ontario Inc.
"""
try:
    from accpac import *
except ImportError:
    pass

def onOpen():
    """Called when a view is opened.

    :rtype: int
    :returns: ``accpac.Continue`` to enable the script,
              0 to disable, anything else stops the view loading.
    """
    rvspyTrace("onOpen")
    return Continue

def onOpenReadOnly():
    """Called when a view is opened in readonly mode.

    :rtype: int
    :returns: ``accpac.Continue`` to enable the script,
              0 to disable, anything else stops the view loading.
    """
    rvspyTrace("onOpenReadOnly")
    return Continue

def onBeforeClose():
    """Called before a view is closed.

    :rtype: int
    :returns: ``accpac.Continue`` to allow the close,
              ``accpac.Abort`` to disallow it.
    """
    rvspyTrace("onBeforeClose")
    return Continue

def onAfterClose(result):
    """Called after a view is closed.

    :param result: result of the close operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterClose result=" + str(result))

def onBeforeCompose(event):
    """Called before a view is composed.

    :param event: compose event information.
    :type event: ``accpac.viewComposeArgs``
    :returns: must return ``accpac.Continue`` or the view will not load.
    :rtype: int

    Get the handles for composed views to make it easier to work with
    related data.

    A script attached to the Order Header ``OE0520`` view can access
    the composed Order Details ``OE0522`` view.  Get a handle on before
    compose, store it in the ``__main__`` (script) namespace, and use
    it in other calls.

    .. code-block:: python

        oeordd = None
        def onBeforeCompose(event):
            if len(event.views):
                oeordd = event.views[0]

        def onAfterPut(result):
            # If the put succeeded and a field = value, add a new order line
            if result == 0 and me.get("FIELD") == "VALUE":
                r = oeordd.recordClear()
                r = oeordd.recordGenerate()
                r = oeordd.put(...)
                ...
    """
    s = "Composed with " + str(len(event.views)) + " views"
    for view in event.views:
        if view is None:
            s = s + "\n  None"
        else:
            s = s + "\n  " + view.fieldByPosition(-1).desc
    showMessage(s)
    return Continue

def onAfterCompose(event):
    """Called after a view is composed.

    :param event: compose event information.
    :type event: ``accpac.viewComposeArgs``
    :returns: must return ``accpac.Continue`` or the view will not load.
    :rtype: int
    """
    if e.result != 0:
        showError("The compose failed")

def onBeforeVerify():
    """Called before a view is verified.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeVerify")
    return Continue

def onAfterVerify(result):
    """Called after a view is verified.

    :param result: result of the verify operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterVerify result=" + str(result))

def onBeforeDirty():
    """Called before a view is marked dirty.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeDirty")
    return Continue

def onAfterDirty(result):
    """Called after a view is marked dirty.

    :param result: result of the mark dirty operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterDirty result=" + str(result))

def onBeforeInit():
    """Called before a view is initialized.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeInit")
    return Continue

def onAfterInit(result):
    """Called after a view is initialized.

    :param result: result of the initialization, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterInit result=" + str(result))

def onBeforeRead():
    """Called before a record is read from the view.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeRead")
    return Continue

def onAfterRead(result):
    """Called after a record is read through the view.

    :param result: result of the read operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterRead result=" + str(result))

def onBeforeInsert():
    """Called before a record is inserted into the view.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeInsert")
    return Continue

def onAfterInsert(result):
    """Called after a view is inserted.

    :param result: result of the insert operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterInsert result=" + str(result))

def onBeforeUpdate():
    """Called before a record is updated through the view.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeUpdate")
    return Continue

def onAfterUpdate(result):
    """Called after a view is updated.

    :param result: result of the update operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterUpdate result=" + str(result))

def onBeforeDelete():
    """Called before a record is deleted through the view.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeDelete")
    return Continue

def onAfterDelete(result):
    """Called after a view is deleted.

    :param result: result of the delete operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterDelete result=" + str(result))

def onBeforeFetch():
    """Called before a record is fetched through the view.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeFetch")
    return Continue

def onAfterFetch(result):
    rvspyTrace("onAfterFetch result=" + str(result))

def onBeforePost():
    """Called before a record is posted through the view.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforePost")
    return Continue

def onAfterPost(result):
    """Called after a view is posted.

    :param result: result of the post operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterPost result=" + str(result))

def onBeforeCancel():
    """Called before a record is canceled through the view.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeCancel")
    return Continue

def onAfterCancel(result):
    """Called after a view is canceled.

    :param result: result of the cancel operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterCancel result=" + str(result))

def onBeforeProcess():
    """Called before a view runs processing.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeProcess")
    return Continue

def onAfterProcess(result):
    """Called after a view finishes processing.

    :param result: result of processing, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterProcess result=" + str(result))

def onBeforeFetchLock():
    """Called before a view locks for a fetch.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeFetchLock")
    return Continue

def onAfterFetchLock(result):
    """Called after a view releases a lock for a fetch.

    :param result: result of the fetch lock operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterFetchLock result=" + str(result))

def onBeforeReadLock():
    """Called before a view locks for a read.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeReadLock")
    return Continue

def onAfterReadLock(result):
    """Called after a view releases a lock for a read.

    :param result: result of the read lock operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterReadLock result=" + str(result))

def onBeforeUnlock():
    """Called before a view is unlocked.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeUnlock")
    return Continue

def onAfterUnlock(result):
    """Called after a view is unlocked.

    :param result: result of the unlock operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterUnlock result=" + str(result))

def onBeforeRecordClear():
    """Called before a view is cleared.

    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeRecordClear")
    return Continue

def onAfterRecordClear(result):
    """Called after a view is cleared.

    :param result: result of the clear operation, 0 on success.
    :type result: int
    :rtype: None
    """
    rvspyTrace("onAfterRecordClear result=" + str(result))

def onBeforeAttributes(event):
    """Called before the attributes of a view field are changed.

    :params event: undocumented.
    :type event: unknown
    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    return Continue

def onAfterAttributes(e):
    """Called after the attributes of a view field are changed.

    :param result: result of the attribute operation, 0 on success.
    :type result: int
    :rtype: None
    """
    if e.field == "AMTCRLIMT":
        # e.isChanged = False
        # e.isEnabled = False
        e.isEditable = False
        # e.isKey = False
        # e.isCalculate = False
        # e.typeChanges = False
        # e.presentationChanges = False
        # e.isRequired = False
        # e.editableChanges = False
        return

def onBeforeGet(event):
    """Called before the value of a field is retrieved through the view.

    :params event: undocumented.
    :type event: unknown
    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforeGet " + e.field)
    return Continue

def onAfterGet(event):
    """Called after a field view is retrieved.

    :params event: undocumented.
    :type event: unknown
    :rtype: None
    """
    rvspyTrace("onAfterGet [" + e.field + "] is [" + str(e.value) + "], result=" + str(e.result))

def onBeforePut(event):
    """Called before the value of a field is put in a view field.

    :params event: undocumented.
    :type event: unknown
    :returns: ``accpac.Continue`` or ``accpac.Abort``
    :rtype: int
    """
    rvspyTrace("onBeforePut [" + str(e.value) + "] to [" + e.field + "]")
    return Continue

def onAfterPut(event):
    """Called after a value is put in the view.

    :params event: undocumented.
    :type event: unknown
    :rtype: None
    """
    rvspyTrace("onAfterPut [" + str(e.value) + "] to [" + e.field + "], result=" + str(e.result))

# Called when the revision list has been cancelled - any changes are discarded
def onRevisionCancelled():
    """Called when the revision list is cancelled, changes are discarded.

    :rtype: None
    """
    rvspyTrace("onRevisionCancelled")

# Called when a record in the revision list has been posted to the database
# op:
#  1 = insert
#  2 = update
#  3 = delete
#  4 = move
def onCommitRecord(op):
    """Called when a record in the revision list has been posted.

    :param op: operation code, one of:

        -  1 = insert
        -  2 = update
        -  3 = delete
        -  4 = move
    :type op: int
    :rtype: None
    """
    rvspyTrace("onCommitRecord" + str(op))

# Called when the revision list has been successfully posted
def onRevisionPosted():
    """Called when a revision has been posted.

    :rtype: None
    """

    rvspyTrace("onRevisionPosted")
