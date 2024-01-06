"""
Filename      : moving_average.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
import rf.sp as SP


def moving_average(self, averages=3, name = None):


    return self.__class__(t            = (self.start       , self.step                                      ),
                          X            = SP.moving_average(self.X, averages)                                 ,
                          names        = (self.xname       , "MA." + self.name if name is None else name    ),
                          unitss       = self.unitss                                                         ,
                          symbols      = (self.xsymbol     , r"F\left\{%s\right\}"         % self.symbol    ),
                          descriptions = (self.xdescription, "MovAvg of %s"  % self.description             ),
                          parameters   = Container(averages=averages, function= "moving_average", name= name)
                         )


add_channel_method("moving_average", {"ChannelCS": moving_average})

