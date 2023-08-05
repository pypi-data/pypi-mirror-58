__author__ = 'AR & AA'

import os
import numpy as np
from _Cosmics import cosmics

class RecombinationCosmics:
    """
    Compute recombination and thermodynamic variables as a function of redshift. This is for debugging purposes
    and is done by reading an output file from COSMICS.
    """

    def __init__(self,params,cosmo):

        # initialise
        self._params = params

        # call RECFAST++ to compute reionisation history tables
        print('Reading COSMICS recombination file')

        # TODO: change path to avoid it being relative to recomb class
        # TODO: may want to change config file to give file name as opposed to a directory
        tab_cosmics = cosmics(os.path.join(os.path.dirname(__file__), self._params.recomb_dir))

        self.eta=tab_cosmics.eta_th   # conformal time [h^-1 Mpc]
        # TODO: use internal pycosmo routines to convert eta into a rather than COSMICS tables
        aa=np.logspace(np.log10(1e-4), np.log10(1.), 500)
        etaa=cosmo.background._eta_a(aa)
        self.a=np.interp(self.eta, etaa, aa) # scale factor [1]
        # TODO: check sign for taudot
        self.taudot = -tab_cosmics.opaca2_th / tab_cosmics.h / self.a**2  # taudot=dtau/deta [h Mpc^-1]
        self.cs2=tab_cosmics.cs2_th  # baryon sound speed squared [1]
        self.tm=tab_cosmics.tempb_th   # Baryon (matter) temperature [K]

    def taudot_a(self,a):
        """
        Returns tau_dot=d(tau)/d(eta) where tau is the optical depth and eta is the conformal time
        as a function of the scale factor a
        :param a: scale factor [1]
        :return : tau_dot: conformal time derivative of the optical depth [h Mpc^-1]
        """
        # TODO: check for out of bound interpolations
        #return -np.interp(a, self.a[::-1], self.taudot[::-1] * self.a[::-1]**2) / a**2 # tau_dot [h Mpc^-1]
        return np.interp(a, self.a, self.taudot * self.a**2) / a**2 # tau_dot [h Mpc^-1]

    def cs_a(self, a):
        """
        Returns the baryon sound speed as a function of the scale factor a
        :param a: scale factor [1]
        :return : cs: baryon sound speed [1]
        """

        # TODO: check for out of bound interpolations
        return np.sqrt(np.interp(a, self.a, self.cs2 * self.a) / a )   # sound speed [1]

    def tm_a(self, a):
        #TODO: should probably rename this temperature as Tb
        """
        Return the Baryon (matter) temperature as a function of the scale factor a,
        by interpolating (or extrapolating for early times) the recombination tables.
        :param a: scale factor [1]
        :return: Baryon (matter) temperature Tm [K]
        """

        print 'ERROR: tm_a for COSMICS not implemented'
        return 0.

    def mu_a(self,a):
        """
        Computes the dimensonless mean molecular weight. It can be multiplied by the hydrogen atom mass to express it in mass units.
        :param a: a - scale factor [1]
        :return: mu: dimensionless mean molecular weight [1] (multiply bu the hydrogen atom mass to express in units of
        """
        
        print 'ERROR: mu_a for COSMICS not implemented'
        return 0.

