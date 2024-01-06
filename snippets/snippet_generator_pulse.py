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

X = gen.pulse(T=100, DT=1, dTs=.1, dT=.37, dTr=.03, sigma_x1_noise=.01, sigma_x0_noise=.1*0, sigma_t_noise=.001, x1=1)

print(X.parameters)
X[0:30.2].plot_xy()

# X_PSD = X.psd(df=.05)
# X_PSD.plot(xscale="log")
