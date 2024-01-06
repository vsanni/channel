"""
Filename      : base.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""

import gc, copy as cp

import numpy as np
from jumble.class_base import ClassBase


import channel.pars as pars
import jumble.units as un

from channel.plot import Plot
from channel.properties import Properties
from channel.stat import Stat


verbose = 1

class NumpyChannelBase(ClassBase, Properties, Stat, Plot):


    def __str__(self): return self._status_string(offset="  ")



    def __repr__(self): return "Channel %s, type %s, @ 0x%x\n" % (self.name, self._type, id(self))+self._status_string(offset="  ")



    def _vector_arg_resolve(self, k):

        if isinstance(k, float):
            return self.index_closest(k)

        elif isinstance(k, slice):
            if isinstance(k.start, float) or isinstance(k.stop, float):
                if k.step is not None: self._error("sorry, decimal index slice cannot have a step defined, yet" )

                return slice( *self.index_interval(k.start, k.stop), None)
            else:
                return k

        else:
            return k



    def __setitem__(self, slice_,v):

        slice_ = self._vector_arg_resolve(slice_)

        if   isinstance(v, (tuple, list)) and len(v) == 2:
            self._assign_t(v[0], slice_)
            self._assign_X(v[1], slice_)

        elif isinstance(v, (tuple, list)) and len(v) == 4:
            self._assign_t (v[0], slice_)
            self._assign_st(v[1], slice_)
            self._assign_X (v[2], slice_)
            self._assign_sX(v[3], slice_)
        else:
            self._error("channel bus assignment needs 2 or 4 elements instead of %d"  % len(v))



    def __getitem__(self, slice_ = None): return self._sub(self._vector_arg_resolve(slice_))


    def copy(self): return cp.copy(self)


    def reset(self):

        self._props_defaults()

        self.verbose = 1

        self.t  = None
        self.X  = None
        self.sX = None
        self.st = None

        self._channel_is_protected = False #DO NOT MODIFY THE VALUE OF THIS FLAG VARIABLE! BOOKKEEPING HAS NOT BE IMPLEMENTED YET



    def defaults(self):

        self.reset()



    def __init__(self, t=None, X=None, sX= None, st=None, **kv):

        NumpyChannelBase.defaults(self)

        self._props_update(**kv)

        if X is not None:
            if self._prop.units_original[1] is not None:  X , self.units , _ = un.convert_to_basic( np.asarray(X), units=self.units_original[1], latex=False)
            self._assign_X(X,None)

        if sX is not None:
            if self._prop.units_original[1] is not None:  sX, _          , _ = un.convert_to_basic(np.asarray(sX),units=self.units_original[1], latex=False)
            self._assign_sX(sX,None)

        if t is not None:
            if self._prop.units_original[0] is not None:  t , self.xunits, _= un.convert_to_basic( np.asarray(t),units=self.units_original[0], latex=False)
            self._assign_t(t,None)

        if st is not None:
            if self._prop.units_original[0] is not None:  st, _          , _ = un.convert_to_basic(np.asarray(st),units=self.units_original[0], latex=False)
            self._assign_st(st,None)

        gc.collect()



    def time_check(self, t):
        if self.start <= t <= self.stop: return True
        else                           : self._error("decimal index %g is not in the close interval [ %g, %g]" % (t, self.start, self.stop) )


    def index_closest(self,t):

        self.time_check(t)

        n0 = self.index_left(t)
        n1 = min(n0+1,self.samples-1)

        return n0 if t-self.t[n0] < self.t[n1]-t else n1



    def index_interval(self, t0=None, t1=None):

        s = 0            if t0 is None else self.index_closest(t0)
        e = self.samples if t1 is None else self.index_closest(t1)+1

        return s, e



    def time_interval(self, s=None, e=None):

        ts = self.start if s is None else self.t[s]
        te = self.stop  if e is None else self.t[e]

        return ts, te




    def _status_string(self, format="structure", pre_string="", post_string = "", offset="  ", units_prefix="max"):

        if pars.compare(format,"structure"):
            u = self.xunits

            start, start_units  , _ = un.prefixed(self.start,self.xunits, mode = units_prefix)
            stop , stop_units   , _ = un.prefixed(self.stop,self.xunits, mode = units_prefix)
            stepm , stepm_units , _ = un.prefixed(np.min    (self.step),self.xunits, mode = units_prefix)
            mstep , mstep_units , _ = un.prefixed(np.average(self.step),self.xunits, mode = units_prefix)
            stepM , stepM_units , _ = un.prefixed(np.max    (self.step),self.xunits, mode = units_prefix)

            s  = pre_string
            s += "%sname              : %s [%s], %s\n"         % (offset, self.name, self.units, self.description)
            s += "%sxname             : %s [%s], %s\n"         % (offset, self.xname, u, self.xdescription)
            s += "%sstep Min, Avg, Max: %g %s, %g %s, %g %s\n" % (offset, stepm, stepm_units, mstep, mstep_units, stepM, stepM_units )
            s += "%sstart stop        : (%g %s, %g %s)\n"      % (offset, start, start_units, stop , stop_units)
            s += "%snumber of samples : %g\n"                  % (offset, self.samples)
            s += "%schannel type      : %s\n"                  % (offset, self._type)
            s += post_string

        elif pars.compare(format,"table"):
            s = self.col_status(pre_string=pre_string, post_string=post_string, offset=offset)

        else:
            raise Exception("unknown format \"%s\" specified" % format)

        return s


#%%
    def _algebra_resolve_argument(self, v):

        if isinstance(v, np.ndarray):
            if   v.shape == 1: X, sX =  v    , None
            if   v.shape == 2: X, sX = v[:,0], v[:,1]

        if isinstance(v, (list, tuple)):
            if   len(v) == 1: X, sX = np.asarray(v[0]), None
            if   len(v) == 2: X, sX = np.asarray(v[0]), np.asarray(v[1])

        elif isinstance(v, type(self)):
            X, sX = v.X, v.sX
            self.xequal(v.t)

        elif isinstance(v, (int, float, complex)):
            X, sX = v, None

        return X, sX



    def __add__(self, v):
        X, sX = self._algebra_resolve_argument(v)
        if sX is None: return self.like(self.X+X, None)
        else         : return self.like(self.X+X, np.sqrt( self.sX*self.sX + sX*sX) )



    def __sub__(self, v):
        X, sX = self._algebra_resolve_argument(v)
        if sX is None: return self.like(self.X-X, None)
        else         : return self.like(self.X-X, np.sqrt( self.sX*self.sX + sX*sX) )



    def __mul__(self, v):
        X, sX = self._algebra_resolve_argument(v)
        Y     = self.X*X
        if sX is None:
            return self.like(Y, None)
        else:
            sx_x  = self.sX.X/self.X.X
            sy_y  =        sX/X
            return self.like(Y, Y*np.sqrt( sx_x*sx_x + sy_y*sy_y) )

    __rmul__ = __mul__


    def __truediv__(self, v):
        X, sX = self._algebra_resolve_argument(v)
        Y     = self.X/X
        if sX is None:
            return self.like(Y, None)
        else:
            sx_x  = self.sX.X/self.X.X
            sy_y  =        sX/X
            return self.like(Y, Y*np.sqrt( sx_x*sx_x + sy_y*sy_y) )


    def __neg__(self): return self.like(-self.X, self.sX )



    def __pos__(self): return self.like( self.X, self.sX )



    def __pow__(self, n):
        if self.sX is not None: return self.like(self.X**n,  n * self.X**(n-1)*self.sX)
        else                  : return self.like(self.X**n,  None                     )



    # def __iadd__(self, v):
    #     X, sX = self._algebra_resolve_argument(v)
    #     if sX is None: return self.like(self.X+X, None)
    #     else         : return self.like(self.X+X, np.sqrt( self.sX*self.sX + sX*sX) )


#%%
    def _sub_algebra(self, operator, t0, X, sX= None, st=None):

        if isinstance(X, type(self)):
            if self.step != X.step: self._error("cannot add %s channel  with different sampling time steps" % self._type )
            else                  : X, sX = X.X, X.sX

        n0 = self.index_closest(t0)
        N  = X.size

        if sX is not None:
            Y    = self.X [n0:n0+N]
            sY   = self.sX[n0:n0+N]
            if   operator == "+":
                self.sX[n0:n0+N] = np.sqrt( sY*sY+ sX*sX)
            elif operator == "-":
                self.sX[n0:n0+N] = np.sqrt( sY*sY+ sX*sX)
            elif operator == "*":
                A                =  sY/Y
                B                =  sX/X
                self.sX[n0:n0+N] = X*Y*np.sqrt( A*A+B*B)
            elif operator == "/"      :
                A                =  sY/Y
                B                =  sX/X
                self.sX[n0:n0+N] = Y*X*np.sqrt(A*A+B*B)
            elif operator == "r":
                self.sX[n0:n0+N] = sX

        if   operator == "+": self.X[n0:n0+N] += X
        elif operator == "-": self.X[n0:n0+N] -= X
        elif operator == "*": self.X[n0:n0+N] *= X
        elif operator == "/": self.X[n0:n0+N] /= X
        elif operator == "r": self.X[n0:n0+N]  = X


    def sub_add     (self, t, X, sX= None, st=None): self._sub_algebra("+", t, X, sX, st)
    def sub_subtract(self, t, X, sX= None, st=None): self._sub_algebra("-", t, X, sX, st)
    def sub_multiply(self, t, X, sX= None, st=None): self._sub_algebra("*", t, X, sX, st)
    def sub_divide  (self, t, X, sX= None, st=None): self._sub_algebra("*", t, X, sX, st)
    def sub_replace (self, t, X, sX= None, st=None): self._sub_algebra("r", t, X, sX, st)
