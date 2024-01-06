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

def convolve(self, X, mode="full",  method="auto", name = None):

    parameters = Container(mode=mode, method=method)
    X          = X                   if not isinstance(X, type(self)) else X.X
    name       = "conv." + self.name if name is None                  else name

    return self.__class__(t              = (self.start       , self.step                                    ),
                          X              =  signal.convolve(self.X, X , **parameters)                        ,
                          names          = (self.xname       , name                                         ),
                          unitss         =  self.unitss                                                      ,
                          symbols        = (self.xsymbol     , r"Conv\left\{%s\right\}"  % self.symbol      ),
                          descriptions   = (self.xdescription, "convolution of %s"       % self.description ),
                          parameters     = parameters
                          )

add_channel_method("convolve", {"ChannelCS": convolve})
