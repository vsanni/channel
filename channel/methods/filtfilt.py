"""
Filename      : filtfilt.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
from scipy   import signal

def filtfilt(self, b, a, padtype='odd', padlen=None, method='pad', irlen=None, name = None):

    return self.__class__(t              = (self.start, self.step),
                          X              = signal.filtfilt(b, a, self.X, axis=-1, padtype=padtype, padlen=padlen, method=method, irlen=irlen),
                          names          = (self.xname       , "filtfilt." + self.name if name is None else name),
                          unitss         = self.unitss,
                          symbols        = (self.xsymbol     , r"F\left\{%s\right\}"         % self.symbol                    ),
                          descriptions   = (self.xdescription, "filter of %s"  % self.description               ),
                          parameters     = Container(a=a, b=b, axis=-1, padtype=padtype, padlen=padlen, method=method, irlen=irlen, function="filtfilt", name = name)
                  )

add_channel_method("filtfilt", {"ChannelCS": filtfilt})
