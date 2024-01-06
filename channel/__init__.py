"""
Filename      : __init__.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""

__author__     = "vsanni"
__email__      = "vsanni@local.com"

__name__       = "channel"
__version__    = "2.3.9" #@Version@ please, do not edit this line
__status__     = "alpha" #@Status@ please, do not edit this line
__date__       = "01/06/2024" #@Date@ please, do not edit this line

from os               import listdir

from channel.CS       import ChannelCS, IsChannelCS
from channel.VS       import ChannelVS, IsChannelVS
from jumble.vprint    import vprint
from jumble.type_extra import as_list
from container import Container

import jumble.file_location as floc



__verbosity_level__ = 1


def Channel(t=None, X=None, st = None, sX = None, **kv):
    """
    *Synopsis*:

    Channel(t=None, X=None, st = None, sX = None, names=[None, None], **kv)

    Create a Constant Sampling channel:

        f0 = 2.4

        t = np.arange(-10,10,0.01)

        x = np.sin(2*np.pi*f0*t)/t

        ChC = Channel((-10.0, .01),  x, names=['time' , 'Current'], unitss=['s','A'])

    Create a Variable Sampling channel:

        ChV = Channel(t, x, names=['time' , 'Current'], units=['s','A'])
    """

    _channel = None
    for c in channel_definition.values():
        if   c[1](t, X):
          _channel = c[0]
          break

    if _channel is None:
        raise Exception("Channel: error, unrecognizable channel type, cannot initialize channel.")

    return _channel(t=t, X=X, st =st, sX = sX, **kv)



def add_definition(name, constructor, type_detector):
    global channel_definition

    function_type = type(Channel)
    if name not in channel_definition:
        if  not isinstance(type_detector, function_type):
           raise ValueError("add_definition: error, _typeDetector must be functions" )

        channel_definition[name] = [ constructor, type_detector]

    else:
       raise ValueError("add_definition: error, channel type \"%s\" already defined" % name)



def add_channel_member(name_descriptor, D, property_=None):

    property_ = as_list(property_, len(D))

    for (k,v), prop  in  zip(D.items(),property_):
        setattr( channel_definition[k][0], name_descriptor, v if prop is None else property(v))
        vprint(__verbosity_level__, 3, " %s," % k)



def add_channel_method(name_descriptor, D):

    vprint(__verbosity_level__, 3, "%s method added to Channel type:" % name_descriptor)

    add_channel_member(name_descriptor, D, property_= None)

    vprint(__verbosity_level__, 3, "\n")



def add_channel_property(name_descriptor, D):

    vprint(__verbosity_level__, 3, "%s property added to Channel type:" % name_descriptor)

    add_channel_member(name_descriptor, D, property_= True)

    vprint(__verbosity_level__, 3, "\n")



channel_definition = Container()

add_definition("ChannelCS", ChannelCS, IsChannelCS)
add_definition("ChannelVS", ChannelVS, IsChannelVS)


for fl in listdir(floc.path(__import__("channel").__file__)+"/methods"):
    if fl.find(".py") > 0:
        __import__("channel.methods."+fl[:-3])
