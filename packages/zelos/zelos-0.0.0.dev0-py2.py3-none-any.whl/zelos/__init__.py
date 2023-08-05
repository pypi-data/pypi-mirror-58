__version__ = "0.0.0.dev0"

__title__ = "zelos"
__description__ = "A comprehensive binary emulation platform."
__url__ = "https://github.com/zeropointdynamics/zelos"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"

__author__ = "Zeropoint Dynamics"
__email__ = "zelos@zeropointdynamics.com"

__license__ = "AGPLv3"
__copyright__ = "Copyright (c) 2019 Zeropoint Dynamics"

from .core import Engine


__all__ = ["Engine"]
