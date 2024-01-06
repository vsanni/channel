"""
Filename      : snippet_ps..py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import channel.generator as CG
import figs
import numpy  as np

figs.close_all()


X = CG.comb(f=np.arange(1,11)*60, T=50, dt=.00001, sigma_x0_noise=0.0001, unitss=["s","V"])

X_PS = X.ps()

X_PS.plot_xy(yunits="dBm", xscale="log", yunits_prefix=None)

X_PS.plot_xy(scale="log", units_prefix=None)
