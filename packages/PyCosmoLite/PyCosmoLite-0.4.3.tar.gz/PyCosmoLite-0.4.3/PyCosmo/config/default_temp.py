"""
Updated 29th June
by Federica Tarsitano
"""
import collections
import sympy as sp
from . import Parameter

# Cosmology Input Parameters
# = Parameter(val = , symbol = sp.symbols(''), txt = '', unit = ' ' )
#--------------------

h = Parameter(val = 0.7, symbol = sp.symbols('h'),
              txt = 'dimensionless Hubble constant; Hubble constant H0 = h*100km/s/Mpc', unit = '[1]' )

omega_b = Parameter(val = 0.045, symbol = sp.symbols('\Omega_b'),
                    txt = 'Baryon density parameter (z=0)', unit = '[1]' )

omega_m = Parameter(val = 0.3, symbol = sp.symbols('\Omega_m'),
                    txt = 'Matter density paramater (dark matter + baryonic matter)', unit = '[1]' )

omega_l_in = Parameter(val = 'flat', symbol = sp.symbols('\Omega_\Lambda'),
                       txt = 'Dark energy density. If flat then omega_l is 1.- omega_m - omega_r', unit = ' [1]' )

w0 = Parameter(val = -1.0, symbol = sp.symbols('w_0'),
               txt = 'DE equation of state at z=0', unit = '[1]' )

wa = Parameter(val = 0.0, symbol = sp.symbols('w_a'),
               txt = 'DE equation of state evolution such that w(a)=w0+wa(1-a)', unit = '[1] ' )

n = Parameter(val = 1.0, symbol = sp.symbols('n'),
              txt = 'Spectral index for scalar modes', unit = '[1] ' )

tau = Parameter(val = 0.09 , symbol = sp.symbols('\tau'),
                txt = 'Optical depth [under development]', unit = ' ??' )

pk_norm_type= Parameter(val = 'sigma8', symbol = sp.symbols('norm_{type}'),
                        txt = 'Power spectrum normalisation scheme: deltah for CMB normalisation or sigma8 for sigma8 normalisation', unit = ' ' )

pk_norm = Parameter(val = 0.8, symbol = sp.symbols('norm'),
                    txt = 'Power spectrum normalisation value: either deltah or sigma8 depending on pk_norm_type setting', unit = ' ' )

deltah = Parameter(val = 4.6e-5, symbol = sp.symbols('\Delta h'),
                   txt = 'Powerspectrum Normalisation (early time)', unit = ' ')

Yp = Parameter(val = 0.24, symbol = sp.symbols('Yp'),
               txt = 'Helium fraction [under development]', unit = '[1]')

Tcmb = Parameter(val = 2.725, symbol = sp.symbols('T_{cmb}'),
                 txt = 'CMB temperature', unit = '[K]' )

Nnu = Parameter(val = 3.04, symbol = sp.symbols('N_\nu'),
                txt = 'Number of effective massless neutrino species [under development]', unit = '[1]')

F = Parameter(val = 1.14, symbol = sp.symbols('F'), txt = '?? [under development]', unit = ' ??' )

fDM = Parameter(val = 0.0, symbol = sp.symbols('fDM'), txt = '??? [under development]', unit = '?? ' )

# Parameters used for numerics
#--------------------

aini = Parameter(val = 1.0e-7, symbol = sp.symbols('a_{ini}'),
                 txt = 'a used as initial starting point for Boltzman calculation', unit = ' ')

intamin = Parameter(val = -1, symbol = sp.symbols('int(a)_{min}'),
                    txt = 'mininum a value used for the interpolation routines (-1 sets to aini/1.1)', unit = ' ')

intamax = Parameter(val = 1.0, symbol = sp.symbols('int(a)_{MAX}'),
                    txt = 'maximum a value used for the interpolation routines', unit = ' ')

intnum = Parameter(val = 100, symbol = sp.symbols('int\_num'),
                 txt = 'number of points ussed in interpolation', unit = ' ')

speed = Parameter(val = 'slow', symbol = sp.symbols('speed'),
                 txt = 'fast (interpolations used) or slow - full calcs', unit = ' ')

recomb = Parameter(val = '---', symbol = sp.symbols('recomb'),
                 txt = 'code to compute recombination: "recfast++" or "cosmics"', unit = ' ')

cosmics_dir = Parameter(val = '---', symbol = sp.symbols('cosmics_dir'),
                 txt = 'COSMICS directory for recombination', unit = ' ')

pk_type = Parameter(val = 'EH', symbol = sp.symbols('pk_type'),
                 txt = 'sets is the linear perturbations should be calculated using boltzman solver ("boltz") or approximations ("approx")', unit = ' ')

pk_nonlin_type = Parameter(val = 'halofit', symbol = sp.symbols('pk_nonlin_type'),
                 txt = 'sets if the nonlinear matter power spectrum should be calculated using the halofit fitting function ("halofit") '
                       'or the revised halofit fitting function ("rev_halofit")', unit = ' ')

tabulation = Parameter(val = True, symbol = sp.symbols('tabulation'),
                 txt = 'sets if cosmological observables should be computed using the tabulated power spectra (True) '
                       'or the non tabulated power spectra (False)', unit = ' ')

tabulation = Parameter(val = True, symbol = sp.symbols('tabulation'),
                 txt = 'sets if cosmological observables should be computed using the tabulated power spectra (True) '
                       'or the non tabulated power spectra (False)', unit = ' ')

