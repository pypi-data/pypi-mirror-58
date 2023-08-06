# Copyright (C) 2018-2019 F. Cuvelier
# License: GNU GPL version 3
__version__='0.2.0' # automaticaly written by setpackages.py script
__packages__={'fc-tools': '0.0.24'} # automaticaly written by setpackages.py script
from .bench import bench,gitinfo
from . import demos

def gitinfo():
  return {'name': 'fc-bench', 'tag': '0.2.0', 'commit': '56ba4901391836cc91e2ce64c6f15699b966fdd5', 'date': '2019-12-23', 'time': '07-53-49', 'status': '0'} # automatically updated
  if len(inf)>0: 
    return inf
  # Only for developpers
  import fc_tools,os
  D=os.path.realpath(os.path.join(__path__[0],os.path.pardir))
  if os.path.basename(D)=='src':
    D=os.path.realpath(os.path.join(D,os.path.pardir))
  return fc_tools.git.get_info(D)
