"""
Filename      : snippet_integrate.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

from channel import Channel
import numpy as np
import figs

t0 = 0
dt = .0001
T  = 1.2
nu = 2.5
t  = np.arange(0,T,dt)
x  = np.sin(2*np.pi*nu*t)/1000
x1 = (1-np.cos(2*np.pi*nu*t))/(2*np.pi*nu)

#X = Channel( (0, .001), np.array([10]*100),
X = Channel( (t0, dt), x,
            names          = ['time' , 'Current'],
            unitss = ['s','A'],
            descriptions   = ["elapsed time", "Current across resistor $R_1$"],
            symbols        = ["t", "I"])

X1 = Channel( (t0, dt), x1,
            names          = ['time' , 'Current'],
            unitss = ['s','A'],
            descriptions   = ["elapsed time", "Current across resistor $R_1$"],
            symbols        = ["t", "I"])


XS = X.integrate_simpson           (unitss =["s","A"])
XR = X.integrate_forward_rectangles(unitss =["s","A"])
XT = X.integrate_trapezoids        (unitss =["s","A"])
#%%
figs.close_all()

fig, ax = X.plot_xy()
XS.plot_xy(axis=ax)
XR.plot_xy(axis=ax)
XT.plot_xy(axis=ax)


#%%

X.plot_xy()

XS.plot_xy()
XR.plot_xy()
XT.plot_xy()
