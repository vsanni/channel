"""
Created on Fri Mar 31 06:27:32 2023

@author: 25177612+vsanni@users.noreply.github.com
"""

import numpy as np
from channel.generator import sinusoid, random_normal
from jumble.units_prefixed import us, ms, MHz, ns, GHz

import figs


dt    = 10*ns
sigma = .01

sin = sinusoid(T=3*us, f=10*MHz, dt=dt)

TX  = random_normal(100*us,dt=dt, sigma=sigma, names =["time", "TX"], descriptions=["time", "TX Amplitude"])
TX.sub_add(20*us, sin)

RX  = random_normal(100*us,dt=dt,sigma=sigma, names =["time", "RX"], descriptions=["time", "RX Amplitude"])
RX.sub_add(80*us, sin/100)

RXClean = RX.like(np.zeros(RX.size), name ="RX_clean", description="RX Clean Amplitude")
RXClean.sub_add(80*us, sin/100)


conv = RX.matched_filter(sin)


figs.close_all()

fig, ax = figs.axes(3)

TX.plot  (axis = ax[0])
RX.plot  (axis = ax[1])
RXClean.plot  (axis = ax[1])
conv.plot(axis = ax[2])
