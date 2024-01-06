"""
Filename      : moving_average.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
from scipy   import signal

def decimate(self, q, n=None, ftype='iir', zero_phase=True, name = None):

    return self.__class__(t       = (self.start, self.step*q),
                   X              = signal.decimate(self.X, q, n, ftype, axis=-1, zero_phase=zero_phase),
                   names          = (self.xname       , "decimate." + self.name if name is None else name),
                   unitss         = self.unitss,
                   symbols        = (self.xsymbol     , r"F\left\{%s\right\}"         % self.symbol                    ),
                   descriptions   = (self.xdescription, "filter of %s"  % self.description              ),
                   parameters     = Container(q=q, n=n, ftype=ftype, axis=-1, zero_phase=zero_phase, function= "decimate", name = name)
                  )

add_channel_method("decimate", {"ChannelCS": decimate})
