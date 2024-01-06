"""
Filename      : snippet_ChannelCS_plots.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from snippet_channel import CSC
import figs

figs.close_all()

CSC.plot_xy()

CSC.plot_fill_xy()

CSC.plot_step()

CSC.plot_bar()

CSC.plot_scatter(yunits_prefix="u")

CSC.plot_stem()
