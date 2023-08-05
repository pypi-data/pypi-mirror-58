# coding: utf-8
__version__ = '1.0.0-alpha'

"""
    elektron is a Python library to access Refinitiv Data with Python.
    It's usage requires:
        - An Refinitiv Eikon login
        - The Eikon Scripting Proxy
"""


from .core import *
from .content import *
from .delivery import *
from .factory import *
from .function.tools import *
from .pricing import *

from .tools import module_helper


module_helper.delete_reference_from_module(__name__, 'tools')
module_helper.delete_reference_from_module(__name__, 'module_helper')




