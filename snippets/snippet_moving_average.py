"""
Filename      : snippet_moving_average.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import channel.generator as CG
import figs
import numpy as np

figs.close_all()

X = CG.comb(f=[12.4, 621], sigma_x0_noise=.1)

XS = X.moving_average(200)

fig, ax = X.plot_xy()

XS.plot(axis=ax)

XSS = (XS - XS.mean())*20

XSS.plot(axis=ax)
