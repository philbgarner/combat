"""
package: combat

Provides a DnD style combat system for NakedMud.
"""

import os
import importlib

__all__ = [ ]

# compile a list of all our modules
for fl in os.listdir(__path__[0]):
    if fl.endswith(".py") and not (fl == "__init__.py" or fl.startswith(".")):
        __all__.append(fl[:-3])

# import all of our modules so they can register item types and hooks
#__all__ = ['equipped', 'wielded', 'gear_config', 'gear_config_olc', 'gear_olc']
__all__ = []

for module in __all__:
    importlib.import_module('.' + module, package=__name__)