"""
Filename      : ChannelBase.py
Date          : 2012/08/12
Version       : 0.0
Testing Class : none
Remarks       :
@author       : 25177612+vsanni@users.noreply.github.com
"""


from channel           import Channel
from container import Container
from jumble.type_extra import as_list
import numpy as np
from scipy.signal import _waveforms as wf

def steps(start, stop, step):

    return np.arange(0,int((stop-step)/step)+0.5+1)*step+start


def gaussian_peak(T=6.0, dt =.001, t0=-3.0,
                  t1            = 0.0,
                  sigma_t       = 1.0,
                  x0            = 1/np.sqrt(2.0*np.pi),
                  x1            = 0.0,
                  sigma_x_noise = 0.0,
                  names         = ["time"        , "gaussian_peak" ],
                  unitss        = ["s"           , "AU"            ],
                  descriptions  = ["elapsed time", "Gaussian Peak" ],
                  symbols       = ["t"           , "A"             ]
                  ):

    t = np.arange(0,T,dt)+t0
    N = t.size

    x1 += (0.0 if sigma_x_noise  == 0.0 else np.random.normal(0.0, sigma_x_noise, N))

    x = x0 * np.exp( -0.5*((t-t1)/sigma_t)**2 ) + x1

    parameters = Container(t1            = t1,
                           sigma_t       = sigma_t,
                           x0            = x0,
                           x1            = x1,
                           sigma_x_noise = sigma_x_noise,
                           )

    return  Channel( (t0, dt), x,
                    names          = names,
                    unitss         = unitss,
                    symbols        = symbols,
                    descriptions   = descriptions,
                    parameters     = parameters
                   )



def random_normal(T=.1, dt =.0001, t0=0.0, mu=0.0, sigma=1,
                  names        = ["time"        , "norm_rand"     ] ,
                  unitss       = ["s"           , "AU"            ],
                  descriptions = ["elapsed time", "Gaussian Noise"],
                  symbols      = ["t"           , "x"             ]
                  ):

    t = np.arange(0,T,dt)+t0
    x = np.random.normal(mu, sigma, t.size)

    return  Channel((t0, dt), x,
                    names          = names,
                    unitss         = unitss,
                    symbols        = symbols,
                    descriptions   = descriptions,
                    parameters     = Container(mu=mu, sigma=sigma))



def _noise_periodic_function(N, x0=1.0, phi=0.0, x1=0.0, sigma_x0_noise=None, sigma_phi_noise=None, sigma_x1_noise=None):

    X0  = x0  + (0.0 if sigma_x0_noise  == 0.0 else np.random.normal(0.0,  sigma_x0_noise, N))
    Phi = phi + (0.0 if sigma_phi_noise == 0.0 else np.random.normal(0.0, sigma_phi_noise, N))
    X1  = x1  + (0.0 if sigma_x1_noise  == 0.0 else np.random.normal(0.0,  sigma_x1_noise, N))

    return X0, Phi, X1




def sinusoid(T=1.0, dt =.001, t0=0.0,
             f=10, x0=1.0, phi=0.0, x1=0.0,
             sigma_x0_noise=0.0, sigma_phi_noise=0.0, sigma_x1_noise=0.0,
             names        = ["time"        , "sinusoid"    ],
             unitss       = ["s"           , "AU"          ],
             descriptions = ["elapsed time", "Sinusoid Amp"],
             symbols      = ["t"           , "A"           ]
             ):

    t = np.arange(0,T,dt)+t0

    common =  Container(x0              = x0             ,
                        phi             = phi            ,
                        x1              = x1             ,
                        sigma_x0_noise  = sigma_x0_noise ,
                        sigma_phi_noise = sigma_phi_noise,
                        sigma_x1_noise  = sigma_x1_noise)

    X0, Phi, X1 = _noise_periodic_function(N=t.size, **common )

    X           = X0*np.sin(2.0*np.pi*f*t + Phi) + X1


    return  Channel( (t0, dt), X,
                    names          = names,
                    unitss         = unitss,
                    symbols        = symbols,
                    descriptions   = descriptions,
                    parameters     = common
                   )



def comb(T=1.0, dt =.001, t0=0.0,
         f=[5, 10, 15], x0=1.0, phi=0.0, x1=0.0,
         sigma_x0_noise=0.0, sigma_phi_noise=0.0, sigma_x1_noise=0.0,
         names        = ["time"        , "comb"        ],
         unitss       = ["s"           , "AU"          ],
         descriptions = ["elapsed time", "Comb Amp"    ],
         symbols      = ["t"           , "A"           ]
        ):

    t = np.arange(0,T,dt)+t0
    f = np.asarray(as_list(f))
    C = t.size
    R = f.size

    if phi is None: phi = np.random.uniform(0.0, 2*np.pi, R)
    if x1  is None: x1  = np.random.uniform([-1.0, 1.0] , R)
    if x0  is None: x0  = np.random.uniform(0.5, 1.0    , R)

    common =  Container(x0              = x0             ,
                        phi             = phi            ,
                        x1              = x1             ,
                        sigma_x0_noise  = sigma_x0_noise ,
                        sigma_phi_noise = sigma_phi_noise,
                        sigma_x1_noise  = sigma_x1_noise)

    X0, Phi, X1 = _noise_periodic_function(N =(C,R) ,**common)

    X           = X0*np.sin(2.0*np.pi*t[:,np.newaxis]*f + Phi) + X1

    return  Channel((t0, dt), X.sum(axis=1),
                    names          = names,
                    unitss         = unitss,
                    symbols        = symbols,
                    descriptions   = descriptions,
                    parameters   = common
                   )



def chirp(T=10, dt =.0001, t0=0.0,
          form="linear", f0=1,f1=10, vertex_zero=True, DT=10, x0=1.0, phi=0.0, x1=0.0,
          sigma_x0_noise=0.0, sigma_phi_noise=0.0, sigma_x1_noise=0.0,
          names        = ["time"        , "chirp"       ],
          unitss       = ["s"           , "AU"          ],
          descriptions = ["elapsed time", "Chirp Amp"   ],
          symbols      = ["t"           , "A"           ]
         ):

    t = np.arange(0,T,dt)+t0

    common =  Container(x0              = x0             ,
                        phi             = phi            ,
                        x1              = x1             ,
                        sigma_x0_noise  = sigma_x0_noise ,
                        sigma_phi_noise = sigma_phi_noise,
                        sigma_x1_noise  = sigma_x1_noise)

    X0, Phi, X1 = _noise_periodic_function(N=t.size, **common )

    phase       = wf._chirp_phase(t, f0, DT, f1, method=form, vertex_zero=True)

    X           = X0*np.sin(phase + Phi) + X1

    return  Channel((t0, dt), X,
                    names          = names,
                    unitss         = unitss,
                    symbols        = symbols,
                    descriptions   = descriptions,
                    parameters   = Container(form = form, f0 = f0, f1 = f1, DT = DT, vertex_zero=vertex_zero, **common)
                    )


def _pulse_period(t, dt=0.01, DT=1.0, dTr=0.1, dT=.4, dTs = 0.1):

    t -= t[0]

    t2 = DT-dTs
    t1 = DT-dT-dTs
    t0 = DT-dTr-dT-dTs

    X   = np.zeros_like(t)

    N = np.where((t0 <= t) & (t <t1))[0]
    if N != []:
        X[N] = (t[N]-t[N[0]])/(t1-t0)
        if N != []:
            N     = np.where((t1 <= t) & (t <t2))[0]
            X[N ] = 1.0
        if N != []:
            N    = np.where((t2 <= t) & (t <DT))[0]
            X[N] = 1 + (t[N]-t[N[0]])/(t2-DT)

    return X



def _pulse(t, dt=0.01, DT=1.0, dTr=0.1, dT=.4, dTs = 0.1):

    X = np.zeros_like(t)

    N = int(DT/dt)

    for n0 in range(0,t.size,N):
        n1       = min(n0+N,t.size)
        X[n0:n1] = _pulse_period(t[n0:n1], dt=dt, DT=DT, dTr=dTr, dT=dT, dTs=dTs)

    return X



def pulse(T=1, dt =.001, t0=0.0,
          DT=1, dTr=0.1, dT=.4, dTs = 0.1, x0=1.0, phi=0.0, x1=0.0,
          sigma_x0_noise=0.0, sigma_t_noise=0.0, sigma_x1_noise=0.0,
          names        = ["time"        , "pulse"       ],
          unitss       = ["s"           , "AU"          ],
          descriptions = ["elapsed time", "pulse Amp"   ],
          symbols      = ["t"           , "A"           ]
         ):

    common = Container(DT=DT, dt=dt, dTr=dTr, dT=dT, dTs=dTs)

    N  = int(T/dt)
    X0 = x0 + (0.0 if sigma_x0_noise  == 0.0 else np.random.normal(0.0, sigma_x0_noise, N))
    X1 = x1 + (0.0 if sigma_x1_noise  == 0.0 else np.random.normal(0.0, sigma_x1_noise, N))

    if sigma_t_noise  == 0.0:
        X = _pulse_period(np.arange(0, DT, dt), **common)
        X = np.tile(X,int(T/DT)+1)
        X = X0*X[:N]+X1

    else:
        t = np.arange(0,T,dt) +np.random.normal(0.0, sigma_t_noise, N)
        X = X0*_pulse(t, **common)+X1

    return  Channel((t0, dt), X,
                    names          = names,
                    unitss         = unitss,
                    symbols        = symbols,
                    descriptions   = descriptions,
                    parameters   = Container(x0             = x0             ,
                                             phi            = phi            ,
                                             x1             = x1             ,
                                             sigma_x0_noise = sigma_x0_noise ,
                                             sigma_x1_noise = sigma_x1_noise ,
                                             sigma_t_noise  = sigma_t_noise  ,
                                             **common)
                   )
