"""
Filename      : snippet_generator.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""


import channel.generator as CG

import figs

from jumble.units_prefixed import uV


figs.close_all()

X = CG.sinusoid(x0=1*uV, x1=10*uV)
print(X.parameters)
X.plot_xy()
