"""
Filename      : PS.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method, Container
import numpy as np
import rf.sp as sp



def ps (self, df = None, Window_type = "hanning", a = 0.5, detrend = 1, name = None ):

    Dt     = (self.stop-self.start)
    df_min = 1.0/Dt

    if df is None:
        df = df_min

    elif df < df_min:
        raise ValueError("ps: error, window length, %g s, allows a minimum frequency bin of %g " % (Dt, df_min))

    N = 2<<sp.max_power_of_two(int(self.sampling_frequency/df))-1

    S = Container(name        = name,
                  df          = df,
                  Window_type = Window_type,
                  a           = a,
                  sf          = self.sampling_frequency,
                  detrend     = detrend,
                  N           = N,
                  w           = sp.window_calc(N, Window_type),
                  Windows     = 0,
                  NormFactor  = 0,
                  function    = "ps"
                  )

    f, P, S.Windows, S.NormFactor = sp.PS (self.X, S.w, S.a, S.sf, S.detrend, None, 0)

    ch = self.__class__((f[0], f[1]-f[0]), P,
                        names          = ("Frequency", "PS_%s" % self.name if name is None else name),
                        unitss         = self.unitss,
                        symbols        = ("f"        , r"PS\left\{%s\right\}" %  self.symbol     ),
                        descriptions   = ("frequency", "Power spectrum of %s" %  self.description),
                        parameters     = S
                        )
    #TODO, this is a patch, units conversion
    ch.unitss = ("Hz" if self.xunits == "s" else "1/(%s)" % self.xunits,
                 "(%s)^2" % self.units)

    return ch


add_channel_method("ps" , {"ChannelCS": ps})
