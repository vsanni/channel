"""
Filename      : fit_function.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author        : 25177612+vsanni@users.noreply.github.com
"""


from os      import listdir
from channel import add_channel_method, add_channel_property, __verbosity_level__
from  jumble.vprint import vprint
import jumble.file_location as floc
from container import Container

fit_class ={}
for fl in listdir(floc.path(__import__("fit").__file__)):
    if fl.find(".py") > 0 and fl[0] != "_":
        s          = fl[:-3]
        module     = __import__("fit."+s).__dict__[s]
        class_name = module.__dict__["__name_fit_class"] if "__name_fit_class"  in module.__dict__.keys() else "Fit%s" % s.title().replace("_", "")

        try   : fit_class[class_name] = getattr(module,class_name)
        except: vprint(__verbosity_level__, 2, "\tfit_function: warning, couldn't import class %s from module fit.%s.py" % (class_name, s), on_newline=True )


def fit_function_list(self):
    print("predefined fitting functions: %s" % "".join([ "\n\t\"%s\"" % k for k in fit_class]))


add_channel_property("fit_function_list" , {"ChannelCS": fit_function_list, "ChannelVS": fit_function_list})


def fit(self, function_name=None, name = None, *v, **kv):

    global fit_class

    if function_name is None:
        raise ValueError("channel.fit: error, fit function name missing, use channel function fit_function_list to get list of fitting functions")

    coord = Container(names       = [ self.symbols[0], self.symbols[1], "Delta"+self.symbols[1]],
                      description = [self.xname, self.name, "Residual"],
                      symbol      = self.symbols,
                      units       = [self.xunits, self.units],
                      )

    fit = fit_class[function_name](x=self.t[:], y=self.X, sx=self.st, sy=self.sX, verbose=self.verbose, *v, **kv)

    fit.fit()

    return fit


add_channel_method("fit" , {"ChannelCS": fit, "ChannelVS": fit})
