"""
Filename      : Integrate.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
from scipy   import signal

def _integrate_common(self, b, name = None, prefix=None, zi=None, unitss=None):

    if zi is None: X    = signal.lfilter(b, [1., -1.], self.X, axis=-1)*self.step
    else         : X, _ = signal.lfilter(b, [1., -1.], self.X, axis=-1, zi=zi)*self.step

    if unitss is None: unitss = [self.xunits,  None if self.xunits is None or self.units is None else self.units+self.xunits]

    ch = self.__class__(t              = (self.start, self.step),
                        X              = X,
                        names          = (self.xname       , prefix + "." + self.name if name is None else name  ),
                        symbols        = (self.xsymbol     , r"%s\left\{%s\right\}" % ( prefix, self.symbol)     ),
                        descriptions   = (self.xdescription, "Integral of %s"  % self.description                ),
                        unitss = unitss,
                        parameters     = Container(  name = name , zi=zi)
                        )

    return ch


def integrate_forward_rectangles(self, name = None, zi=None, unitss=None):

    return _integrate_common(self, [1] , name = name, prefix="FRI", zi=zi, unitss=unitss)



def integrate_trapezoids(self, name = None, zi=None, unitss=None):

    return _integrate_common(self, [1/2, 1/2],  name = name, prefix="TI", zi=zi, unitss=unitss)



def integrate_simpson(self, name = None, zi=None, unitss=None):

    return _integrate_common(self, [1/6, 4/6, 1/6],  name = name, prefix="SI", zi=zi, unitss=unitss)



add_channel_method("integrate_forward_rectangles", {"ChannelCS": integrate_forward_rectangles})
add_channel_method("integrate_trapezoids"        , {"ChannelCS": integrate_trapezoids})
add_channel_method("integrate_simpson"           , {"ChannelCS": integrate_simpson})
