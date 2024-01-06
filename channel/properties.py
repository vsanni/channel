"""
Filename      : properties.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""

from container import Container
from jumble.type_extra import length

import numpy as np

class Properties():

    _props_type = Container(names           = ["x_coord"     , "y_coord"     ],
                            symbols         = ["x"           , "y"           ],
                            descriptions    = ["x coordinate", "y coordinate"],
                            unitss          = ["AU"          , "AU"          ],
                            units_original  = [None          , None          ],
                            prefixes        = ["max"         , "max"         ],
                            parameters      = None,
                            meta_data       = None
                            )



    def _props_assign(self, k, v, n=None, raise_error_uknown_par=True):

        N = length(Properties._props_type[k])

        if   n is None:
            if isinstance(Properties._props_type[k], type(None)): self._prop[k] = v
            elif length(v) == N                                 : self._prop[k] = v
            else                                                : self._error("property \"%s\" must be %s" % (k, type(Properties._props_type[k])))

        elif 0 <= n < N:
            type_ = type(Properties._props_type[k][n])
            if  isinstance(v, type_): self._prop[k][n] = v
            elif type_ is type(None): self._prop[k][n] = v
            else                    : self._error("property \"%s\" must be %s" % (k, type_))

        elif n < 0 or n >=N:
            self._error("dont't know what to do with property \"%s\" and %s and element # %d" %(k, str(v), n))

        elif raise_error_uknown_par:
            self._error("dont't know what to do with property \"%s\" and %s" %(k, str(v)))




    def _props_defaults(self):

        self._prop = Container(Properties._props_type)



    def _props_update(self, **kv):

        for  k,v in kv.items(): self._props_assign( k, v)

        return kv



    @property
    def name(self)   : return self._prop.names[1]
    @name.setter
    def name(self, v): self._props_assign( "names", v, 1)

    @property
    def xname(self)   : return self._prop.names[0]
    @xname.setter
    def xname(self, v): self._props_assign( "names", v, 0)

    @property
    def names(self)   : return self._prop.names
    @names.setter
    def names(self, v): self._props_assign( "names", v)



    @property
    def units(self)   : return self._prop.unitss[1]
    @units.setter
    def units(self, v): self._props_assign( "unitss", v, 1)

    @property
    def xunits(self)   : return self._prop.unitss[0]
    @xunits.setter
    def xunits(self, v): self._props_assign( "unitss", v, 0)

    @property
    def unitss(self)   : return self._prop.unitss
    @unitss.setter
    def unitss(self, v): self._props_assign( "unitss", v)



    @property
    def units_original(self)   : return self._prop.units_original
    @units_original.setter
    def units_original(self, v): self._props_assign( "units_original", v)



    @property
    def symbol(self)   : return self._prop.symbols[1]
    @symbol.setter
    def symbol(self, v): self._props_assign( "symbols", v, 1)

    @property
    def xsymbol(self)   : return self._prop.symbols[0]
    @xsymbol.setter
    def xsymbol(self, v): self._props_assign( "symbols", v, 0)

    @property
    def symbols(self)   : return self._prop.symbols
    @symbols.setter
    def symbols(self, v): self._props_assign( "symbols", v)



    @property
    def description(self)   : return self._prop.descriptions[1]
    @description.setter
    def description(self, v): self._props_assign( "descriptions", v, 1)

    @property
    def xdescription(self)   : return self._prop.descriptions[0]
    @xdescription.setter
    def xdescription(self, v): self._props_assign( "descriptions", v, 0)

    @property
    def descriptions(self)   : return self._prop.descriptions
    @descriptions.setter
    def descriptions(self, v): self._props_assign( "descriptions", v)



    @property
    def is_complex(self):  return np.iscomplexobj(self.X)


    @property
    def type(self): return self._type


    @property
    def samples(self): return 0 if self.X is None else self.X.size


    @property
    def status(self): print(self._status_string(), on_newline=True)

    @property
    def container(self): return Container(self)

    @property
    def size(self): return len(self.X)


    @property
    def parameters(self): return self._prop.parameters
    @parameters.setter
    def parameters(self, v): self._props_assign( "parameters", v)


    @property
    def meta_data(self): return self._prop.meta_data
    @meta_data.setter
    def meta_data(self, v): self._props_assign( "meta_data", v)
