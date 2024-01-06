"""
Filename      : snippet_integrate.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

from channel import Channel , generator as gen
from jumble.units_prefixed import us, MHz, uF
import numpy as np
import figs

dt  = 0.01*us
t0  = 2.0*us
t   = gen.steps(t0, 5*us, dt) # time vector
C_s = 1*uF
f0  = 1*MHz

I = Channel((t0, dt), np.sin(2*np.pi*f0*t),
            names           = ['time' , 'Current'],
            unitss          = ['s','A'],
            descriptions    = ["elapsed time", "Voltage across capacitor $C_s$"],
            symbols         = ["t", "I"])

V = 1/C_s*I.integrate_simpson()

P=V*I

#%%
P.units       = "W"
P.symbol      = "P_s"
P.names       = [ "time","power"]
P.description = "Power Across the Capacitor $C_s$"

P[2.5*us:5.6*us].plot()

#%%


figs.export(file_location="readme_example")
