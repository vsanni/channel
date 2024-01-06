"""
Created on Fri Mar 31 06:27:32 2023

@author: 25177612+vsanni@users.noreply.github.com
"""

from channel.generator import sinusoid,random_normal
from jumble.units_prefixed import us, ms, MHz, ns, GHz

import figs


X = sinusoid()


sX =  random_normal(T=1,dt=1*ms)

Y = X+sX

CC = X.correlate(Y)


figs.close_all()

fig, ax = figs.axes(3)

X.plot (axis = ax[0])
Y.plot (axis = ax[1])
CC.plot(axis = ax[2])
