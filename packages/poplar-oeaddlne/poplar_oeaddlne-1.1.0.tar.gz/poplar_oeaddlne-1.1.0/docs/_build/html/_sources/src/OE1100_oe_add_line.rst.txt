===================================
Add OE Line - Screen Script
===================================

This screen script doesn't make any customizations to the UI
but monitors the data sources opened by the screen for changes.
When a new detail line is added, the screen adds another line with
a fixed item.

Unlike in the (broken) view script solution,
:py:mod:`poplar_oeaddlne.OE0500_oe_add_line`, we cannot pass parameters to the
screen script so the item mapping is hard coded.

.. automodule:: poplar_oeaddlne.OE1100_oe_add_line
    :members:
    :undoc-members:
    
