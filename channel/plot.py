"""
Filename      : plot.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""


import figs

from container import Container

class Plot():

    plot_decor = Container(units_prefix = ["max"]*2)

    def _is_new_plot(self, decs):

        if   "axis"   not in decs.keys()            : return True
        elif "axis"   in decs.keys()                : return False if decs.axis is None else True
        elif "is_new" not in decs.axis.decors.keys(): return True
        elif decs.axis.decors.is_new                : return True
        else                                        : return False



    def _decors(self,decs={}, **kv):

        decs = Container(figs._plot_keys_expand(decs), **kv)

        if "xunits" in decs.keys():
            if decs.xunits[:2] != "dB": self._error("channel's units cannot be changed or assigned in a plot")
            else                      : decs.xunits = "%s(%s)" % (decs.xunits,self.xunits )
        else:
            decs.xunits = self.xunits

        if "yunits" in decs.keys():
            if decs.yunits[:2] != "dB": self._error("channel's units cannot be changed or assigned in a plot")
            else                      : decs.yunits = "%s(%s)" % (decs.yunits,self.units )
        else:
            decs.yunits = self.units

        if "legend_label" not in decs: decs.legend_label = self.name


        if self._is_new_plot(decs):
            if "xunits_prefix" not in decs: decs.xunits_prefix = self.plot_decor.units_prefix[0]
            if "yunits_prefix" not in decs: decs.yunits_prefix = self.plot_decor.units_prefix[1]
            if "xlabel"        not in decs: decs.xlabel        = self.xdescription
            if "ylabel"        not in decs: decs.ylabel        = self.description
            if "xsymbol"       not in decs: decs.xsymbol       = self.xsymbol
            if "ysymbol"       not in decs: decs.ysymbol       = self.symbol

        else:
            if   "xunits_prefix" in decs: self._error("channel's xunits_prefix cannot be changed in an existing plot")
            elif "yunits_prefix" in decs: self._error("channel's yunits_prefix cannot be changed in an existing plot")



        return decs


    def plot_xy          (self, **decs ): return figs.plot        ( self.t[:], self.X,                             **self._decors(decs, figure_title="plot_xy"          ))
    def plot_step        (self, **decs ): return figs.step        ( self.t[:], self.X,                             **self._decors(decs, figure_title="plot_step"        ))
    def plot_scatter     (self, **decs ): return figs.scatter     ( self.t[:], self.X,                             **self._decors(decs, figure_title="plot_scatter"     ))
    def plot_fill_xy     (self, **decs ): return figs.fill        ( self.t[:], self.X,                             **self._decors(decs, figure_title="plot_fill_xy"     ))
    def plot_fill_between(self, **decs ): return figs.fill_between( self.t[:], self.X,                             **self._decors(decs, figure_title="plot_fill_between"))
    def plot_bar         (self, **decs ): return figs.bar         ( self.t[:], self.X,                             **self._decors(decs, figure_title="plot_bar"         ))
    def plot_stem        (self, **decs ): return figs.stem        ( self.t[:], self.X,                             **self._decors(decs, figure_title="plot_stem"        ))
    def plot_errorbar    (self, **decs ): return figs.errorbar    ( self.t[:], self.X, yerr=self.sX, xerr=self.st, **self._decors(decs, figure_title="plot_errorbar"    ))

    plot = plot_xy



    def figure_close(self, fig=None): figs.close(fig)

    def figure_close_all(self): figs.close_all()

    def figure_set_title(self, title=None):

        if title is not None: self.plot_decor.fig_title = title

        figs.set_title(self.plot_decor.fig, self.plot_decor.fig_title)
