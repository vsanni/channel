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

def correlate(self, X, mode="full",  method="auto", name = None):

    parameters = Container(mode=mode, method=method)
    X          = X                   if not isinstance(X, type(self)) else X.X
    name       = "corr." + self.name if name is None                  else name

    return self.__class__(t            = (self.start       , self.step                                    ),
                          X            =  signal.correlate(self.X, X , **parameters)                        ,
                          names        = (self.xname       , name                                         ),
                          unitss       =  self.unitss                                                      ,
                          symbols      = (self.xsymbol     , r"Corr\left\{%s\right\}"  % self.symbol      ),
                          descriptions = (self.xdescription, "correlation of %s"       % self.description ),
                          parameters   = parameters
                          )

add_channel_method("correlate", {"ChannelCS": correlate})
