"""
Filename      : moving_average.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, add_channel_property
import numpy as np

def mean(self, *v, **kv): return self.X.mean(*v, **kv )
add_channel_method("mean", {"ChannelCS": mean, "ChannelVS": mean})

def std(self, *v, **kv): return self.X.std(*v, **kv )
add_channel_method("std", {"ChannelCS": std, "ChannelVS": std})

def var(self, *v, **kv): return self.X.var(*v, **kv )
add_channel_method("var", {"ChannelCS": var, "ChannelVS": var})

def _sum(self, *v, **kv): return self.X.sum(*v, **kv )
add_channel_method("sum", {"ChannelCS": _sum, "ChannelVS": _sum})


def _max(self, *v, **kv): return np.max(self.X,*v, **kv )
add_channel_method("max", {"ChannelCS": _max, "ChannelVS": _max})

def _min(self, *v, **kv): return self.X.min(*v, **kv )
add_channel_method("min", {"ChannelCS": _min, "ChannelVS": _min})



def argmax(self, *v, **kv): return np.argmax(self.X,*v, **kv )
add_channel_method("argmax", {"ChannelCS": argmax, "ChannelVS": argmax})

def argmin(self, *v, **kv): return self.X.argmin(*v, **kv )
add_channel_method("argmin", {"ChannelCS": argmin, "ChannelVS": argmin})



def cumprod(self, *v, **kv): return self.like(self.X.cumprod(*v, **kv ), name ="cumprod.%s" %self.name)
add_channel_method("cumprod", {"ChannelCS": cumprod, "ChannelVS": cumprod})

def cumsum(self, *v, **kv): return self.like(self.X.cumsum(*v, **kv ), name ="cumsum.%s" %self.name)
add_channel_method("cumsum", {"ChannelCS": cumsum, "ChannelVS": cumsum})



def _round(self, *v, **kv): return self.like(self.X.round(*v, **kv ), name ="round.%s" %self.name)
add_channel_method("round", {"ChannelCS": _round, "ChannelVS": _round})



def conj(self): return self.like(self.X.conjugate(), name ="conj.%s" %self.name)
add_channel_property("conj", {"ChannelCS": conj, "ChannelVS": conj})

def imag(self): return self.like(X=self.X.imag, name ="imag.%s" %self.name)
add_channel_property("imag", {"ChannelCS": imag, "ChannelVS": imag})

def real(self): return self.like(self.X.real, name ="real.%s" %self.name)
add_channel_property("real", {"ChannelCS": real, "ChannelVS": real})

def _abs(self): return self.like(np.abs(self.X), name ="abs.%s" %self.name)
add_channel_property("abs", {"ChannelCS": _abs, "ChannelVS": _abs})

def angle(self): return self.like(np.angle(self.X), name ="angle.%s" %self.name)
add_channel_property("angle", {"ChannelCS": angle, "ChannelVS": angle})
