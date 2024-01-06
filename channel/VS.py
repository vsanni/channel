"""
Filename      : VS.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import numpy as np
from channel import numpy_base as NCB # better use of a la python composition/inheritance
from jumble.type_extra import length


def IsChannelVS(t,x):

    if length(t) == length(x):
        dt = np.diff(t)
        if dt.max() != dt.min():
            return True

    return False


_type   = 'variable sampling'
verbose = NCB.verbose


class ChannelVS(NCB.NumpyChannelBase):
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



    def _assign_t(self, t, slice_):
        if t is None       : self.t         = None
        elif slice_ is None: self.t         = np.asarray(t)
        else               : self.t[slice_] = np.asarray(t)



    def _assign_st(self, st, slice_):
        if st is None      : self.st         = None
        elif slice_ is None: self.st         = np.asarray(st)
        else               : self.st[slice_] = np.asarray(st)


#%%
    @property
    def step(self)    : return self.t[1:]-self.t[:-1]
    @step.setter
    def step(self, t ):
        if len(t)  == self.X.size: self.t = t
        else                     : self._error("specified vector for %s channel has to be %d long" % ( _type, self.X.size))


    @property
    def start(self)    : return self.t[0]
    @start.setter
    def start(self, t0): self.t += -self.start + t0



    @property
    def stop(self)    : return self.t[-1]
    @stop.setter
    def stop(self, t1): self.t += t1 - self.stop



    @property
    def sampling_frequency(self):  self._error(" sampling frequency is undefined for a %s channel" %(_type))



#%%
    def col_status(self,  offset="", pre_string="", post_string = ""):

        x = self.step
        s = pre_string

        t  = '%-32s %14.4g %14.4g %14.4g %14.4g' % ( ("'%s' [%s]" % (self.name, self.units)), self.start, np.min (x) , self.stop, self.samples)
        n  = len(t)+len(offset)
        s += "%s\n" % t
        s += '%s%-32s %14s %14.4g\n' % (offset, ' ', ' ', np.mean(x))
        s += '%s%-32s %14s %14.4g\n' % (offset, ' ', ' ', np.max (x))
        s += '-' * n + '\n'
        s += post_string

        return s


#%%
    def _sub(self, slice_):

        return self.__class__(X=self.X [slice_], sX=None if self.sX is None else self.sX[slice_],
                              t=self.t [slice_], st=None if self.st is None else self.st[slice_],
                              names          = self.names,
                              symbols        = self.symbols,
                              descriptions   = self.descriptions,
                              unitss         = self.unitss
                             )



    def index_left(self, t=None):

        if t is None        : return 0
        elif t <  self.t[ 0]: return None
        elif t >= self.t[-1]: return self.samples-1

        n0, n1  = 0, self.samples

        while True:
            n = (n0+n1)>>1 # left index because of truncation
            if   t < self.t[n] and n1-n0>1: n1 = n
            elif t > self.t[n] and n1-n0>1: n0 = n
            else                          : break

        return n



    def index_right(self, t):

          if t is None        : return self.samples-1
          elif t >  self.t[-1]: return None
          elif t <=  self.t[0]: return 0
          else                :
              n = self.index_left(t)
              if t == self.t[n]: return n
              else             : return n+1


    def like(self, X, sX=None, name=None, symbol=None, description=None, units=None):
        return self.__class__(X             = X,
                              sX            = sX,
                              t             = self.t[:],
                              st            = None if self.st is None else self.st[:],
                              names         = [self.xname       , self.name        if name        is None else name],
                              symbols       = [self.xsymbol     , self.symbol      if symbol      is None else symbol],
                              descriptions  = [self.xdescription, self.description if description is None else description],
                              unitss        = [self.xunits      , self.units       if units       is None else units]
                             )




    def xequal(self,t, raise_error=True, error_str="channel has different start and step"):

       if   self.t != t    : return True
       elif not raise_error: return False
       else                : self._error(error_str)




#%%
    def append(self, t, X, sX= None, st=None):
        if isinstance(X, type(self)):
            X   = X.X
            sX  = None if self.sX is None else  X.sX
            st  = None if self.st is None else  X.st

        else:
            self._error("cannot append %s channel with different steps" % ChannelVS._type)

        self.t = np.append(self.t,t)
        self.X = np.append(self.X,X)

        if self.sX is not None and sX is not None: self.sX = np.append(self.sX, sX)
        if self.st is not None and st is not None: self.st = np.append(self.st, st)


    def prepend(self, t, X, sX= None, st=None):
        if isinstance(X, type(self)):
            X   = X.X
            sX  = None if self.sX is None else  X.sX
            t   = X.t
            st  = None if self.st is None else  X.st
        else:
            self._error("cannot append %s channel with different steps" % ChannelVS._type)

        self.t = np.append(t,self.t)
        self.X = np.append(X,self.X)

        if self.sX is not None and sX is not None: self.sX = np.append(sX, self.sX)
        if self.st is not None and st is not None: self.st = np.append(st, self.st)
