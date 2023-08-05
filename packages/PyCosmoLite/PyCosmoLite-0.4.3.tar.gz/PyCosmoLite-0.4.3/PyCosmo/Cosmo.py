# Copyright (C) 2014 ETH Zurich, Institute for Astronomy
#
# System imports
from __future__ import absolute_import, division, print_function

import os

import dill
import numpy as np

import PyCosmo
from PyCosmo import load_configs
from PyCosmo.Background import Background
if 0:
    from PyCosmo.BoltzmannSolver.LinearPerturbation import \
        LinearPerturbation as LinearPerturbationBoltz
from PyCosmo.LinearPerturbationApprox import LinearPerturbationApprox
# TODO: Tables -> think about interface
from PyCosmo.LinearPerturbationTable import LinearPerturbationTable
from PyCosmo.NonLinearPerturbationHaloFit import NonLinearPerturbationHaloFit
from PyCosmo.NonLinearPerturbationMead import NonLinearPerturbationMead
from PyCosmo.NonLinearPerturbationTable import NonLinearPerturbationTable
from PyCosmo.Projection import Projection
from PyCosmo.TheoryPredTables import TheoryPredTables

from .v2_config import _input_options

_SPEED_OF_LIGHT = 299792.458  # [km/s]
_BOLTZMANN_CONSTANT = 8.6173303e-5  # [eV/K]
_PROTON_MASS = 938.2720813  # [MeV/c**2]
_THOMSON_CROSS_SECTION = 6.6524587158e-29  # [m**2]
_GRAVITATIONAL_CONSTANT = 6.67408e-11  # [m^3/kg/s^2]
_MEGAPARSEC = 3.085677581491367e22  # [m]
_SOLAR_MASS = 1.98848e30  # [kg]
_EV_BY_CSQUARE = 1.782661907e-36  # [kg] - eV/c^2
_H_BAR = 6.582119514e-16  # eV s


HERE = os.path.dirname(os.path.abspath(__file__))


class Cosmo(object):
    """
    PyCosmo is a multi-purpose cosmology calculation tool. It is designed
    to be interactive and user friendly.
    The code includes calculations of:
          + Background
          + Linear perturbations (incl. Boltzmann solver in development)
          + Non-linear perturbations
          + Series of observables (e.g WL powerspectrum, SNe Hubble diagramme, cluster counts etc.)
          + Forecasting tools (e.g. Fisher analyses)
    All of these functionalities are managed by the main (cosmo) class, which links the users in an easy
    with the other classes where the bulk of the calculations are performed.

    :param paramfile: input paramater file name (if not provided the default file PyCosmo/config/default.py will be used)
    """

    _DEFAULT_PARAM_FILE = "PyCosmo.config.default_v2"

    def __init__(self, paramfile=None):
        """Initiates the cosmo class
        :param paramfile:
        """
        if paramfile is None:
            print("Parameter file not supplied. Using default")
            paramfile = self._DEFAULT_PARAM_FILE

        self.paramfile = paramfile
        params = load_configs.loadConfigs(paramfile)
        self.nb_objects = load_configs.extract_code(
            os.path.join(HERE, "CosmologyCore.ipynb")
        )
        self._reset(params)

    def set(self, **kwargs):
        """
        Changes the configuration parameters of the PyCosmo instance. This will also recalculate the derived quantities.

        .. Warning :: Always change parameters of an instance of PyCosmo using the set function. Do not change variables directly

        :param kwargs: keyword arguments for the input parameters to change.
        :return: if no keywords are passed then a list of options is printed

        Example:

        .. code-block:: python

            cosmo.set(omega_m=0.23)

        """

        params = self.params
        for key in kwargs.keys():
            assert key in _input_options, (
                "%s is not a parameter option, please use: %s" % (key, _input_options)
            )
            setattr(params, key, kwargs[key])
        self._reset(params)
        if len(kwargs) == 0:
            print("Current status:")
            self.print_params(inc_consts=False, inc_num=True)
            print("")
            print("Input options: %s" % _input_options)
        # else:
        #    print("Parameters updated")

    def _reset(self, params):
        """
        Rests the internal data in the instance

        :param paramfile: (optional) the name of the param file to use.
        """

        self._enrich_params(params)

        self.params = params

        recomb = self.params.recomb

        if recomb == "recfast++":
            # print("Recombination set to Recfast++")
            from PyCosmo._Recombination import Recombination

            self.rec = Recombination(self.params)
        elif recomb == "class":
            # print("Recombination set to CLASS")
            from PyCosmo._RecombinationClass import RecombinationClass

            self.rec = RecombinationClass(self.params)
        elif recomb == "cosmics":
            # print("Recombination set to COSMICS")
            from PyCosmo._RecombinationCosmics import RecombinationCosmics

            self.rec = RecombinationCosmics(self.params, self)
        elif recomb is None:
            # print("Ignoring recombination.")
            self.rec = None
        else:
            raise ValueError("invalid value '{}' for recombination".format(recomb))

        self.background = Background(self.params, self.rec, self.nb_objects)

        # selectiong the way that linear perturbations are calculated
        if params.pk_type == "EH" or params.pk_type == "BBKS":
            self.lin_pert = LinearPerturbationApprox(self.params, self.background)
        elif params.pk_type == "boltz":
            raise NotImplementedError()
            self.lin_pert = LinearPerturbationBoltz(
                self.params, self.background, self.nb_objects
            )
        else:
            # Todo raise an error
            self.lin_pert = None

        # TODO: remove duplicate ?
        self.lin_pert_tab = LinearPerturbationTable(self.lin_pert)

        if params.pk_nonlin_type == "halofit" or params.pk_nonlin_type == "rev_halofit":
            self.nonlin_pert = NonLinearPerturbationHaloFit(
                self.params, self.background, self.lin_pert
            )

        elif params.pk_nonlin_type == "mead":
            self.nonlin_pert = NonLinearPerturbationMead(
                self.params, self.background, self.lin_pert
            )

        else:
            raise ValueError(
                'unknown pk_nonlin_type "{}"'.format(params.pk_nonlin_type)
            )

        # TODO: what about runtime here ? move to "if params.tabulation" branch below ?
        self.lin_pert_tab = LinearPerturbationTable(self.lin_pert)
        self.nonlin_pert_tab = NonLinearPerturbationTable(self.nonlin_pert, params)
        #
        # TODO: Tables -> do we want two projections or do we set which one we want?
        if params.tabulation:
            self.projection = Projection(
                self.params, self.background, self.lin_pert_tab, self.nonlin_pert_tab
            )
        else:
            self.projection = Projection(
                self.params, self.background, self.lin_pert, self.nonlin_pert
            )

    # TODO: use constants, no magic numbers
    # TODO: tidy up. remove commented stmts
    def _enrich_params(self, params):
        """
        Setting basic constants and some derived quantities
        Initialising the basic cosmological parameters
        """

        # set constants
        params.c = _SPEED_OF_LIGHT
        params.kb = _BOLTZMANN_CONSTANT
        params.mp = _PROTON_MASS
        params.sigmat = _THOMSON_CROSS_SECTION
        params.G = _GRAVITATIONAL_CONSTANT
        params.mpc = _MEGAPARSEC
        params.msun = _SOLAR_MASS
        params.evc2 = _EV_BY_CSQUARE
        params.hbar = _H_BAR

        # params.pk_norm = None   # powerspectrum normalisation not set (will be set by sigma8)
        # params.gamma = None # Powerspectrum turn is not set (will be set later once needed)

        # TODO: need to remove nudges at some point
        # nudges introduced to match boltzmann codes - for debugging purposes only
        # nudge=[1.-1.50298573522e-5/2.,1.-5.56498919433e-05,1.-2.53353919555e-06]  # to agree with cosmics code
        # nudge=[1.,1.,1.]  # no nudge

        if not "cosmo_nudge" in params.keys():
            nudge = [1., 1., 1.]  # no nudge
        else:
            nudge = params.cosmo_nudge

        if not nudge == [1., 1., 1.]:
            print(
                "Warning: nudges to H0, omega_gamma, omega_neu introduced - for debugging purposes only"
            )
        params.H0 = 100.0 * params.h * nudge[0]  # Hubble constant [km/s/Mpc]
        # TODO: check units for rh
        params.rh = (
            params.c / params.H0 * params.h
        )  # Hubble radius (=c/H0) at z=0 [h^-1 Mpc]
        # critical density at z=0 [h^2 M_sun Mpc^-3]
        params.rho_crit = (
            3.
            * params.H0 ** 2
            / (8. * np.pi * params.G)
            * 1e6
            * params.mpc
            / params.msun
            / params.h ** 2
        )
        # TODO: check omega_gamma and omega_neu expressions
        # omega_photon (see Dodelson eq. 2.70) ** express in terms of H0? **)
        # params.omega_gamma = 2.470109245e-5 * (params.Tcmb / 2.725)**4 / params.h**2 * nudge[1]
        params.rho_gamma_eV = (
            (3 * 100 ** 2 / (8 * np.pi * params.G))
            * params.hbar ** 3
            * (1 / (params.mpc * 1e-3)) ** 2
            * (1 / (params.evc2))
            * (params.c * 1e3) ** 3
        )
        params.omega_gamma_prefactor = (
            np.pi ** 2 / 15 * (2.725 * params.kb) ** 4 / (params.rho_gamma_eV)
        )
        params.omega_gamma = (
            params.omega_gamma_prefactor
            * (params.Tcmb / 2.725) ** 4
            / params.h ** 2
            * nudge[1]
        )
        params.omega_neu = (
            params.Nnu
            * 7.
            / 8.
            * (4. / 11.) ** (4. / 3.)
            * params.omega_gamma
            * nudge[2]
        )  # omega for massless neutrino
        params.omega_r = params.omega_gamma + params.omega_neu  # omega_radiation
        # print(params.omega_r)
        # params.omega_r = 0.0000

        # suppress_rad
        if params.suppress_rad:
            params.omega_r = 0.

        # fix some omega settings for special cases:

        if (
            params.omega_l_in == "flat"
        ):  # if False then set omega_l to give flat Universe
            params.omega_l = 1.0 - params.omega_m - params.omega_r
            params.omega_k = 0.0
            params.omega = 1.0  # total density (z=0)
        else:
            params.omega_l = params.omega_l_in
            params.omega = (
                params.omega_m + params.omega_r + params.omega_l
            )  # correct expression
            params.omega_k = 1.0 - params.omega

        if params.omega_suppress:
            params.omega = (
                1.
            )  # this ignores curvature - wrong but used by some codes which does not account for omega_r in omega
            params.omega_k = 0.
            params.omega_r = 0.
            # print(
            #     "Cosmo_add_constants: Warning: curvature suppressed - for testing purposes only"
            # )
            # TODO: curvature suppression perhaps needs to be removed at some point

        params.omega_dm = params.omega_m - params.omega_b  # DM density (z=0)
        if params.omega_k == 0.0:
            params.sqrtk = 1.0
        else:
            params.sqrtk = np.sqrt(abs(params.omega_k))

        if params.omega_r > 0.0:
            params.a_eq = params.omega_r / params.omega_m  # matter-radiation equality
            params.z_eq = 1. / params.a_eq - 1.
        else:
            params.a_eq = np.nan
            params.z_eq = np.nan

        # TODO: generalise a_eq2 to w<>-1
        if (
            params.omega_l > 0.0 and params.w0 == -1. and params.wa == 0.
        ):  # dark energy-matter equality - only valid for LCDM for now
            params.a_eq2 = (params.omega_m / params.omega_l) ** (1 / 3.)
            params.z_eq2 = 1. / params.a_eq2 - 1.
        else:
            params.a_eq2 = np.nan
            params.z_eq2 = np.nan

        if (params.w0 == -1.) and params.wa == 0.:
            params.cosmo_type = "LCDM"
        else:
            params.cosmo_type = "qCDM"

    def print_params(self, inc_consts=True, inc_num=True, inc_others=True):
        """
        Prints the parameters of PyCosmo instance.

        :param inc_consts: prints constants (True or False)
        :param inc_num: prints other cosmo input options (True or False)
        :param inc_others:  prints parameters for other classes (e.g. linearpert)
        """
        print("---- Cosmology parameters ----")
        print()
        print("h: Dimensionless hubble parameter [1]:", self.params.h)
        print("omega_b: Baryon density parameter [1]:", self.params.omega_b)
        print(
            "omega_m: Matter density parameter (DM+baryons) [1]:", self.params.omega_m
        )
        print("omega_l_in: Dark Energy density parameter [1]:", self.params.omega_l)
        print("w0: Dark Energy eq. of state parameter at z=0 [1]:", self.params.w0)
        print("wa: Dark Energy eq. of state evolution [1]:", self.params.wa)
        print("Tcmb: CMB temperature [K]:", self.params.Tcmb)
        print("n: Scalar spectral index [1]:", self.params.n)
        print(
            "Nnu: number of massless neutrino species [under development] [1]:",
            self.params.Nnu,
        )
        print("Helium fraction (Yp) [1]", self.params.Yp)
        print("Optical depth (tau) [1]:", self.params.tau)
        print("powerspectrum Norm type:", self.params.pk_norm_type)
        print("powerspectrum Norm value:", self.params.pk_norm)
        print("powerspectrum type:", self.params.pk_type)
        print("nonlinear powerspectrum type:", self.params.pk_nonlin_type)

        if inc_consts is True:
            print()
            print("---- Constants and derived quantities ----")
            print()
            print("Speed of light (c) [km/s]:", self.params.c)
            print("Hubble constant (H0) [km/s/Mpc]:", self.params.H0)
            print("Hubble radius (rh) [Mpc/h]:", self.params.rh)
            print(
                "Critical Density (rho_crit) [h^2 M_sun/Mpc^3]:", self.params.rho_crit
            )
            print("Dark Matter density (omega_dm) [1]:", self.params.omega_dm)
            print("Photon density (omega_gamma) [1]:", self.params.omega_gamma)
            print("Neutrino density (omega_neu) [1]:", self.params.omega_neu)
            print("Curvature density (omega_k) [1]:", self.params.omega_k)
            print("Total density (omega) [1]:", self.params.omega)
            print(
                "Matter-radiation equality (a_eq,z_eq) [1,1]",
                self.params.a_eq,
                self.params.z_eq,
            )
            print(
                "Dark energy-radiation equality (a_eq2,z_eq2) [1,1]",
                self.params.a_eq2,
                self.params.z_eq2,
            )
            # print('Form factor for linear power spectrum (gamma) [1]:',self.params.gamma)

        if inc_num is True:
            print()
            print("---- Numerical settings ----")
            print()
            print("code to compute recombination:", self.params.recomb)
            print("recomb_dir:", self.params.recomb_dir)
            print("omega_suppress:", self.params.omega_suppress)
            print("suppress_rad:", self.params.suppress_rad)
            print(
                "nudge factors for H0, omega_gamma, and omega_neu [1,1,1]:",
                self.params.cosmo_nudge,
            )


        if inc_others is True:
            if hasattr(self, "lin_pert"):
                if hasattr(self.lin_pert, "print_params"):
                    self.lin_pert.print_params()


        recomb = self.params.recomb
        if recomb == "recfast++":
            print("Recombination set to Recfast++")

        elif recomb == "class":
            print("Recombination set to CLASS")

        elif recomb == "cosmics":
            print("Recombination set to COSMICS")

        elif recomb is None:
            print("Ignoring recombination.")



    def __getstate__(self):
        return dill.dumps(self.__dict__)

    def __setstate__(self, state):
        self.__dict__.update(dill.loads(state))
