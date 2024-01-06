"""
Filename      : snippet_generator.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""


import channel.generator as gen
import figs

figs.close_all()

X = gen.chirp(form="linear")

print(X.parameters)
X.plot_xy()

X_PSD = X.psd(df=.2)
X_PSD.plot(xscale="log", xunits_prefix=None)
