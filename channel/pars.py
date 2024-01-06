"""
Filename      : pars.py
Date          : 2012/08/12
Testing Class : none
Remarks       :
@authors Virginio Sannibale
@email vsanni@sbcglobal.net
@version 0.0
@copyright Copyright 2007, Virginio Sannibale"
"""

__author__    = "Virginio Sannibale"
__copyright__ = "Copyright 2007, Virginio Sannibale"
__email__     = "vsanni@sbcglobal.net"
__version__   = "0.0"


from jumble.eprint import eprint

def expand(N, par):

    if not isinstance( par, tuple):
       exp_pars = [par]*N
    else:
        exp_pars = [None]*len(par)

        for i in range(0, len(par)):
            #print par[i],
            if isinstance(par[i], (int, float, complex, str) ) or par[i] is None:
                exp_pars[i] = [par[i]]*N
            elif ( len(par[i]) == N):
                exp_pars[i] = par[i]
            elif ( len(par[i]) == 1):
                if (type(par[i]) is list):
                   exp_pars[i] = par[i]*N
                else:
                   exp_pars[i] = [par[i]]*N

            else:
                eprint("\ninvalid length for the parameter %d, it must be 1 or the length %d as specified in the first parameter.\n" %(i, N))

    return tuple(exp_pars)



def compare(x, par, min_length=1, case_sensitive=False):

    if x is None or par is None: return False
    elif   case_sensitive       : return x == par[:max(min_length, len(x))]
    else                       : return x.lower() == par.lower()[:max(min_length, len(x))]



def compare_complete(x, par, min_length=1, case_sensitive=False):

    c = compare(x, par, min_length, case_sensitive)

    if c: x = par

    return c, x



def list_check_set_or_get(ModeList, CurMode, Mode=None):

    if Mode:
       for m in ModeList:
           if compare(Mode, m): return m

    elif Mode is None:
      return CurMode

    s = ''.join([ " '%s', " % s for s in ModeList[:-1]])

    eprint("\nExp.Aux.Mode: error, invalid mode '%s' specified, valid modes are:%s and '%s'.\n" % (Mode, s, ModeList[-1]))



def same(par, default_par=None):

    if par.count(par[0]) == len(par): return par[0]
    else                             : return default_par



def table_print(Format=['%14.3f', ' ', None], *v): #one of the most  useless function that took me so long to write

    rows = len(v[0])
    cols = len(v)

    header         = Format[2]
    Format, spaces = expand(cols, (Format[0], Format[1]))

    format_string = [ Format[j].strip() + spaces[j] for j in range(cols-1)]
    format_string.append(Format[cols-1])

    table_width = len(''.join([format_string[j] % v[j][0] for j in range(cols)]))

    if header:
        header_format = [ Format[j].strip()[0:3]+"s" + spaces[j] for j in range(cols-1)]
        header_format.append(Format[cols-1].strip()[0:3]+"s")


        print(''.join([header_format[j] % header[j] for j in range(cols)]))

        print('-'*table_width)

    for i in range(rows):
        print(''.join([format_string[j] % v[j][i] for j in range(cols)]))

    return table_width

#table_print(['%12.4f', "  ", ['a', 'b', 'c', 'e', 'd']], [1, 2, -3, 4, 5, 6], [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60])
#print
#table_print(['%15g', ' ', None], [1, 2, -3, 4, 5, 6], [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60])
