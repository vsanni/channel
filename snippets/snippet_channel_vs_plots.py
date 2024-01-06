"""
Filename      : snippet_Channel_VS_plots.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from snippet_channel import VSC
import figs

figs.close_all()

VSC.plot_xy()

VSC.plot_fill_xy()

VSC.plot_step()

VSC.plot_bar()

VSC.plot_scatter()

VSC.plot_stem()
