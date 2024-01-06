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

def sosfilt(self, sos, zi=None, name = None):

    X = signal.sosfilt(sos, self.X, axis=-1, zi=zi),

    if zi is not None: X, zfndarray = X
    else             : zfndarray    =  None

    return self.__class__(t            = (self.start, self.step),
                          X            = X,
                          names        = (self.xname       , "sosfilt." + self.name if name is None else name),
                          unitss        = self.unitss,
                          symbols      = (self.xsymbol     , r"F\left\{%s\right\}"         % self.symbol     ),
                          descriptions = (self.xdescription, "filter of %s"  % self.description              ),
                          parameters   = Container(sos=sos, axis=-1, zi=zi, function= "sosfilt", name = name),
                          extra        = Container(zfndarray=zfndarray)
                          )

add_channel_method("sosfilt", {"ChannelCS": sosfilt})
