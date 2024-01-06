"""
Filename      : snippet_psd.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import channel.generator as CG
import figs

figs.close_all()

X = CG.sinusoid(T=150, sigma_x1_noise=0)

X_PSD = X.psd()

X_PSD.plot_xy(yunits="dB")

X_PSD.plot_xy(scale=["log","log"])

A = X/X
