import cprint
import cprint.main
from cprint.tools import demo as _demo
from cprint.tools import demoid as _demoid
from cprint.tools import getshow_config as _showconfig

__version__ = "1.4.0"

cprint.custom_style = {}

_cpshow = lambda : _showconfig(2)
_cpshoww = lambda : _showconfig(3)

config = cprint = main = tools = None
del config, cprint, main, tools