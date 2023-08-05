from __future__ import absolute_import, division, print_function

import numpy as np
from scipy import integrate, special

from .LinearPerturbationBase import LinearPerturbationBase


class LinearPerturbationApprox(LinearPerturbationBase):

    """
    Class created to deal with things like fitting funtions.
    """

    def __init__(self, params, background):
        self._params = params
        self._background = background

        self._enrich_params()

    def __powerspec_a_k(self, a=1.0, k=0.1, diag_only=False):
        """
        Compute the linear power spectrum for given a and k values.

        :param a: scale factor [1]
        :param k: wavenumber [Mpc^-1]

        :return: P(k): matter power spectrum P(k) [Mpc^3]
        """
        a = np.atleast_1d(a)
        k = np.atleast_1d(k)
        if diag_only:
            assert len(a) == len(k)
        T_k = self.transfer_k(k=k)
        growth = self.growth_a(a)
        # using equation in section 2.4 of notes
        norm = (
            2.0
            * np.pi ** 2
            * self._params.deltah_norm ** 2
            * (self._params.c / self._params.H0) ** (3.0 + self._params.n)
        )

        if diag_only:
            pk = norm * growth ** 2 * k ** self._params.n * T_k ** 2
        else:
            pk = norm * np.outer(growth.T ** 2, k ** self._params.n * T_k ** 2).T
        return pk

    def growth_a(self, a=1.0, k=None, norm=0, verbose=False):
        """
        Compute the linear growth factor D(a) by integrating the growth differential equation

        :param a: scale factor [1]
        :param norm: normalisation scheme: 0: D(a=1)=1 (default), 1: D(a)=a in matter era

        :return: D(a): growth factor normalised to 1 at a=1 [1]
        """
        # assert k is None, 'this model {} does not consider k'.format(self)
        a = np.atleast_1d(a)

        # TODO: perhaps should add a switch that takes me to the hyper_a solution
        # TODO: check # integration as this differs from the Hypergoemtric solution by .25% at z=10
        # TODO: avoid hardwired value for ai
        # TODO: norm does not work yet

        ai = self._params.ic  # 5.e-2
        a_start = min(np.concatenate((a, np.array([ai]))))  # initial condition for integration
        if a_start < ai and verbose:
            print('growth_a: warning: initial redshift appears high')
        if a_start < 1e-80:
            raise ValueError("this method does not work for a < 1e-80")
        a = np.atleast_1d(a)

        perm = np.argsort(a)  # keepint track of index that would sort the array a
        # print(perm)
        inverse_perm = np.argsort(perm)  # useful indec for going back to original
        # print(inverse_perm)
        atemp = a[perm]
        y_start = np.array([1.0, 0.0])  # initial conditions: y1=G=1, y2=dG/dlna=0.
        a_out = np.concatenate((np.array([a_start]), atemp, np.array([1.])))
        x_out = np.log(a_out)

        h0 = self._params.h0_odeint
        rtol = self._params.rtol_odeint
        atol = self._params.atol_odeint

        u = integrate.odeint(self._growth_derivs, y_start, x_out, rtol=rtol, atol=atol, h0=h0)
        utemp = u[1:-1, ][inverse_perm]

        if norm == 0:
            D = utemp[:, 0] * a / u[-1, 0]  # normalise to D=1 at a=1
        elif norm == 1:
            D = utemp[:, 0] * a  # normalise to D=a in matter dominated era

        if verbose == False:
            return D
        elif verbose == True:
            return self._growth_hyper_a(a)

    def _growth_derivs(self, y, x):
        """Compute derivatices for the ODE for calcuting the growth factor.
        !!!NEED TO INCLUDE REFERENCE!!!
        """
        a_temp = np.exp(
            np.array(x)
        )  # ; x=ln(a) #; compute derivatives of y1=G and y2=dG/dlna
        f1 = y[1]  # f1=dy1/dx=y2=dG/dlna

        _dlnh_dlna = self._background._dlnh_dlna(a=a_temp)

        f2 = (
            -(4.0 + _dlnh_dlna) * y[1]
            - (3.0 + _dlnh_dlna - 1.5 * self._background._omega_m_a(a=a_temp)) * y[0]
        )
        return [f1, f2]

    def _growth_hyper_a(self, a=1.0):  # , Om=0.25,z=0):
        """
        LCDM growth function D(z) using hypergeometric function. Only
        valid for LCDM.
        This comes from Aseem Paranjape and is used for testing.
        ; param: a: scale factor [1]
        ; return: D(a): growth factor normalised to 1 at a=1 [1]
        """
        a = np.atleast_1d(a)
        a_temp = np.append(a, [1.0])
        acube = a_temp ** 3
        hbyh0 = np.sqrt(self._background._H2_H02_a(a=a_temp))
        g = (
            hbyh0
            / np.sqrt(self._params.omega_m)
            * np.power(a_temp, 2.5)
            * special.hyp2f1(
                5.0 / 6, 1.5, 11.0 / 6, -acube * (1.0 / self._params.omega_m - 1)
            )
        )
        g /= g[-1]  # normalised to 1 at a=1.0
        return g[:-1]

    # TODO: add a parameter and a waring, that a is not used
    def transfer_k(self, k):
        """
        Compute the matter transfer function using a choice of fitting
        functions. Currently the BBKS and Eisenstein and Hu transfer
        functions are supported. The choice of the fitting function is
        set by params.tk_type which can be set to either:
            - 'EH' for  Eisenstein & Hu, 1998, ApJ, 511, 5 (default)
            - 'BBKS' for BBKS as summarized by Peacock, 1997, MNRAS,
               284, 885

        :param  k: wavenumber [Mpc^-1]

        :return: T(k): matter transfer function [1]
        """
        if self._params.pk_type == "EH":
            tk = self._transfer_EH(k)
        elif self._params.pk_type == "BBKS":
            tk = self._transfer_BBKS(k)
        else:
            print(
                "transfer_k: error - only EH and BBKS fitting functions are supported"
            )

        return tk

    def _transfer_BBKS(self, k):
        """
        BBKS transfer function as summarized by Peacock (1997, MNRAS, 284, 885)

        :param  k: wavenumber [Mpc^-1]
        :return: T(k): BBKS matter transfer function [1]
        """
        k = np.atleast_1d(k)
        q_pd = k / self._params.h / self._add_gamma_Sugiyama()

        if self._params.tk_type == 'BBKS_CCL':
            tfac = self._params.Tcmb / 2.7
            q_pd = q_pd * tfac ** 2

        tk = np.log(1. + 2.34 * q_pd) / (2.34 * q_pd) * (1. + 3.89 * q_pd +
                                                         (16.1 * q_pd) ** 2
                                                         + (5.46 * q_pd) ** 3
                                                         + (6.71 * q_pd) ** 4) ** (-.25)

        return tk

    def _add_gamma_Sugiyama(self):
        """ This calculates Gamma for the linear powerspectrum using the
        prescription Sugiyama (1995, APJS, 100, 281)"""
        gamma = (
            self._params.omega_m
            * self._params.h
            * np.exp(
                -self._params.omega_b
                * (1. + np.sqrt(2. * self._params.h) / self._params.omega_m)
            )
        )
        self._params.gamma = gamma
        return gamma

    def _transfer_EH(self, k):
        """Return the CDM + baryon transfer function as defined in
        Eisenstein & Hu, 1998, ApJ, 511, 5, Equation (16) Input: wave
        vector k in Mpc^-1"""

        T = self._params.omega_b / self._params.omega_m * self._T_b(
            k
        ) + self._params.omega_dm / self._params.omega_m * self._T_c(k)

        return T

    def _jn_spher(self, n, x):
        """Returns the spherical Bessel function of order n.
        This is used to compute the oscillatory feature of the baryonic
        transfer function as in Eisenstein & Hu, 1998, ApJ, 511, 5"""

        jn_spher = np.sqrt(np.pi / (2. * x)) * special.jn(n + .5, x)

        return jn_spher

    def _G(self, y):
        """Returns the function G as defined in Eisenstein & Hu, 1998,
        ApJ, 511, 5, Equation (15)
        G(y) = y(-6. sqrt(1 + y) + (2 + 3 y) ln((sqrt(1 + y) + 1)/(sqrt(1 + y) - 1)))
        and needed to calculate alpha_b"""

        G = y * (
            -6. * np.sqrt(1. + y)
            + (2. + 3. * y) * np.log((np.sqrt(1. + y) + 1.) / (np.sqrt(1. + y) - 1.))
        )

        return G

    def _photon2baryon_dens(self, z):
        """Returns the ratio of the baryon to photon momentum density R
        as defined in Eisenstein & Hu, 1998, ApJ, 511, 5, Equation (5)
        for redshift z
        R = 31.5 omega_b h^2 sigma_27^-4 (z/10^3)^-1"""

        R = (
            31.5
            * self._params.omega_b
            * self._params.h ** 2
            * self._params._sigma_27 ** (-4)
            * (z / 10 ** 3) ** (-1.)
        )

        return R

    def _T_0(self, k, alpha_c, beta_c):
        """Returns the transfer function T_0 as defined in Eisenstein &
        Hu, 1998, ApJ, 511, 5, Equation (19)

        T_0 = ln(e+1.8 beta_c q)/(ln(e+1.8 beta_c q) + C q^2)

        where
        q = (k [Mpc^-1])/(13.41 k_eq)
        C = 14.2/alpha_c + 386/(1+69.9 q^1.08)
        alpha_c = a_1^(-omega_b/omega_0) a_2^(-(omega_b/omega_0)^3)
        a_1 = (46.9 omega_0 h^2)^0.670 (1+(32.1 omega_0 h^2)^-0.532)
        a_2 = (12.0 omega_0 h^2)^0.424 (1+(45.0 omega_0 h^2)^-0.582)
        beta_c^-1 = 1 + b_1 ((omega_c/omega_0)^b_2 - 1)
        b_1 = 0.944 (1 + (458 omega_0 h^2)^-0.708)^-1
        b_2 = (0.395 omega_0 h^2)^-0.0266"""

        # Define the needed variables as in Eqs. (10), (20)
        q = k / (13.41 * self._params._k_eq)
        C = 14.2 / alpha_c + 386. / (1. + 69.9 * q ** 1.08)

        T_0 = np.log(np.e + 1.8 * beta_c * q) / (
            np.log(np.e + 1.8 * beta_c * q) + C * q ** 2
        )

        return T_0

    def _T_b(self, k):
        """Returns the baryonic part of the transfer function as defined
        in Eisenstein & Hu, 1998, ApJ, 511, 5, Equation (21)

        T_b = (T_0(k,1,1)/(1 + (k s/5.2)^2) + alpha_b/(1 + (beta_c/(k s))^3)*e^-(k/k_Silk)^1.4)*j_0(k s_tilde)
        """

        # Define the needed variable as in Eq. (22)
        s_tilde = self._params._sound_horiz / (
            1. + (self._params._beta_node / (k * self._params._sound_horiz)) ** 3
        ) ** (1. / 3.)

        T_b = (
            self._T_0(k, 1., 1.) / (1. + (k * self._params._sound_horiz / 5.2) ** 2)
            + self._params._alpha_b
            / (1. + (self._params._beta_b / (k * self._params._sound_horiz)) ** 3.)
            * np.exp(-(k / self._params._k_Silk) ** 1.4)
        ) * self._jn_spher(0, k * s_tilde)

        return T_b

    def _T_c(self, k):
        """Returns the CDM part of the transfer function as defined in
        Eisenstein & Hu, 1998, ApJ, 511, 5, Equation (17)
        T_c = f T_0(k,1,beta_c) + (1 - f) T_0(k,alpha_c,beta_c)
        """

        f = 1. / (1. + (k * self._params._sound_horiz / 5.4) ** 4)  # Eq. (18)

        T_c = f * self._T_0(k, 1., self._params._beta_c) + (1. - f) * self._T_0(
            k, self._params._alpha_c, self._params._beta_c
        )

        return T_c

    def _enrich_params(self):
        """Sets the constant parameters needed for the
        LinearPerturbationApprox class.  If pk_type = EH it sets the
        parameters needed for computing the transfer function as defined
        in Eisenstein & Hu, 1998, ApJ, 511, 5.

        If pk_type = BBKS it sets the parameters needed for computing
        the BBKS transfer function as summarized by Peacock (1997,
        MNRAS, 284, 885)
        """

        if self._params.pk_type == "EH":

            omh2 = self._params.omega_m * self._params.h ** 2
            if self._params.Tcmb <= 0.:
                print("Warning in EH: CMB temperature <= 1.")

            self._params._sigma_27 = (
                self._params.Tcmb / 2.7
            )  # Normalised CMB temperature

            # Redshift values
            # TODO: this differs from z_eq in the cosmo class. should probably rename
            # it to avoid confusion
            # Redshift at matter-radiation equality, Eq. (2)
            self._params._z_equality = 2.5e4 * omh2 * self._params._sigma_27 ** -4
            b_1 = 0.313 * omh2 ** -0.419 * (1. + 0.607 * omh2 ** 0.674)
            b_2 = 0.238 * omh2 ** 0.223
            self._params._z_drag = (
                1291.
                * (omh2 ** 0.251)
                / (1. + 0.659 * omh2 ** 0.828)
                * (1. + b_1 * (self._params.omega_b * self._params.h ** 2) ** b_2)
            )  # Redshift at drag epoch, Eq. (4)

            # Wave vector values
            self._params._k_eq = (
                7.46e-2 * omh2 * self._params._sigma_27 ** -2
            )  # Eq. (3), units: Mpc^-1
            self._params._k_Silk = (
                1.6
                * (self._params.omega_b * self._params.h ** 2) ** 0.52
                * (omh2) ** 0.73
                * (1. + (10.4 * omh2) ** -0.95)
            )  # Eq. (7), units: Mpc^-1

            # Comoving distance values
            self._params._R_drag = self._photon2baryon_dens(self._params._z_drag)
            self._params._R_eq = self._photon2baryon_dens(self._params._z_equality)
            self._params._sound_horiz = (
                2
                / (3 * self._params._k_eq)
                * np.sqrt(6 / self._params._R_eq)
                * np.log(
                    (
                        np.sqrt(1. + self._params._R_drag)
                        + np.sqrt(self._params._R_drag + self._params._R_eq)
                    )
                    / (1. + np.sqrt(self._params._R_eq))
                )
            )  # Eq. (6)

            # CDM transfer function, Equations (11), (12)

            self._params._a1 = (46.9 * omh2) ** 0.670 * (1. + (32.1 * omh2) ** -0.532)
            self._params._a2 = (12. * omh2) ** 0.424 * (1. + (45. * omh2) ** -0.582)
            self._params._alpha_c = self._params._a1 ** (
                -self._params.omega_b / self._params.omega_m
            ) * self._params._a2 ** (
                -(self._params.omega_b / self._params.omega_m) ** 3.
            )
            self._params._b1 = 0.944 * (1. + (458. * omh2) ** -0.708) ** -1
            self._params._b2 = (0.395 * omh2) ** -0.0266
            self._params._beta_c = (
                1.
                + self._params._b1
                * (
                    (self._params.omega_dm / self._params.omega_m) ** self._params._b2
                    - 1.
                )
            ) ** -1.

            # Baryon transfer function, Equations (14), (24), (23)

            # alpha_b = 2.07 k_eq s (1 + R_d)^-3/4 G((1 + z_eq)/(1 + z_d))
            # beta_b = 0.5 + omega_b/omega_m_0 + (3 - 2 omega_b/omega_m_0) sqrt((17.2 omega_m_0 h^2)^2 + 1)
            # b_node = 8.41 (omega_m_0 h^2)^0.435

            self._params._alpha_b = (
                2.07
                * self._params._k_eq
                * self._params._sound_horiz
                * (1. + self._params._R_drag) ** -.75
                * self._G((1. + self._params._z_equality) / (1. + self._params._z_drag))
            )
            self._params._beta_b = (
                0.5
                + self._params.omega_b / self._params.omega_m
                + (3 - 2 * self._params.omega_b / self._params.omega_m)
                * np.sqrt((17.2 * omh2) ** 2 + 1)
            )
            self._params._beta_node = 8.41 * omh2 ** 0.435

        if self._params.pk_type == "BBKS":
            self._add_gamma_Sugiyama()

        # normalise linear power spectrum   #TODO: perhaps avoid writing in
        # params; perhaps needs more error checking
        if self._params.pk_norm_type == "deltah":
            self._params.deltah_norm = self._params.pk_norm
            self._params.sigma8 = self.sigma8()
        if self._params.pk_norm_type == "sigma8":
            self._params.sigma8 = self._params.pk_norm
            self._params.deltah_norm = 4.e-5  # arbitrary temporary value
            sigma8_temp = self.sigma8()
            self._params.deltah_norm = (
                self._params.deltah_norm * self._params.sigma8 / sigma8_temp
            )

        return None

    def print_params(self):
        """
        Print the parameters added by LinearPerturbationApprox

        """

        if self._params.pk_type == "EH":
            print("")

            print(
                "---- Derived cosmology parameters for Eisenstein and Hu transfer function ----"
            )
            print()
            print("sigma_27: Dimensionless CMB temperatue [1]:", self._params._sigma_27)
            print(
                "z_equality: Redshift of matter-radiation equality [1]:",
                self._params._z_equality,
            )
            print("z_drag: Redshift of drag epoch [1]:", self._params._z_drag)
            print(
                "k_eq: Particle horizon at equality epoch [Mpc-1]:", self._params._k_eq
            )
            print("k_Silk: Silk damping scale [Mpc-1]:", self._params._k_Silk)
            print(
                "sound_horiz: Sound horizon (sound_horiz) [Mpc]:",
                self._params._sound_horiz,
            )

        if self._params.pk_type == "BBKS":

            print("---- Derived cosmology parameters for BBKS transfer function ----")
            print()
            print("gamma: Gamma Sugiyama [h Mpc-1]:", self._params.gamma)
