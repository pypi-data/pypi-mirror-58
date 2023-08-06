# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)
"""Fixtures specific for the Team variant of Lino Care.

.. autosummary::
   :toctree:

   models


"""

from lino_xl.lib.tickets import *

class Plugin(Plugin):
    """Adds the :mod:`lino_xl.lib.votes` plugin.
    """

    needs_plugins = [
        'lino_xl.lib.excerpts',
        'lino_xl.lib.topics',
        'lino.modlib.comments', 'lino.modlib.changes',
        'lino_xl.lib.votes',
        'lino_care.lib.care']

