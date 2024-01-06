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

#%%
t =  np.linspace(0,10,2000)
X  = np.random.randn(len(t))/20

X = Channel( (0, t[1]), X,
            names        = ['time' , 'Voltage'],
            unitss       = ['s','V'],
            descriptions = ["elapsed time", "Voltage across resistor $R_1$"],
            symbols      = ["t", "I"])


#%%
mu, sigma, y0, y1 = 0.0, 1.0, 1.0, 0.0
N =  200

x = np.linspace(-5*sigma,5*sigma, N)
y = y0 * np.exp( -0.5*((x-mu)/sigma)**2 ) + y1+np.random.randn(N)/20

X.X[1500:1500+len(y)] = y

#%%
figs.close_all()

X.plot_xy()


#%%
H = X.histogram()

H.plot()

#%%
X[7.5:8.5].plot_xy()

H = X[0:7.5].histogram()

H.plot()


H.plot(yscale="log")
