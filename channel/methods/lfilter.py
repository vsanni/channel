"""
Filename      : lfilter.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
from scipy   import signal

def lfilter(self, b, a, zi=None, name = None):

    X = signal.lfilter(b, a, self.X, axis=-1, zi=zi)

    if zi is not None: X, zfarray = X
    else             : zfarray    =  None


    return self.__class__(t              = (self.start, self.step),
                          X              = X,
                          names          = (self.xname       , "lfilter." + self.name if name is None else name),
                          unitss          = self.unitss,
                          symbols        = (self.xsymbol     , r"F\left\{%s\right\}"         % self.symbol                    ),
                          descriptions   = (self.xdescription, "filter of %s"  % self.description              ),
                          parameters     = Container(a=a, b=b, axis=-1, zi=zi, name=name, zfarray=zfarray)
                          )

add_channel_method("lfilter", {"ChannelCS": lfilter})
