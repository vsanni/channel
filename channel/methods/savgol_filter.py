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

def savgol_filter(self, window_length, polyorder, deriv=0, delta=1.0, axis=-1, mode='interp', cval=0.0, name=None):

    parameters = Container(window_length=window_length, polyorder=polyorder, deriv=deriv, delta=delta, axis=axis, mode=mode, cval=cval)

    return self.__class__(t            = (self.start, self.step)                                             ,
                          X            = signal.savgol_filter(self.X, **parameters)                                 ,
                          names        = (self.xname       , "savgol." + self.name if name is None else name),
                          unitss       = self.unitss                                                         ,
                          symbols      = (self.xsymbol     , r"F\left\{%s\right\}"         % self.symbol    ),
                          descriptions = (self.xdescription, "filter of %s"  % self.description             ),
                          parameters   = parameters
                         )

add_channel_method("savgol_filter", {"ChannelCS": savgol_filter})
