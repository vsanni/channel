"""
Filename      : mixer.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
import rf.sp as SP



def mixer(self, f0=None, phi0=0.0, name= None):

    return self.__class__(t              = (self.start, self.step),
                          X              = SP.mixer(t=self.t[:], x=self.X, f0=f0, phi0=phi0),
                          names          = (self.xname       , "MX.%s"    % (self.name  if name  is None else name )),
                          unitss         = self.unitss,
                          symbols        = (self.xsymbol     , "%s×x"     % self.symbol                             ),
                          descriptions   = (self.xdescription, "mixed %s" % self.description                        ),
                          parameters     = Container(f0=f0, phi0=phi0, function = "mixer", name=name )
                          )

add_channel_method("mixer", {"ChannelCS": mixer})
