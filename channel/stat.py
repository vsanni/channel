"""
Filename      : stat.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""

import numpy as np
import jumble.measurement as me
import jumble.units as un
from container import Container
from jumble.vprint import vprint

import channel.pars as pars

class Stat():

    @property
    def _stat_is_stored(self):

        return False # force to always recompute

        # if "stat_stored" not in self.keys()     : return False
        # elif   not   self._channel_is_protected : return False
        # else                                    : return True



    @property
    def stat_values(self):


        if self._stat_is_stored :
            return self.stat_stored

        else:
            n = self.X.argmin()
            N = self.X.argmax()

            self.stat_stored = Container(elements  = self.X.shape[0],
                                         min       = self.X[n],
                                         min_index = n,
                                         mean      = self.X.mean(),
                                         max       = self.X[N],
                                         max_index = N,
                                         std       = self.X.std()
                                         )

        return self.stat_stored



    def _stat_string(self, format="structure", pre_string="", post_string = "", offset=None, field_size=14):

        q = self.stat_values

        min_, min_units , _ = un.prefixed(q.min ,self.units, self.units_prefix)
        mean, mean_units, _ = un.prefixed(q.mean,self.units, self.units_prefix)
        max_, max_units , _ = un.prefixed(q.max ,self.units, self.units_prefix)
        std , std_units , _ = un.prefixed(q.std ,self.units, self.units_prefix)

        if pars.compare(format, "structure"):
            if offset is None : offset="  "
            s  = pre_string
            s += "%sElements  : %d\n"        % (offset, q.elements)
            s += "%sMin, index: %g %s, %d\n" % (offset, min_, min_units , q.min_index)
            s += "%sMean      : %g %s\n"     % (offset, mean, mean_units)
            s += "%sMax, index: %g %s, %d\n" % (offset, max_, max_units , q.max_index)
            s += "%sSTD       : %g %s\n"     % (offset, std , std_units )
            s += post_string

        elif pars.compare(format,"table"):
            if offset is None : offset=" "
            frmt_string = offset+"%"+str(field_size)+"g"
            s = pre_string+"".join([ frmt_string % q[k] for k in ["elements", "min", "min_index", "mean, ""max", "max_index", "std"]])+post_string

        else:
            raise Exception("unknown format \"%s\" specified" % format)

        return s



    def stat_measurement(self, **kv):

        self.stat_values()

        mx = self.stat_stored.mean

        sx = None if self.stat_stored.elements == 1 else self.stat_stored.std/np.sqrt(self.stat_stored.elements-1)

        return  me.string(self.symbol,mx,sx=sx, units=self.units, **kv)


    @property
    def stat(self):
        vprint(0,0, self._stat_string(), on_newline=True)
