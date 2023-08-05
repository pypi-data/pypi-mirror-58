from __future__ import print_function, division

import numpy as np


class Projection(object):

    def __init__(self, params, background, lin_pert, nonlin_pert):

        self.params = params
        self.background = background
        self._lin_pert = lin_pert
        self._nonlin_pert = nonlin_pert

    def cl_limber(self, ells, weight_function1, weight_function2, a_grid, cosmo,
                  perturb='nonlinear'):
        """
        Compute the angular power spectrum of the auto- or cross-correlation between
        two LSS probes i.e. galaxy overdensity, cosmic shear or CMB lensing.
        :param ells: array of angular multipoles l
        :param weight_function1: radial weight function for first probe
        :param weight_function2: radial weight function for second probe
        :param a_grid: integration grid in scale factor a
        :param perturb: string tag denoting if we use linear or nonlinear power spectrum
        :return cls: value of the angular power spectrum at the multipoles ells
        """

        amin, amax, num = a_grid
        amin, amax = min(amin, amax), max(amin, amax)
        a_vec = np.linspace(amin, amax, num)      # use a as integration variable
        intg_vec = self.cl_limber_int(a_vec, ells, weight_function1,
                                      weight_function2, cosmo, perturb)
        cl = np.trapz(intg_vec, a_vec, axis=1)

        return cl

    def cl_limber_int(self, a, ells, weight_function1, weight_function2, cosmo, perturb='nonlinear'):
        """
        Return the integrand needed to compute the angular power spectrum of the auto- or
        cross-correlation between two LSS probes in the Limber approximation.
        :param a: array of scale factor values a
        :param ells: array of angular multipoles l
        :param weight_function1: radial weight function for first probe
        :param weight_function2: radial weight function for second probe
        :param perturb: string tag denoting if we use linear or nonlinear power spectrum
        :return intg: value of integrand at ell for the values of a
        """

        r = self.background.dist_trans_a(a=a)
        weightfunc = (weight_function1(a, self) * weight_function2(a, self)
                      / r**2 / a**2 / self.background.H_a(a) * self.params.c)

        avec = np.tile(a, len(ells))
        weightvec = np.tile(weightfunc, len(ells))
        kvec = np.outer(ells, 1 / r).flatten()

        if perturb == 'linear':
            intg = weightvec * self._lin_pert.powerspec_a_k(avec, kvec, diag_only=True)
        elif perturb == 'nonlinear':
            intg = weightvec * self._nonlin_pert.powerspec_a_k(avec, kvec, diag_only=True)
        else:
            raise ValueError('perturb {} not implemented'.format(perturb))

        intg = intg.reshape(len(ells), -1)
        return intg

    def cl_limber_ISW(self, ell, weight_function1, weight_function2, growth_ISW, a_grid,
                      perturb='linear'):
        """
        Compute the angular power spectrum of the cross correlation between
        the CMB temperature anisotropies and the galaxy overdensity/cosmic shear.
        :param ell: array of angular multipole l
        :param weight_function1: radial weight function for first probe
        :param weight_function2: radial weight function for second probe
        :param growth_ISW: growth function for ISW
        :param a_grid: integration grid in scale factor a
        :param linear: string tag denoting if we use linear or nonlinear power spectrum
        :return cls: value of the angular power spectrum at the multipoles ells
        """

        # There is no minus sign in the integrand, i.e. we don't need to reverse the integration
        # range
        amin, amax, num = a_grid
        amin, amax = min(amin, amax), max(amin, amax)
        # this code requires descending a values to work:
        a_vec = np.linspace(amin, amax, num)[::-1]
        intg_vec = self.cl_limber_ISW_int(
            a_vec, ell, weight_function1, weight_function2, growth_ISW, perturb)
        # cl = np.trapz(intg_vec,a_vec)
        cls = np.trapz(intg_vec, a_vec, axis=1)

        cls *= 3. * self.params.omega_m * self.params.H0 ** 2 * \
            self.params.Tcmb / self.params.c ** 2 * 1. / ell ** 2

        return cls

    def cl_limber_ISW_int(self, a, ells, weight_function1, weight_function2, growth_ISW,
                          perturb='linear'):
        """
        Return the integrand needed to compute the angular power spectrum of the cross correlation
        between the CMB temperature anisotropies and the galaxy overdensity/cosmic shear/CMB
        lensing.

        :param a: array of scale factor values a
        :param ells: array of angular multipoles l
        :param weight_function1: radial weight function for first probe
        :param weight_function2: radial weight function for second probe
        :param growth_ISW: growth function for ISW
        :param perturb: string tag denoting if we use linear or nonlinear power spectrum
        :return intg: value of integrand at ell for the values of a
        """

        r = self.background.dist_trans_a(a=a)
        weightfunc = weight_function1(a, self) * weight_function2(a, self) * growth_ISW(a, self)
        # TODO This is for a vectorised call - need to remove at some point

        avec = np.ones(len(ells) * len(a))
        weightvec = np.tile(weightfunc, len(ells))
        kvec = np.outer(ells, 1 / r).flatten()

        if perturb == 'linear':
            intg = weightvec * self._lin_pert.powerspec_a_k(avec, kvec, diag_only=True)
        else:
            intg = weightvec * self._nonlin_pert.powerspec_a_k(avec, kvec, diag_only=True)

        intg = intg.reshape(len(ells), -1)

        return intg

    def cl_limber_IG(self, ell, weight_function1, weight_function2, F, a_grid, IAmodel='NLA'):
        """
        Compute the angular power spectrum of the cross correlation between
        intrinsic galaxy ellipticities and tracers of the LSS.
        :param ell: array of angular multipole l
        :param weight_function1: radial weight function for first probe -> this needs to be the weight function
        :param weight_function2: radial weight function for second probe -> this needs to be n(z)
        :param F: IA bias function
        :param a_grid: integration grid in scale factor a
        :param IAmodel: string tag denoting if we use NLA or LA IA model
        :return cls: value of the angular power spectrum at the multipoles ells
        """

        amin, amax, num = a_grid
        amin, amax = min(amin, amax), max(amin, amax)
        a_vec = np.linspace(amin, amax, num)
        intg_vec = self.cl_limber_IG_int(a_vec, ell, weight_function1, weight_function2, F, IAmodel)
        # cl = np.trapz(intg_vec,a_vec)
        cls = np.trapz(intg_vec, a_vec, axis=1)

        return cls

    def cl_limber_IG_int(self, a, ells, weight_function1, weight_function2, F, IAmodel='NLA'):
        """
        Return the integrand for the angular power spectrum of intrinsic alignments (IAs)
        computed using the NLA or LA model.
        :param a: array of scale factor values a
        :param ells: array of angular multipoles l
        :param weight_function1: radial weight function for first probe -> this needs to be the weight function
        :param weight_function2: radial weight function for second probe -> this needs to be n(z)
        :param F: IA bias function
        :param IAmodel: string tag denoting if we use NLA or LA IA model
        :return intg: value of integrand at ell for the values of a
        """

        r = self.background.dist_trans_a(a=a)
        # For the second redshift selection functions, we need to transform a to z
        z = 1. / a - 1.
        weightfunc = weight_function1(a, self) * weight_function2(z) * F(a, self) / r**2 / a**2

        avec = np.tile(a, len(ells))
        weightvec = np.tile(weightfunc, len(ells))
        kvec = np.outer(ells, 1. / r).flatten()

        if IAmodel == 'NLA':
            intg = weightvec * self._nonlin_pert.powerspec_a_k(avec, kvec, diag_only=True)
        else:
            intg = weightvec * self._lin_pert.powerspec_a_k(avec, kvec, diag_only=True)

        intg = intg.reshape(len(ells), -1)

        return intg

    def cl_limber_II(self, ell, weight_function1, weight_function2, F, a_grid, IAmodel='NLA'):
        """
        Compute the angular power spectrum of the auto power spectrum of
        intrinsic galaxy ellipticities.
        :param ell: array of angular multipole l
        :param weight_function1: redshift selection function for first probe
        :param weight_function2: redshift selection function for second probe
        :param F: IA bias function
        :param a_grid: integration grid in scale factor a
        :param IAmodel: string tag denoting if we use NLA or LA IA model
        :return cls: value of the angular power spectrum at the multipoles ells
        """

        amin, amax, num = a_grid
        amin, amax = min(amin, amax), max(amin, amax)
        a_vec = np.linspace(amin, amax, num)
        intg_vec = self.cl_limber_II_int(a_vec, ell,
                                         weight_function1, weight_function2, F, IAmodel)
        cls = np.trapz(intg_vec, a_vec, axis=1)

        return cls

    def cl_limber_II_int(self, a, ells, weight_function1, weight_function2, F, IAmodel='NLA'):
        """
        Return the integrand for the angular power spectrum of the auto correlation of intrinsic alignments (IAs)
        computed using the NLA or LA model.
        :param a: array of scale factor values a
        :param ells: array of angular multipoles l
        :param weight_function1: redshift selection function for first probe
        :param weight_function2: redshift selection function for second probe
        :param F: IA bias function
        :param IAmodel: string tag denoting if we use NLA or LA IA model
        :return intg: value of integrand at ell for the values of a
        """

        r = self.background.dist_trans_a(a=a)
        # For the redshift selection functions, we need to transform a to z
        z = 1. / a - 1.
        weightfunc = (self.background.H_a(a=a) / self.params.c * weight_function1(z)
                      * weight_function2(z) * F(a, self)**2 / r**2 / a**2)

        avec = np.tile(a, len(ells))
        weightvec = np.tile(weightfunc, len(ells))
        kvec = np.outer(ells, 1. / r).flatten()

        if IAmodel == 'NLA':
            intg = weightvec * self._nonlin_pert.powerspec_a_k(avec, kvec, diag_only=True)
        else:
            intg = weightvec * self._lin_pert.powerspec_a_k(avec, kvec, diag_only=True)

        return intg.reshape(len(ells), -1)
