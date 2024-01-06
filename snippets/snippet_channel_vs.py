"""
Filename      : snippet_channel_CS.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

import numpy as np
from channel.VS import ChannelVS

t0 = 12.4
dt = .001
nu = 5
N = 500
t  = np.sort(np.arange(0,N,4)+np.random.randint(-2,2,N//4))*dt
x  = np.sin(2*np.pi*nu*t)

X = ChannelVS(t           = t,
              X           = x,
              name        = ['time' , 'Current'],
              units       = ['s','A'],
              description = ["elapsed time", "Current across resistor $R_1$"],
              symbol      = ["t", "I"]
              )

print(X)



X = ChannelVS(t           = t,
              X           = x)

print(X)
