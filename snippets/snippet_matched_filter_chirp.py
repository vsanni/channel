"""
Created on Fri Mar 31 06:27:32 2023

@author: 25177612+vsanni@users.noreply.github.com
"""

import numpy as np
from channel.generator import chirp, random_normal
from jumble.units_prefixed import us, ms, MHz, ns, GHz

import figs


dt    = 10*ns
sigma = .01

cp = chirp(T=3*us, DT=100*us, f0=10*MHz, f1=1*GHz, dt=dt)

TX  = random_normal(100*us,dt=dt, sigma=sigma, names =["time", "TX"], descriptions=["time", "TX Amplitude"])
TX.sub_add(20*us, cp)

RX  = random_normal(100*us,dt=dt,sigma=sigma, names =["time", "RX"], descriptions=["time", "RX Amplitude"])
RX.sub_add(80*us, -cp/100)

RXClean = RX.like(np.zeros(RX.size), name ="RX_clean", description="RX Clean Amplitude")
RXClean.sub_add(80*us, -cp/100)


conv = RX.matched_filter(-cp)


figs.close_all()

fig, ax = figs.axes(3)

TX.plot  (axis = ax[0])
RX.plot  (axis = ax[1])
RXClean.plot  (axis = ax[1])
conv.plot(axis = ax[2])


CV = conv**2

CV.plot()
