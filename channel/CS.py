"""
Filename      : CS.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import numpy as np
from channel import numpy_base as NCB # better use of a la python composition/inheritance
from jumble.type_extra import length, is_numeric, is_iterable

def IsChannelCS(t, x):

    if t is None:
        if is_iterable(x): return True
        else             : return False

    elif length(t) == 2:
        if length(t[0]) ==1 and is_numeric(t[0]):
            if length(t[1])==1 and is_numeric(t[1]):
                if t[1] > 0:
                    if length(x) != 2:
                        return True
    else:
        dt = np.diff(t)
        if  dt.max() == dt.min():
            if len(t) == len(x):
                return True

    return False


_type   = 'constant sampling'
verbose = NCB.verbose


class TimeIndex():

    def __init__(self, start, step, N ):

        self._start = start
        self._step  = step
        self._N     = N

    def __getitem__(self, n):
        if isinstance( n, slice):
            start = 0       if n.start is None else n.start
            stop  = self._N if n.stop  is None else n.stop
            return np.arange(start, stop, n.step )* self._step+ self._start

        else:
            return n*self._step+self._start

    @property
    def step(self): return self._step
    @step.setter
    def step(self, dt): self._step = dt


    @property
    def start(self): return self._start
    @start.setter
    def start(self, t0): self._start= t0


    @property
    def stop(self): return self.start+(self._N-1)*self.step
    @stop.setter
    def stop(self, t1): self.start = t1 - (self._N-1)*self.step






class ChannelCS(NCB.NumpyChannelBase):

    _type = _type

#%%
    def _assign_X(self, X, slice_):
        if X is None       : self.X         = None
        elif slice_ is None: self.X         = np.asarray(X)
        else               : self.X[slice_] = np.asarray(X)



    def _assign_sX(self, sX, slice_):
        if sX is None      : self.sX        = None
        elif slice_ is None: self.sX         = np.asarray(sX)
        else               : self.sX[slice_] = np.asarray(sX)



    def _assign_t(self, t, slice_= None):

        if slice_ is not None                          : self._error("%s channel x index definition cannot be a  vector " % ChannelCS._type)
        elif isinstance(t, (list,tuple)) and len(t)== 2: self.t = TimeIndex(*t, self.X.size)
        else                                           : self._error("%s channel x index definition must be two values start and step" % ChannelCS._type )




    def _assign_st(self, st, slice_= None): self.st = st

#%%
    @property
    def step(self): return self.t.step
    @step.setter
    def step(self, dt): self.t.step = dt


    @property
    def start(self): return self.t.start
    @start.setter
    def start(self, t0): self.t.start= t0


    @property
    def stop(self): return self.t.stop
    @stop.setter
    def stop(self, t1): self.t.start = t1


    @property
    def sampling_frequency(self): return 1.0/self.t.step
    @sampling_frequency.setter
    def sampling_frequency(self, sf): self.t.step = 1/sf


#%%
    def col_status(self,  offset="", pre_string="", post_string = ""):

        s  = pre_string
        s += '%-32s %14.4g %14.4g %14.4g %14.4g\n' % ( ("'%s' [%s]" % (self.name, self.units)), self.start, self.step, self.stop, self.samples)
        s += post_string

        return s


#%%
    def _sub(self, slice_):
        return self.__class__(X             = self.X [slice_],
                              sX            = None if self.sX is None else self.sX[slice_],
                              t             = (self.start+self.step*slice_.start, self.step) ,
                              names         = self.names,
                              symbols       = self.symbols,
                              descriptions  = self.descriptions,
                              unitss        = self.unitss
                             )



    def _check_index(self, t, n):
        if   n < 0           : self._error("value entered %g produces an index for a value lower than the minimum availabe %g"  % (t, self.start))
        elif n > self.X.size : self._error("value entered %g produces an index for a value higher than the maximum availabe %g" % (t, self.stop ))
        else                 : return n



    def index_left(self, t):
        return self._check_index(t, int((t-self.start)/self.step))



    def index_right(self, t):
        nl = int((t-self.start)/self.step)
        return self._check_index(t, nl if nl*self.step == t else nl+1)


    def like(self, X, sX=None, name=None, symbol=None, description=None, units=None):
        return self.__class__(X             = X,
                              sX            = sX,
                              t             = (self.start, self.step),
                              st            = self.st,
                              names         = [self.xname       , self.name        if name        is None else name       ],
                              symbols       = [self.xsymbol     , self.symbol      if symbol      is None else symbol     ],
                              descriptions  = [self.xdescription, self.description if description is None else description],
                              unitss        = [self.xunits      , self.units       if units       is None else units      ]
                             )



    def xequal(self,t, raise_error=True, error_str="channel has different start and step"):

        if   self.start == t.start and self.step == t.step: return True
        elif not raise_error                              : return False
        else                                              : self._error(error_str)


    def xcompatible(self,t, raise_error=True, error_str="channel has different step"):

        if   self.step == t.step: return True
        elif not raise_error    : return False
        else                    : self._error(error_str)


#%%
    def append(self, X, sX= None):
        if isinstance(X, type(self)):
            if self.xcompatible(X, raise_error=True, error_str="cannot append %s channel with different sampling time steps" % ChannelCS._type):
                X  = X.X
                sX = X.sX

        self.X = np.append(self.X, X)
        if self.sX is not None: self.sX = np.append(self.sX, sX)



    def prepend(self, X, sX= None, st=None):
        if isinstance(X, type(self)):
            if self.xcompatible(X, raise_error=True, error_str="cannot prepend %s channel with different sampling time steps" % ChannelCS._type ):
                X  = X.X
                sX = X.sX

        self.X = np.append(X,self.X)
        if sX is not None: self.sX = np.append(sX, self.sX)


        self.start -= len(X)*self.step
