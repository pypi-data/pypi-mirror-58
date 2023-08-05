from bdata.bdata import bdata,life
from bdata.mdata import mdata,mdict,mhist,mscaler,mvar,mcontainer,mlist,mcomment
from bdata.bjoined import bjoined
from bdata import mudpy

import os

__all__ = ['bdata','mudpy','bjoined','mdata']
__version__ = '5.0.2'
__author__ = 'Derek Fujimoto'
_mud_data = os.path.join(os.environ['HOME'],'.mdata')
