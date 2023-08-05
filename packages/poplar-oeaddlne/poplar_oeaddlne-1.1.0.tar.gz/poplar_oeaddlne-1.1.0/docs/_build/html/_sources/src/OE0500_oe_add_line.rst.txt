===================================
Add OE Line - View Script
===================================

This view script is intended to trigger when a new line is added to
an order.  When triggered, it tries to write a new line to the order
with an item defined in the parameters.  

This script will always fail, causing an error to be raised from the 
view.  It demonstrates a case in which the new script approach is not
suitable, use a Screen script (:py:mod:`poplar_oeaddlne.OE1100_oe_add_line`).

.. automodule:: poplar_oeaddlne.OE0500_oe_add_line
    :members:
    :undoc-members:
    
