"""
Filename      : histogram.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from channel import add_channel_method
from jumble.bin import Bin


def histogram(self, name = None, **kv):

    if "units"        not in kv.keys(): kv["units"      ] = self.units
    if "symbol"       not in kv.keys(): kv["symbol"     ] = self.symbol
    if "description"  not in kv.keys(): kv["description"] = self.description

    bin_ = Bin(x=self.X, **kv)

    bin_.bin()



    return bin_

add_channel_method("histogram", {"ChannelCS": histogram, "ChannelVS": histogram})
