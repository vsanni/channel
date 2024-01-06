"""
Filename      : matched_filter.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
from scipy   import signal

def matched_filter(self, signal_template, name = None):

    if isinstance(signal_template, type(self)): signal_template = signal_template.X

    return self.__class__(t              = (self.start, self.step)                                                       ,
                          X              = signal.lfilter(signal_template[::-1], 1, self.X),
                          names          = (self.xname       , "matched_filtered." + self.name if name is None else name),
                          unitss         = self.unitss                                                                   ,
                          symbols        = (self.xsymbol     , r"F\left\{%s\right\}"         % self.symbol              ),
                          descriptions   = (self.xdescription, "filter of %s"  % self.description                       ),
                          parameters     = Container(signal=signal_template, name=name)
                          )

add_channel_method("matched_filter", {"ChannelCS": matched_filter})
