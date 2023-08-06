# Copyright (C) 2018-2019 F. Cuvelier
from __future__ import print_function
import numpy as np

def gitinfo():
  return {'name': 'fc-bench', 'tag': '0.2.0', 'commit': '56ba4901391836cc91e2ce64c6f15699b966fdd5', 'date': '2019-12-23', 'time': '07-53-49', 'status': '0'} # automatically updated
  if len(inf)>0: # Only for developpers
    return inf
  import fc_tools,fc_bench,os
  D=os.path.realpath(os.path.join(fc_bench.__path__[0],os.path.pardir))
  if os.path.basename(D)=='src':
    D=os.path.realpath(os.path.join(D,os.path.pardir))
  return fc_tools.git.get_info(D)
    

class bData:
  def __init__(self,name,value,sformat,strlen=0,numpy=''):
    self.name=name # str
    self.value=value # scalar
    self.sformat=sformat # example '{:8}' for integer, '{:8.3f}' '{:12.3e}'   for double, '{:>10}' for string
    self.strlen=strlen
    self.numpy=numpy  # i4, i8, f8, ...
    self.set_strlen(strlen)
    self.strnumpy()
    
    
  def str(self):
    return self.sformat.format(self.value)
  
  def strnumpy(self):
    if not (self.numpy==''):
      return
    if isinstance(self.value,str):
      self.numpy=':>%d'%self.strlen
      return
    if hasattr(self.value,'dtype'):
      self.numpy=self.value.dtype.str
      return
        
    
  def set_strlen(self,slen):
    from fc_tools.others import is_function
    if not is_function(self.value) and self.strlen==0:
      self.strlen=max(len(self.name),len(self.sformat),len(self.sformat.format(self.value)),slen)+2
    
  def get_value(self,Out):
    from fc_tools.others import is_function
    if is_function(self.value):
      return self.value(Out)
    return self.value
  
class bdatacol:
  def __init__(self,**kwargs):
    self.name=kwargs.get('name','')
    self.values=kwargs.get('values',[]) # a list of nIn values
    self.sformat=kwargs.get('sformat','') # example '{:8}' for integer, '{:8.3f}' '{:12.3e}'   for double, '{:>10}' for string
    self.strlen=kwargs.get('strlen',0)
    self.numpy=kwargs.get('numpy','')
    #self.info=kwargs.get('info',[])
  
  def str(self,row):
    return self.sformat.format(self.values[row])
    
def bdatacol_bdata(bD,nIn):
    #isinstance(bD,fc_bench.bench.bData)
    assert isinstance(bD,bData)
    bDc=bdatacol()
    bDc.name=bD.name
    bDc.sformat=bD.sformat
    bDc.strlen=bD.strlen
    bDc.numpy=bD.numpy
    bDc.values=[None]*nIn
    return bDc

def setfun(N,verbose,**kwargs):
  import fc_oogmsh,fc_mesh
  d=kwargs.pop('d',2) # in [2,2.5,3]
  Type=kwargs.pop('Type',None) # Type of simplices 1: Lines, 2: Triangles, 4: Tedrahedra 
  geofile=kwargs.pop('geofile','condenser11')
  meshfile=fc_oogmsh.buildmesh(d,geofile,N,verbose=0,**kwargs)
  oGh=fc_oogmsh.ooGmsh(meshfile)
  
  if Type is None:
    Type=2 # Triangles
    if oGh.dim==3 and (4 in oGh.types):
      Type=4
  assert Type in oGh.types
  q,me=oGh.extractElement(Type)
  dim,d,nq,nme=fc_mesh.simplicial.get_dims(q,me)
  if verbose:
    print('# geofile: %s'%geofile)
    print('#  -> dim=%d, d=%d'%(dim,d))
  
  bDs=[bData('{:>8}'.format('N'),N,'{:8}'),bData('{:>8}'.format('nq'),nq,'{:8}'),bData('{:>8}'.format('nme'),nme,'{:8}')]
  return ((q,me),bDs)

def line_text_delimiter():
  return '#'+ 75*'-'

def str_bDs(bDs):
  #s=' '*8 # len of '#labels:'
  s=''
  for bD in bDs:
    sf='{:>%d}'%bD.strlen
    s+=sf.format(bD.str())
  return s

def formats_bDs(bDs):
  s='#format:' 
  for bD in bDs:
    #l=len(bD.name)
    l=bD.strlen
    fmt='{:>%d}'%l
    s+=fmt.format(bD.sformat)
  return s

def numpy_bDs(bDs):
  s='#numpy: ' 
  for bD in bDs:
    #l=len(bD.name)
    l=bD.strlen
    fmt='{:>%d}'%l
    s+=fmt.format(bD.numpy)
  return s

def title_bDs(bDs):
  s=''
  for bD in bDs:
    sf='{:>%d}'%bD.strlen
    s+=sf.format(bD.name)
  st='#labels:'  
  s=st+s
  return s,len(st)

def print_info(**kwargs):
  Print=kwargs.pop('Print',lambda s: print(s))
  import fc_tools.Sys as fc_sys 
  CPU=fc_sys.getCPUinfo();
  OS=fc_sys.getOSinfo();
  Print('#%12s: %s'%('computer',fc_sys.getComputerName()))
  Print('#%12s: %s (%s)'%('system',OS['description'],OS['arch']))
  Print('#%12s: %s'%('processor',CPU['name']))
  Print('#%13s (%d procs/%d cores by proc/%d threads by core)'%(' ',CPU['nprocs'],CPU['ncoreperproc'],CPU['nthreadspercore']))
  Print('#%12s: %3.1f Go'%('RAM',fc_sys.getRAM()))
  soft,release=fc_sys.getSoftware()
  Print('#%12s: %s'%('software',soft))
  Print('#%12s: %s'%('release',release))


def mean_run(fun,datas,nbruns,copyinput):
  import time
  import numpy as np
  Tcpu=np.zeros((nbruns+2,))
  if copyinput: # if input is modified
    import copy
    datascopy=copy.deepcopy(datas)
  else:
    datascopy=datas
    
  for i in range(0,nbruns+2):
    if isinstance(datas,tuple):
      tstart=time.time()
      Out=fun(*datascopy)
      Tcpu[i]=time.time()-tstart
    else:
      tstart=time.time()
      Out=fun(datascopy)
      Tcpu[i]=time.time()-tstart
    if copyinput:
      #Out=copy.deepcopy(Out)
      datascopy=copy.deepcopy(datas)
  Tcpu.sort()  
  tcpu=np.mean(Tcpu[1:-1])
  return tcpu,Out

def biprint(S,fid):
  print(S)
  if fid is not None:
    fid.write(S+'\n')
    
def funname_small(fun):
  if isinstance(fun,str):
    name=fun
  else:
    name=fun.__name__
  I=name.rfind('.')
  if I>=0:
    name=name[I+1:]
  I=name.rfind('_')
  if I>=0:
    name=name[:I]
  return name  

def build_open_filename(Fun,**kwargs):
  name=kwargs.pop('name','')
  tag=kwargs.pop('tag','')
  Date=kwargs.pop('date',False)
  savefile=kwargs.pop('savefile', '')
  save=kwargs.pop('save',False)
  savedir=kwargs.pop('savedir', '') # relative to currrent path. default 'benchs'
  import time,os
  from fc_tools.others import mkdir_p
  DateNum=time.time()
  fid=None
  if len(savefile)>0 or len(savedir)>0 or len(tag)>0:
    save=True    
  if not save:  
    return (fid,savefile,DateNum)
  if len(savedir)==0:
    savedir='benchs'
  mkdir_p(savedir)  
  
  if len(savefile)==0:
    savefile=funname_small(Fun)
  savefile, ext = os.path.splitext(savefile)
  if len(ext)==0:
    ext='.out'
  if Date:
    strdate=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(DateNum))
  else:
    strdate=''
  if len(tag)>0:  
    savefile+='_'+tag
  if len(strdate)>0:  
    savefile+='_'+strdate
  savefile=os.path.join(savedir,savefile+ext)
  try:
    fid=open(savefile,'w')
  except IOError:
    print("Could not open file <%s> !"%savefile)
  return (fid,savefile,DateNum)
      
def strfun(fun):
  from fc_tools.others import is_lambda_function,func2str
  if is_lambda_function(fun):
    return func2str(fun,source=True)
  else:
    return func2str(fun,source=False)
  
def setBDatasAdd(BDs,Out,addBD):
  if addBD is None: 
    return BDs
  if isinstance(addBD,list):
    for k in range(len(addBD)):
      BDs.append(addBD[k])
      BDs[-1].value=BDs[-1].value(Out)
    return BDs
  if isinstance(BDs,bData):
    BDs.append(addBD)
    BDs[-1].value=BDs[-1].value(Out)
  return BDs 
  
def setBDatasError(BDs,Error,Out,i):
  from fc_tools.others import is_function,get_nargin
  if is_function(Error):
    Error=[Error]
  nE=len(Error);
  if nE>1:
    fname=lambda i,j: '  Error[%d,%d]'%(i,j)
  else:
    fname=lambda i,j: '  Error[%d]'%i
  for j in range(nE):
    if get_nargin(Error[j])==len(Out):
      E=Error[j](*Out)
    else:
      E=Error[j](Out)
    name=fname(i,j)
    BDs.append(bData(name,E,'{:%d.3e}'%(len(name)+3)))
  return BDs

def setBDatasCompFun(BDs,compFun,OutRef,Out,i):
  from fc_tools.others import is_function,get_nargin
  if is_function(compFun):
    compFun=[compFun]
  nE=len(compFun);
  if nE>1:
    fname=lambda i,j: '  comp[%d,%d]'%(i-1,j)
  else:
    fname=lambda i,j: '  comp[%d]'%(i-1)
  for j in range(nE):
    E=compFun[j](OutRef,Out)
    name=fname(i,j)
    BDs.append(bData(name,E,'{:%d.3e}'%(len(name)+3)))
  return BDs

def set_names(names,Lfun):
  if names is None:
    names=[]
    for fun in Lfun:
      names.append(fun.__name__)
  else:
    assert len(names)==len(Lfun)
    for i in range(len(names)):
      if len(names[i])==0:
        names[i]=Lfun[i].__name__
  return names

def print_labelsinfo(names,Lfun,compfun,Print,ltd):
  from fc_tools.others import is_function
  Print('# Benchmarking functions:')
  for i in range(len(names)):
    Print('#   fun[%d], %14s: %s'%(i,names[i],strfun(Lfun[i])))
  if compfun is not None:
    Print(ltd) 
    Print('# Comparative functions:')
    if is_function(compfun):
      Print('#   comp[i-1], error between fun[0] and fun[i] by using')
      Print('#        %s'%strfun(compfun))
      Print('# where')
      Print('#    - 1st input parameter is the output of fun[0]')
      Print('#    - 2nd input parameter is the output of fun[i]')
    else:
      for s in range(len(compfun)):
        Print('#   comp[i-1,%d], compares outputs of fun[0] and fun[i]\n#       %s'%(s,strfun(compfun[s])))
      Print('#    For each comparative function:')
      Print('#      - 1st input parameter is the output of fun[0]')
      Print('#      - 2nd input parameter is the output of fun[i]')
      
def setBenchColumns(setbDs,Lfun,names,before,after,Errors,compfun,nIn):
  nfun=len(Lfun)
  Res=[]
  for s in setbDs:
    Res.append(bdatacol_bdata(s,nIn))
  for i in range(nfun):
    if len(before)==nfun:
      for s in before[i]:
        Res.append(bdatacol_bdata(s,nIn))
    name=names[i]+'(s)'  # cputime in second
    Res.append(bdatacol(name=name,values=[None]*nIn,sformat='{:%d.3f}'%(len(name)),strlen=len(name)+3,numpy='f8'))
    if len(after)==nfun:
      for s in after[i]:
        Res.append(bdatacol_bdata(s,nIn))
    if len(Errors)>0:
      nE=len(Errors)
      if nE>1:
        fname=lambda i,j: '  Error[%d,%d]'%(i,j)
      else:
        fname=lambda i,j: '  Error[%d]'%i 
      for j in range(nE):
        name=fname(i,j)
        Res.append(bdatacol(name=name,values=[None]*nIn,sformat='{:%d.3e}'%(len(name)),strlen=len(name)+3,numpy='f8'))
    if i>0:
      nE=len(compfun)
      if nE>1:
        fname=lambda i,j: '  comp[%d,%d]'%(i-1,j)
      if nE==1:
        fname=lambda i,j: '  comp[%d]'%(i-1) 
      for j in range(nE):
        name=fname(i,j)
        Res.append(bdatacol(name=name,values=[None]*nIn,sformat='{:%d.3e}'%(len(name)),strlen=len(name)+3,numpy='f8'))
  return Res

def print_title(Res,DateNum,nbruns,Print):
  import time
  Print('#date:{}'.format(time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(DateNum))))
  Print('#nbruns:{}'.format(nbruns))
  Print(numpy_bDs(Res))
  Print(formats_bDs(Res))
  slabels,ns=title_bDs(Res)
  Print(slabels)
  return (slabels,ns)
  
def computeFun(fun,Out):
  from fc_tools.others import is_function,get_nargin
  assert is_function(fun)
  if get_nargin(fun)==len(Out):
    E=fun(*Out)
  else:
    E=fun(Out)
  return E

def computeFun2(fun,OutRef,Out):
  from fc_tools.others import is_function,get_nargin
  assert is_function(fun)
  if get_nargin(fun)==len(Out):
    E=fun(*Out)
  else:
    E=fun(Out)
  return E
  
def computeBenchColumns(Res,setfun,Lfun,names,before,after,compfun,nbruns,copyinput,row):
  from fc_tools.others import is_function
  datas,bDs,Errors=setfun()
  if is_function(Errors):
    Errors=[Errors]
  nfun=len(Lfun)
  k=0
  for i in range(nfun):
    fun=Lfun[i]
    tcpu,Out=mean_run(fun,datas,nbruns,copyinput)
    if i==0:
      OutRef=Out
      for s in bDs:
        Res[k].values[row]=s.get_value(Out)
        k+=1
    if len(before)==nfun:
      for s in before[i]:
        Res[k].values[row]=s.get_value(Out)
        k+=1
    Res[k].values[row]=tcpu
    k+=1
    if len(after)==nfun:
      for s in after[i]:
        Res[k].values[row]=s.get_value(Out)
        k+=1
    for j in range(len(Errors)):
      Res[k].values[row]=computeFun(Errors[j],Out)
      k+=1
    if i>0:
      for j in range(len(compfun)):
        Res[k].values[row]=compfun[j](OutRef,Out)
        k+=1
    
  return Res

def PrintRow(Res,Print,ns,row):
  s=''
  for j in range(len(Res)):
    sf='{:>%d}'%Res[j].strlen
    s+=sf.format(Res[j].str(row))
  Print(' '*ns+s)
  

def bench(Lfun,setfun,In,**kwargs):
  import time
  #from inspect import getfullargspec
  from fc_tools.others import is_function,get_nargin
  #LN=np.array(LN,dtype=int)
  nbruns=kwargs.get('nbruns', 5)
  debug=kwargs.pop('debug', True)
  compfun=kwargs.pop('compfun', [])
  comment=kwargs.pop('comment', [])
  info=kwargs.pop('info', True)
  copyinput=kwargs.pop('copyinput', False) 
  labelsinfo=kwargs.pop('labelsinfo', False)
  names=kwargs.pop('names', None)
  before=kwargs.pop('before', [])
  after=kwargs.pop('after', [])
  
  if isinstance(In, np.ndarray):
    if len(In.shape)==2:
      if In.shape[1]==1:
        In=In.flatten()
  
  #assert(isinstance(compfun, list)," <compfun> option must be a list")
  #assert( (len(compfun)==0) or (len(compfun)==len(Lfun))," <compfun> option: len(compfun)==0 or len(compfun)==len(Lfun)")
  
  names=set_names(names,Lfun)
  
  if isinstance(comment,str):
    comment=[comment]
  if is_function(compfun):
    compfun=[compfun]  
      
  (fid,savefile,DateNum)=build_open_filename(names[0],**kwargs)    
  Print=lambda S: biprint(S,fid)  
  
  ltd=line_text_delimiter()
  Print(ltd)
  
  if len(comment)!=0:
    for i in range(len(comment)):
      Print(comment[i])
    Print(ltd)  
  
  if info:
    print_info(Print=Print)
    Print(ltd)
        
  datas,setbDs,Errors=setfun(In[0],True,Print=Print,**kwargs)
  Print(ltd)
  if is_function(Errors):
    Errors=[Errors]
  #  Print(ltd)
    
    
  if labelsinfo:
    print_labelsinfo(names,Lfun,compfun,Print,ltd)
    Print(ltd)


  nIn=len(In)
  
  if fid is not None:
    Print('#benchfile: '+savefile);
  
  nfun=len(Lfun)
  isTitle=False
  
  Res=setBenchColumns(setbDs,Lfun,names,before,after,Errors,compfun,nIn)
  slabels,ns=print_title(Res,DateNum,nbruns,Print)
  
  for row in range(nIn):
    N=In[row]
    Res=computeBenchColumns(Res,lambda : setfun(N,False,**kwargs),Lfun,names,before,after,compfun,nbruns,copyinput,row)
    PrintRow(Res,Print,ns,row)
    
  if fid is not None:
    fid.close()
  return Res

