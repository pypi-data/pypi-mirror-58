# Copyright (C) 2014 ETH Zurich, Institute for Astronomy

'''
Created on Oct 1, 2014

author: jakeret
'''

# Cosmology Input Parameters
#--------------------

h = 0.7
"""dimensionless Hubble constant [1]"""

omega_b = 0.06
"""Baryon density parameter [1]"""

omega_m = 0.25
"""Matter density paramater (dark matter + baryons) [1]"""

omega_l = "flat"
"""Dark energy density. If 'flat' then omega_l is 1.- omega_m - omega_r [1]"""

w0 = -1.0
"""DE equation of state at z=0 [1]"""

wa = 0.0            
"""DE equation of state evolution such that w(a)=w0+wa(1-a) [1]"""

n = 1.0             
"""Spectral index for scalar modes [1]"""

tau = 0.09             
"""Optical depth [under development]"""

#pk_norm_type='deltah'
pk_norm_type='sigma8'
"""Power spectrum normalisation scheme: 'deltah' for CMB normalisation or 'sigma8' for sigma8 normalisation"""

#pk_norm = 4.6*10**-5    # deltah example
pk_norm=.8 # sigma8 example
"""Power spectrum normalisation value: either deltah or sigma8 depending on pk_norm_type setting"""

Tcmb = 2.725
"""CMB temperature [K]"""

Yp = 0.24            
"""Helium fraction [under development] [1]"""

Nnu = 3.            
"""Number of effective massless neutrino species [under development] [1]"""

F = 1.14             
"""??? [under development]"""

fDM = 0.0             
"""??? [under development]"""


# Parameters used for numerics
#--------------------

pk_type = 'EH'
"""sets is the linear perturbations should be calculated using boltzman solver ('boltz') or approximations ('EH' for Einstein and Hu or 'BBKS') """

pk_nonlin_type = 'halofit'
"""sets if the nonlinear matter power spectrum should be calculated using the halofit fitting function ('halofit') or the revised halofit fitting function ('rev_halofit') """


#intamin = -1.0
#"""mininum a value used for the interpolation routines (-1 sets to aini/1.1) [under development]"""

#intamax = 1.0
#"""maximum a value used for the interpolation routines [under development]"""

#intnum = 100
#""" number of points ussed in interpolation [under development]"""

#speed = "slow"
#"""fast (interpolations used) or slow - full calcs [under development]"""

recomb = "recfast++"
"""code to compute recombination: 'recfast++' or 'cosmics' or 'class' [under development; at present this is only used to build tables for Boltzmann calculations]"""

#TODO: fix this! use resources to resolve paths
recomb_dir = "not set"
"""COSMICS or CLASS directory for recombination [under development]"""

omega_suppress = True
""" suppress radiation contribution in omega total as is often done """

suppress_rad = True
""" suppress radiation contribution in omega total as is often done """


cosmo_nudge=[1.,1.,1.]
""" nudge factors for H0, omega_gam, and omega_neu to compare with other codes - set to [1.,1.,1.] or leave out to suppress nudge"""

tabulation = True
"""sets if cosmological observables should be computed using the tabulated power spectra (True) or the non tabulated power spectra (False)"""

# Boltzmann Solver parameters
#--------------------

table_size = 2000
"""defines the interpolation size of the quatities cs**2, eta and taudot"""

l_max = 50
"""tbd: angular trancation limit """

lna_0 = None
"""tbd, if not passed it automatically calculated by the initial conditions """

y_0 = None
"""tbd, if not passed it automatically calculated by the initial conditions """

initial_conditions = "class"
"""initial_conditions: (optional) initial conditons to use. Allowed values are:
    cosmics: tbd
    class: tbd
    camb: tbd
"""

lna_max = None
"""t_end as log of redshift a (if none of them is passed, lnamax=0. is assumed)"""

econ_max = 3e-4
"""sets the maximum econ error for the boltzmann solver. If the econ exeeds this limit, the timestep is reduced"""

econ_ratio = 10
"""the ratio between the maximum econ and the minimum econ. The solver increases the timestep if econ is smaller than
the econ_max / econ_ratio"""

dt_0 = 1.5e-2
"""the initial timestep size. np.sqrt(econ_max) is normally a good guess"""

halflife = 0.1
""" the econ is calculated as a running mean: recon = (recon * (halflife - dt) + dt * abs(econ)) / halflife """

courant = [10., 1.]
"""scale parameter for the timescale [a * H / k,  eta * a * H] """

equations = "newtonian_lna"
"""equationset to choose"""

max_trace_changes = 999
"""limits the number of trace changes, reduces c code generation, might sacrifice stability, a
value 1 is often sufficient."""

sec_factor = 10.0
"""always pivote if it swapped numbers differ by sec_factor or more"""

trace_changes_log_file = ""
"""if this is a path and not an empty string the created c solver will track trace changes
to this file. Usually only used for internal uses"""

traces_folder = ""
"""use different folder for writing and reading traces. if not set default folder within
PyCosmo is used"""

cache_folder = ""
"""use different folder for writing and reading c code and compiled solver. if not set default
folder within PyCosmo is used"""
