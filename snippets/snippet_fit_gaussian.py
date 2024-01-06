"""
Filename      : snippet_integrate.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


import numpy          as np
import figs
from channel      import Channel
from jumble.units_prefixed import mA
#%%
t =  np.linspace(0,10,2000)
x  = np.random.randn(len(t))/20*mA

X = Channel( (0, t[1]), x,
            names        = ['time' , 'Current'],
            unitss       = ['s','A'],
            descriptions = ["elapsed time", "Current across resistor $R_1$"],
            symbols      = ["t", "I"])


#%%
mu, sigma, x0, x1 = 0.0, 1.0, 0.5, 0.0
N =  200

t = np.linspace(-5*sigma,5*sigma, N)
x = x0 * np.exp( -0.5*((t-mu)/sigma)**2 ) + x1+np.random.randn(N)/20

X.X[1500:1500+len(t)] = x*mA

#%%
figs.close_all()

X.plot_xy()

fit = X.fit("FitGaussian")

fit.plot()
fit.plot_comparison()
fit.plot_residuals()

#%%
X[7.5:8.5].plot_xy()

fit = X[7.5:8.5].fit("FitGaussian")

fit.plot()
fit.plot_comparison()
fit.plot_residuals()
