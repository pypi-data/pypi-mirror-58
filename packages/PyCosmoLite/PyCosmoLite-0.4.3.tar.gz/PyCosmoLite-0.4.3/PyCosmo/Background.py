
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import dill
import hope
import numpy as np
from scipy import integrate

from PyCosmo import _derivs_boltz_hope, _Util
from PyCosmo.symbols import symbols as S

from ._sympy_helpers import compile_nbo_eq


def __intg_qevol_hope(y, a, w0, wa):
    w_a = w0 + (1.0 - a) * wa
    return -3.0 * (w_a + 1.0) / a

# _intg_qevol_hope = hope.jit(__intg_qevol_hope)
_intg_qevol_hope = __intg_qevol_hope


class Background(object):
    """
    The background calculations are based on a Friedmann-Robertson-Walker model, where
    the evolution is governed by the Friedmann equation.
    """

    # The first part contains the functions that deal with the elements of the Friedmann equation.
    # In particular the focus in the Hubble function
    # In the PyCosmo notes, this is section 1.2

    def __init__(self, params, rec, nb_objects):
        self._params = params
        self._rec = rec
        self.nbo = nb_objects
        self._compile_functions()

    def __getstate__(self):
        dd = self.__dict__.copy()
        for name in ("h_func", "chi_func"):
            del dd[name]
        nbo = dill.dumps(self.nbo)
        del dd["nbo"]
        return (nbo, dd)

    def __setstate__(self, data):
        nbos, dd = data
        self.nbo = dill.loads(nbos)
        self.__dict__.update(dd)
        self._compile_functions()

    def _compile_functions(self):
        c = compile_nbo_eq
        self.h_func = c(self.nbo, "H", S.H_0, S.omega_r, S.omega_m, S.omega_k, S.omega_l, S.a)
        self.chi_func = c(self.nbo, "chi", S.H_0, S.omega_r, S.omega_m, S.omega_k, S.omega_l, S.a)

    #########################################################
    #  A series of functions for calculating                #
    #  the Hubble function:                                 #
    #########################################################

    def H_a(self, a=1.0):
        """
        This calculates the Hubble parameter for a given scale factor a

        :param a: scale factor [1]
        :return: hubble parameter [km/s/Mpc]
        """
        a = np.atleast_1d(a)
        return self._hubble(a)

    # H(a) [km/s/Mpc]   ** ar version to gain speed - warning: factor of h's and only valid for
    # w=-1
    def _hubble(self, a):
        if self._params.cosmo_type == 'LCDM':
            # TODO: use this ...
            # from BoltzmannSolver.generator.k_5.k_5 import H
            # H_0 = 1 / self._params.rh
            # omegas = [self._params.omega_k, self._params.omega_r, self._params.omega_m, self._params.omega_gaam,
            #           self._params.omega_neu, self._params.omega_l, self._params.omega_b, self._params.omega_dm]
            # hub = H(*[float(np.exp(buffers["lna"][1])), float(buffers["lna"][1]), self.tables.lna, self.tables.cs2,
            #          self.tables.eta, self.tables.taudot, len(self.tables.lna), H_0] + omegas)
            hub = self._params.H0 * (self._params.omega_r * a**(-4)
                                     + self._params.omega_m * a**(-3)
                                     + self._params.omega_k * a**(-2)
                                     + self._params.omega_l)**0.5
        else:
            # Return the Hubble function at specified a [[km/s/Mpc]
            hub = np.sqrt(self._H2_H02_a(a=a)) * self._params.H0
        return hub

    # H(a) [km/s/Mpc]   ** ar version to gain speed - warning: factor of h's and only valid for w=-1
    def _hubble_new(self, a):
        if self._params.cosmo_type == 'LCDM':
            a = np.atleast_1d(a)
            hub = self.h_func(self._params.H0, self._params.omega_r, self._params.omega_m,
                              self._params.omega_k, self._params.omega_l, a[0])
        else:
            # Return the Hubble function at specified a [[km/s/Mpc]
            hub = np.sqrt(self._H2_H02_a(a=a)) * self._params.H0
        return hub

    def _H2_H02_a(self, a=1.0):
        return (self._H2_H02_Omegar_a(a=a)
                + self._H2_H02_Omegam_a(a=a)
                + self._H2_H02_Omegak_a(a=a)
                + self._H2_H02_Omegal_a(a=a))

    def _H2_H02_Omegar_a(self, a=1.0):
        return self._params.omega_r / a**4

    def _H2_H02_Omegam_a(self, a=1.0):
        return self._params.omega_m / a**3

    def _H2_H02_Omegak_a(self, a=1.0):
        return self._params.omega_k / a**2

    def _H2_H02_Omegal_a(self, a=1.0, override_speed=None):
        if self._params.cosmo_type == 'LCDM':
            return np.ones(len([a])) * self._params.omega_l  # Todo: check len([a])
        else:
            return self._params.omega_l * self._qevol(a)  # use integrator

    def _w_a(self, a=1.0):
        return self._params.w0 + (1.0 - a) * self._params.wa

    def _qevol(self, a=1.0):
        a = np.atleast_1d(a)
        if 1.0 not in a:
            a_temp = np.append(a, [1.0])
        else:
            a_temp = a
        a_sort, ind_unsort = _Util._check_a_ode(a=a_temp)
        ind1 = np.where(a_sort == 1.0)

        temp = integrate.odeint(_intg_qevol_hope,
                                y0=0.,
                                t=a_sort,
                                args=(self._params.w0, self._params.wa,),
                                mxstep=100000,
                                h0=1e-8).ravel()

        res = np.exp(temp - temp[ind1[0][0]])
        return (res[ind_unsort])[0:len(a)]

    #########################################################
    #  A series of functions for calculating                #
    #  cosmological distances:                              #
    #########################################################

    def dist_rad_a(self, a=1.0, override_speed=None):
        """Calculates the radial comoving distance, sometimes the comoving radius.
        The units of the output are [Mpc]
        """
        a = np.atleast_1d(a)  # make sure input is a numpy array

        a_sort, ind_unsort = _Util._check_a_ode(a=a)
        if 1.0 not in a_sort:
            a_temp = np.append(a_sort, [1.0])
        else:
            a_temp = a_sort
        temp = integrate.odeint(self._chi_a_int,
                                0.,
                                a_temp,
                                mxstep=100000,
                                h0=1e-8).flatten()
        chi = (temp - temp[-1])[ind_unsort] * self._params.c
        return chi

    def _chi_a_int_new(self, __, a):
        """"
        Integrand for calculating the line-of-sight comoving distance
        """
        a_value = np.atleast_1d(a)[0]
        return self.chi_func(self.H_a(a), self._params.omega_r, self._params.omega_m,
                             self._params.omega_k, self._params.omega_l, a_value)

    def _chi_a_int(self, __, a):
        """"
        Integrand for calculating the line-of-sight comoving distance
        """
        return -1.0 / self.H_a(a) / a**2  # need to be careful about the sqrtk

    def dist_trans_a(self, a=1.0, override_speed=None):
        """"
        Calculates the transverse comoving distance, sometimes called the comoving angular-diameter distance
          The units of the outputs are [Mpc]
        input:  a - scale factor [no dimensions]
                fast - keyword: False or True
                avgstep - option used with fast
        output: transverse comoving distance [Mpc]
        """
        Dc = self.dist_rad_a(a=a, override_speed=override_speed)
        if self._params.omega_k == 0.0:
            Dm = Dc
        elif self._params.omega_k > 0.0:
            Dm = (self._params.rh
                  * np.sinh(self._params.sqrtk * Dc / self._params.rh)
                  / self._params.sqrtk)
        elif self._params.omega_k < 0.0:
            Dm = (self._params.rh
                  * np.sin(self._params.sqrtk * Dc / self._params.rh)
                  / self._params.sqrtk)
        return Dm

    def dist_ang_a(self, a=1.0, override_speed=None):
        """
        calculates the angular-diameter distance to a given scale factor.
        The units of the outputs are [Mpc]
        """
        return self.dist_trans_a(a=a, override_speed=override_speed) * a

    def dist_lum_a(self, a=1.0, override_speed=None):
        """
        calculates the luminosity-diameter distance to a given scale factor.
        The units of the outputs are [Mpc]
        """
        return self.dist_trans_a(a=a, override_speed=override_speed) / a

    def _eta_a(self, a):  # conformal time/horizon: eta(a) [h^-1 Mpc] -AR version
        return [integrate.quad(self._eta_intgd, 0., aa)[0] for aa in a]

    def _eta_intgd(self, a):   # da integration     - AR version for speed up
        return 1. / (a**2 * self._hubble(a)) * self._params.H0 * self._params.rh

    #########################################################
    # A series of functions to compute thermodynamical      #
    # variables including recombination                     #
    #########################################################

    def _taudot_a(self, a=1.0):
        """tau_dot=d(tau)/d(eta) where tau is the optical depth and eta is the conformal time
        :param a: scale factor [1]
        :return : taudot: d(tau)/d(eta) [h Mpc^-1]
        """

        return self._rec.taudot_a(a)

    def _cs(self, a):
        """
        Returns the photon-baryon fluid sound speed [1]

        :param a: scale factor [1]
        :return : cs: baryon sound speed [1]

        """
        a = np.atleast_1d(a)
        return self._rec.cs_a(a)

    def _tau_a(self, a=1.0):
        """ Calculation of the optical depth *** more comments needed!! ***
        (might at some point need to speed this up as well)
        """
        a = np.atleast_1d(a)
        return np.array([integrate.quadrature(self._tau_intgd, np.log(aa), 0.0)[0] for aa in a])

    def _tau_intgd(self, lna):
        a = np.exp(lna)
        return -self._taudot_a(a=a) / (a * self.H_a(a=a) / self._params.H0 / self._params.rh)

    def _r_bph_a(self, a=1.):  # baryon to photon ratio r_bph(a) [1]
        return _derivs_boltz_hope._r_bph_a(a, self._params.omega_b, self._params.omega_gamma)

    def _cs_approx(self, a):    # photon-baryon fluid sound speed [1]
        # this is a simple expression which is probably a simple approximation - needs refining
        return np.sqrt(1. / (3. * (1. + self._r_bph_a(a))))

    def _cs_renorm(self, a):
        return (self._cs(a)
                * np.sqrt(a)
                / (self._cs(self._params.aini) * np.sqrt(self._params.aini))
                / np.sqrt(3.))

    def _dlnh_dlna(self, a=1.0):
        """Calculates dlnh_dlna. !!! Would be happy to get rid of this!!!"""
        a = np.atleast_1d(a)
        temp = (-.5
                / self._H2_H02_a(a)
                * (3. * self._H2_H02_Omegam_a(a=a)
                   + 3. * (1. + self._w_a(a))
                   * self._H2_H02_Omegal_a(a=a)
                   + 2. * self._H2_H02_Omegak_a(a=a))
                )

        return temp

    #########################################################
    # The next section lists a set of functions for         #
    # calculating the density parameters are a function of  #
    # a. This is also consistent with the notes in          #
    # section 1.2 of the PyCosmo notes.                     #
    #########################################################

    def _omega_m_a(self, a=1.0):
        """
        Calculates the matter density for a given scale factor
        input: a - scale factor [no dimensions]
        output: [no dimensions]
        """
        return self._H2_H02_Omegam_a(a=a) / self._H2_H02_a(a=a)

    def _omega_r_a(self, a=1.0):
        """
        Calculates the radiation density for a given scale factor
        input: a - scale factor [no dimensions]
        output: [no dimensions]
        """
        return self._H2_H02_Omegar_a(a=a) / self._H2_H02_a(a=a)

    def _omega_l_a(self, a=1.0):
        """
        Calculates the dark energy density for a given scale factor
        input: a - scale factor [no dimensions]
        output: [no dimensions]
        """
        return self._H2_H02_Omegal_a(a=a) / self._H2_H02_a(a=a)

    def _omega_a(self, a=1.0):
        """
        Calculates the total density for a given scale factor
        input: a - scale factor [no dimensions]
        output: [no dimensions]
        """
        return self._omega_m_a(a=a) + self._omega_r_a(a=a) + self._omega_l_a(a=a)

    def _omega_k_a(self, a=1.0):
        """
        Calculates the curvature for a given scale factor
        input: a - scale factor [no dimensions]
        output: [no dimensions]
        """
        return 1.0 - self._omega_a(a=a)
