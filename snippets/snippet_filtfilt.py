"""
Filename      : snippet_filtfilt.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import channel.generator as CG
import figs
from scipy import signal as si


dt = 0.0001

b, a = si.butter(8, 50, fs=1/dt)
figs.close_all()

X = CG.comb(f=[12.5, 457.], dt=dt, sigma_x0_noise=0.1)

X.unitss = ["s","V"]

X_f = X.filtfilt(b,a)

fig, ax = X.plot_xy(title="filtfilt")

X_f.plot_xy(axis=ax)
