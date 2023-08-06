# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""
Lino Care extension of :mod:`lino_xl.lib.cal`.

.. autosummary::
   :toctree:

    models
    fixtures

"""

from lino_xl.lib.cal import Plugin


class Plugin(Plugin):
    
    extends_models = ['Event']
    needs_plugins = ['lino_care.lib.care']

