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


figs.close_all()


X = CG.random_normal(T=10)
print(X.parameters)
X.plot_xy()

H = X.histogram()
H.plot()
