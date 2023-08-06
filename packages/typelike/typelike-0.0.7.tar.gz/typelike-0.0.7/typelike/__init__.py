
from . import core

from .core import *
from .version import __version__

# Contents
# __all__ = ['__version__']
# __all__ += core.__all__
__all__ = [
    'AnyLike',
    'Anything',
    'ListLike',
    'NumberLike',
    '__version__'
]
