# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""
Lino Vilma extension of :mod:`lino_xl.lib.contacts`.

"""

from lino_xl.lib.contacts import Plugin


class Plugin(Plugin):
    
    extends_models = ['Person', 'Company']

