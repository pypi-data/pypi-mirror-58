=========================
Making an Extender Module
=========================

Now that we have a working version, it is time to think about
delivering it to the client. In almost all cases, the correct way
to distribute your scripts is in a module, even if you only have one.

A module allows you to group scripts together, track versions and
author data, and autoamtically configure scripts at module import time.
Always wrap your tools in modules.

Module format
-------------

Extender modules use an INI style file that includes the metadata,
scripts, and configuration in one file.

Create the new `OEADDLNE` module::

    [MODULE]
    id=OEADDLNE
    name=OEADDLNE
    desc=After an order line with itam A11030 is entered, enter one for A11050
    company=2665093 Ontario Inc.
    version=0.1.0
    website=https://2665093.ca/

    [SCRIPT]
    FILENAME=OEADDLNE_OE1100_oe_add_line.py
    >>> SCRIPT >>>
    # OE1100
    from accpac import *
    ...
    <<< SCRIPT <<<

That is all it takes.  Install modules from the Extender -> Setup -> Modules 
screen.  The script will be installed automatically, and when screen scripts 
are installed they are configured by default.

View Scripts
------------

View scripts get an extra clause in the module file that defines the scripts
configuration: which view it attaches to, which parameters it accepts, etc.

Had we been deploying out view script, we could have made a module that 
included an additional ``VIEWSCRIPT`` block::

    [MODULE]
    id=OEADDLNE
    name=OEADDLNE
    desc=After an order line with itam A11030 is entered, enter one for A11050
    company=2665093 Ontario Inc.
    version=0.1.0
    website=https://2665093.ca/

    [SCRIPT]
    FILENAME=OEADDLNE_OE0500_oe_add_line.py
    >>> SCRIPT >>>
    from accpac import *
    ...
    <<< SCRIPT <<<

    [VIEWSCRIPT]
    VIEWID=OE0500
    UNIQID=2019050100000004
    ACTIVE=1
    ORDER=0
    SCRIPT=OEADDLNE_OE0500_oe_add_line.py
    P1=A1-103/0
    P2=A1-105/0
    P3=1

Now that we have a module, let's get back to the question of how to make the 
mappings user configurable.
