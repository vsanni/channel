"""
Filename      : snippet_channel_CS.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import numpy as np
from channel.CS import ChannelCS

t0 = 12.4
dt = .001
nu = 5
t  = np.arange(1000)*dt
x  = np.sin(2*np.pi*nu*t)

X = ChannelCS( t=(t0, dt),
               X=x,
               names        = ['time' , 'Module21_I'],
               unitss       = ['s','A'],
               descriptions = ["elapsed time", "Current across resistor $R_1$"],
               symbols      = ["t", "I"]
               )

print(X)
