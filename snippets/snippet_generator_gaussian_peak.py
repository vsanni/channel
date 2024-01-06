"""
Filename      : snippet_generator.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""


import channel.generator as gen
import figs
from jumble.units_prefixed import ms


X = gen.gaussian_peak(T=10*ms, dt=.01*ms, t0=0.0,t1=3*ms,sigma_t=.1*ms, sigma_x_noise=0.02)

figs.close_all()

X.plot()
