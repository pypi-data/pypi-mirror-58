__author__ = 'AR & AA'

import os
import numpy as np

class RecombinationClass:
    """
    Compute recombination and thermodynamic variables as a function of redshift. This is for debugging purposes
    and is done by reading an output file from CLASS.
    """

    def __init__(self,params):

        # initialise
        self._params = params

        # call RECFAST++ to compute reionisation history tables
        print('Reading CLASS recombination file')

        # TODO: ensure a range is not outside CLASS table
        # TODO: to be safer use h values from class rather than from PyCosmo
        # TODO: change path to avoid it being relative to recomb class
        # TODO: may want to change config file to give file name as opposed to a directory
        tab_class = np.loadtxt(os.path.join(os.path.dirname(__file__), self._params.recomb_dir) +
                               'test_thermodynamics.dat')
        self.z = tab_class[:, 0]  # z [1]
        self.a = 1./(1. + self.z)  # a [1]
        self.eta = tab_class[:, 1] * self._params.h  # eta [h^-1 Mpc]
        self.taudot = tab_class[:, 3] / self._params.h  # -taudot [h Mpc^-1]
        self.cs2 = tab_class[:, 7]  # baryon sound speed squared [1]


    def taudot_a(self,a):
        """
        Returns tau_dot=d(tau)/d(eta) where tau is the optical depth and eta is the conformal time
        as a function of the scale factor a
        :param a: scale factor [1]
        :return : tau_dot: conformal time derivative of the optical depth [h Mpc^-1]
        """

        # TODO: check for out of bound interpolations
        return -np.interp(a, self.a[::-1], self.taudot[::-1] * self.a[::-1]**2) / a**2 # tau_dot [h Mpc^-1]

    def cs_a(self, a):
        """
        Returns the baryon sound speed as a function of the scale factor a
        :param a: scale factor [1]
        :return : cs: baryon sound speed [1]
        """
        # TODO: check for out of bound interpolations
        return np.sqrt( np.interp(a, self.a[::-1], self.cs2[::-1] * self.a[::-1]) / a )   # sound speed [1]


    def tm_a(self, a):
        #TODO: should probably rename this temperature as Tb
        """
        Return the Baryon (matter) temperature as a function of the scale factor a,
        by interpolating (or extrapolating for early times) the recombination tables.
        :param a: scale factor [1]
        :return: Baryon (matter) temperature Tm [K]
        """

        print('ERROR: tm_a for CLASS not implemented')
        return 0.

    def mu_a(self,a):
        """
        Computes the dimensonless mean molecular weight. It can be multiplied by the hydrogen atom mass to express it in mass units.
        :param a: a - scale factor [1]
        :return: mu: dimensionless mean molecular weight [1] (multiply bu the hydrogen atom mass to express in units of
        """

        print('ERROR: mu_a for CLASS not implemented')
        return 0.

