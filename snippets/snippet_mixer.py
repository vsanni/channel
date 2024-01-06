"""
Filename      : snippet__mixer.py
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

X = CG.sinusoid(T=.0025,dt=1e-5,f=500,x0=1,x1=0)
X.plot_xy()

Y = X.mixer(f0=500,phi0=np.pi/4)

Y.plot_xy()


Y.plot_xy(complex_plot=["modulus","angle"])
