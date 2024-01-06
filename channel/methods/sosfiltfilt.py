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

def sosfiltfilt(self,sos, padtype='odd', padlen=None, name = None):

    return self.__class__(t              = (self.start, self.step),
                          X              = signal.sosfiltfilt(sos, self.X, axis=-1, padtype='odd', padlen=None),
                          names          = (self.xname       , "sosfiltfilt." + self.name if name is None else name),
                          unitss         = self.unitss,
                          symbols        = (self.xsymbol     , r"F\left\{%s\right\}" % self.symbol        ),
                          descriptions   = (self.xdescription, "filter of %s"  % self.description         ),
                          parameters     = Container(sos=sos, axis=-1, padtype=padtype, padlen=padlen, function= "sosfiltfilt", name = name)
                          )

add_channel_method("sosfiltfilt", {"ChannelCS": sosfiltfilt})
