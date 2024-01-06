"""
Filename      : snippet_channel.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

from channel import Channel
import numpy as np
from jumble.units_prefixed import uA, ms, kHz

t0 = 10*ms
dt = 0.01*ms
nu = 0.75*kHz
t  = np.arange(0,t0,dt)
x  = np.sin(2*np.pi*nu*t)*uA

CSC = Channel((t0, dt), x,
            names           = ['time' , 'Current'],
            unitss          = ['s','A'],
            descriptions    = ["elapsed time", "Current across resistor $R_1$"],
            symbols         = ["t", "I"])

VSC = Channel( t, x,
            names          = ['time' , 'Current'],
            unitss         = ['s','A'],
            descriptions   = ["elapsed time", "Current across resistor $R_1$"],
            symbols        = ["t", "I"])


print(CSC)
print(VSC)
