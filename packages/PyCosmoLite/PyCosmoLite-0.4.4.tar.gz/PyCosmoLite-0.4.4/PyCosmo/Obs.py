from __future__ import absolute_import, division, print_function

import copy
from functools import partial

import numpy as np

from ._scipy_utils import interp1d

# CONSTANTS
# Gravitational constant
G = 6.67408*10**-11  # [G] = m^3/(kg s^2)
# Conversion between Mpc and metres
Mpc2m = 3.086*10**16*10**6  # 1pc = 3.086*10^16 m, 1 Mpc = 10^6 pc
# Mass of the Sun
Msun = 1.9885*10**30  # [Msun] = kg


try:
    profile
except NameError:
    def profile(x): return x


class Obs(object):
    """
    This is to create an instance that contains information about
    experiments and surveys that is needed to calculate the observables. There are currently two
    visions for this a PyCosmoObs one- which would create objects able to calculate the observables associated with
    an experiment and PyCosmoSV version that would mainly deal with the features of the survey and not, for instance,
    calculate cls. Regardless of this choice there are still common features between the two that we
    impliment now.

    The idea is that the Obs class would act at the same level as the Cosmo class and would be initialise using
    a parameter file.

    """

    def __init__(self):

        pass

    def setup(self, obsparams):
        """
        Sets the multiplicative calibration parameters as defined in obsparams.
        :param obsparams: dictionary containing specifications for observable
        :return:
        """

        # Ensure that the galaxy bias and the multiplicative bias are defined
        # If not, set them to 1
        if 'bias' not in obsparams:
            print('WARNING: Setting bias to 1.')
            obsparams['bias'] = 1.
        if 'm' not in obsparams:
            print('WARNING: Setting m to 0.')
            obsparams['m'] = 0.
        if 'Akcmb' not in obsparams:
            print('WARNING: Setting Akcmb to 1.')
            obsparams['Akcmb'] = 1.

        self._enrich_params(obsparams)
        self.windows(obsparams)

    def print_params(self):

        pass

    def _enrich_params(self, obsparams):
        """
        Set undefined parameters to default or interpreted values.
        :param obsparams: dictionary containing specifications for observable
        :return:
        """

        if 'nztype' not in obsparams:
            obsparams['nztype'] = [None, None]

        if 'IAmodel' not in obsparams:
            print('Setting intrinsic alignment model to NLA...')
            obsparams['IAmodel'] = 'NLA'
        if 'fzmodel' not in obsparams:
            print('Setting F(z) model to corrected version according to Hirata&Seljak 2010...')
            obsparams['fzmodel'] = 'corr'

        obsparams['a_grid'] = [1./(1. + obsparams['z_grid'][0]), 1./(1. + obsparams['z_grid'][1]),
                               obsparams['z_grid'][2]]

    def nz(self, obsparams, nzmode=None, path2zdist=None):
        """
        Compute and normalise redshift selection function of survey.
        :param obsparams: dictionary containing specifications for observable
        :param nzmode: string tag in ['smail', 'cfhtlens', 'custom']
        :param path2zdist: if n(z) comes from a file, then this is the path to the file
        :return z: redshift grid
        :return pz_norm: corresponding normalised redshift selection function
        """
        # Todo need to think about default of a (like the Cosmo Class) or z?

        distribution_type = ['smail', 'cfhtlens', 'custom']

        assert nzmode.lower() in distribution_type, \
            'The redshift distribution type in input parameters is not recognised. Use one of the following: \n %s ' \
            % distribution_type

        if nzmode.lower() == 'smail':
            assert set(['z0', 'alpha', 'beta']).issubset(obsparams), \
                'Make sure the Smail distribution parameters z0, alpha and beta are included in obsparams.'

            num_points = int(obsparams['z_grid'][2])
            z = np.linspace(obsparams['z_grid'][0], obsparams['z_grid'][1], num_points)
            pz = np.exp(-(z / obsparams['z0']) ** obsparams['beta']) * z ** obsparams['alpha']

        elif nzmode.lower() == 'cfhtlens':
            data = np.genfromtxt(path2zdist)

            z_grid = (data[:, 0][:-1]+data[:, 0][1:])/2.
            z = np.append(z_grid, data[:, 0][-1])
            pz = data[:, 1]

        elif nzmode.lower() == 'custom':
            datafile = np.genfromtxt(path2zdist)

            z = datafile[:, 0]
            pz = datafile[:, 1]

        else:
            z = None
            pz = None

        if z is not None:
            norm = np.trapz(pz, z)

            pz_norm = pz/norm

            # Assert that the normalisation worked
            intg = np.trapz(pz_norm, z)
            assert np.abs(intg - 1.0) <= 10**(-8), 'Normalisation failed to reach required accuracy.'

        else:
            pz_norm = pz

        return z, pz_norm

    def bin_setup(self, obsparams):
        """
        Set up the redshift selection functions, i.e. each redshift selection function
        is either calculated from the default hard coded ones or the tabulated selection
        functions are read in and saved as attributes in self.n.

        :param obsparams: dictionary containing specifications for observable
        :return:
        """

        self.n = [0, 0]
        # Check if this is an auto correlation
        if obsparams['probes'].count(obsparams['probes'][0]) == len(obsparams['probes']):
            nzmode = obsparams['nz'][0]
            if nzmode is not None:
                print('Setting up galaxy selection function for {}.'.format(obsparams['probes'][0]))
                if nzmode in ['cfhtlens', 'custom']:
                    path2zdist = obsparams['path2zdist'][0]
                    z, selec = self.nz(obsparams, nzmode, path2zdist)
                else:
                    z, selec = self.nz(obsparams, nzmode)
                self.n[0] = interp1d(z, selec, bounds_error=False, fill_value=0.)
                self.n[1] = copy.deepcopy(self.n[0])
            else:
                self.n[0] = None
                self.n[1] = copy.deepcopy(self.n[0])

        else:
            for i in range(len(obsparams['probes'])):
                nzmode = obsparams['nz'][i]
                if nzmode is not None:
                    print('Setting up galaxy selection function for {}.'.format(
                        obsparams['probes'][i]))
                    if nzmode in ['cfhtlens', 'custom']:
                        path2zdist = obsparams['path2zdist'][i]
                        z, selec = self.nz(obsparams, nzmode, path2zdist)
                    else:
                        z, selec = self.nz(obsparams, nzmode)
                    self.n[i] = interp1d(z, selec, bounds_error=False, fill_value=0.)
                else:
                    self.n[i] = None

    def windows(self, obsparams):
        """
        Set up the radial window functions for the surveys and the
        probes, i.e. computes the window functions appropriate
        for the galaxy overdensity, gamma, CMB temperature and CMB kappa and
        saves them in the attribute self.window.
        :param obsparams: dictionary containing specifications for observable
        :return:
        """

        # Read in the redshift selection functions when the class is initialised
        self.bin_setup(obsparams)

        print('Setting up redshift window function...')
        self.window = [0, 0]
        for i in range(len(obsparams['probes'])):
            probe = obsparams['probes'][i]
            if probe == 'deltag':
                self.window[i] = partial(self._weight_function_clustering, n=self.n[i])
            elif probe == 'gamma':
                self.window[i] = partial(self._weight_function_lensing, n=self.n[i])
            elif probe == 'temp':
                self.window[i] = self._weight_function_cmbtemp
            elif probe == 'cmbkappa':
                if 'zrecomb' in obsparams:
                    self.zrecomb = obsparams['zrecomb']
                else:
                    print('You have chosen to compute cls involving CMB kappa.'
                          'This needs a recombination redshift. Please set it using the zrecomb keyword in params.')
                self.window[i] = self._weight_function_cmblensing

    def _weight_function_cmblensing(self, a, cosmo):
        """
        Compute the radial weight function for CMB lensing as a function of scale factor a as
        W^kappa_CMB(a) = 3/2 Omega_m (H0/c)^2 r(chi)(a)/a (r(chi)(a_*)-r(chi)(a))/r(chi)(a_*).
        This will be used to calculate the weak lensing angular power spectra.
        :param a_vec: scale factor [1]
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :return window: radial weight function W^CMB_kappa(a) [1]
        """

        # Compute the needed distances because they are needed multiple times
        dists = cosmo.background.dist_trans_a(a=a)
        distrecomb = cosmo.background.dist_trans_a(a=1./(1.+self.zrecomb))

        window = 3./2.*(cosmo.params.H0/cosmo.params.c)**2*cosmo.params.omega_m*dists/a *\
            ((distrecomb - dists)/distrecomb)

        window[a < 1./(1 + self.zrecomb)] = 0.

        return window

    def _weight_function_clustering(self, a, cosmo, n):
        """
        Calculate the radial weight functions for clustering as a function of a as
        W^delta = n(a) H(a)/c.
        This will be used to calculate the clustering angular power spectra
        :param a: scale factor [1]
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param n: callable (function) redshift distribution of survey [1]
        :return window: radial weight function W^deltag(a) [1]
        """

        z = 1./a - 1.

        window = n(z)*cosmo.background.H_a(a)/cosmo.params.c

        return window

    def _weight_function_cmbtemp(self, a, cosmo):
        """
        Calculate the radial weight functions for CMB temperature as a function of a as
        W^CMB = 1.
        This will be used to calculate the ISW angular power spectra
        :param a: scale factor [1]
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :return window: radial weight function W^CMB(a) [1]
        """

        window = np.ones(a.shape[0])

        return window

    def _weight_function_lensing(self, a_vec, cosmo, n):
        """
        Compute the radial weight function for weak lensing as a function of scale factor a as
        W^gamma(a) = 3/2 Omega_m (H0/c)^2 r(chi)(a)/a int_amin^amax da_s/a_s^2 n(a_s) (r(chi)(a_s)-r(chi)(a))/r(chi)(a).
        where n is the redshift distribution of the survey.
        This will be used to calculate the weak lensing angular power spectra.
        :param a_vec: scale factor [1]
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param n: callable (function) redshift distribution of survey [1]
        :return window: radial weight function W^gamma(a) [1]
        """

        # TODO For now: hard coded amin and anum
        amin = 1./15.
        anum = 200

        # We need to test that we do not cut off the integrals too early
        assert np.abs(n(1. / amin - 1.)) <= 1e-5,\
            ('There is still a significant number of galaxies at the cutoff '
             'redshift. You might try a higher cutoff.')

        window = []

        a_temp = np.concatenate((np.linspace(amin, a_vec[0], anum, endpoint=False), a_vec))
        pz = n(1. / a_temp - 1.) / a_temp**2
        chi = cosmo.background.dist_rad_a(a=a_temp)
        chi_a = cosmo.background.dist_rad_a(a=a_vec)
        rchi_a = cosmo.background.dist_trans_a(a=a_vec)

        for i in range(len(a_vec)):

            if cosmo.params.omega_k == 0.:
                integrand = pz[:anum + i] * (chi[:anum + i] - chi_a[i]) / chi[:anum + i]
            elif cosmo.params.omega_k < 0.:
                integrand = (pz[:anum + i]
                             * np.sin(cosmo.params.sqrtk * (chi[:anum + i] - chi_a[i])
                                      / cosmo.params.rh)
                             / np.sin(cosmo.params.sqrtk * chi[:anum + i] / cosmo.params.rh)
                             )
            else:
                integrand = (pz[:anum + i]
                             * np.sin(cosmo.params.sqrtk * (chi[:anum + i] - chi_a[i])
                                      / cosmo.params.rh)
                             / np.sinh(cosmo.params.sqrtk * chi[:anum + i] / cosmo.params.rh)
                             )

            wind = np.trapz(integrand, a_temp[:anum + i])
            window.append(wind)
        len_wind = len(window)
        window = np.array(window).reshape(-1, len_wind)
        window *= 1.5 * (cosmo.params.H0 / cosmo.params.c) ** 2 * (
                                                             cosmo.params.omega_m * rchi_a / a_vec)
        window = window.reshape(len_wind,)
        return window

    def _cl_lss(self, ells, cosmo, obsparams):
        """
        Calculate the cls  for LSS based on
        Cl^ij = int_amin^amax c da/(a^2 H(a)) W_i(a) W_j(a)/r(chi)(a)^2 P(k=(l+1/2)/r(chi)(a), a)
        where W is the radial weight function for clustering.
        :param ells: array of inverse angular scale [1]
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param obsparams: dictionary containing specifications for observable
        :return cls: array of spherical harmonic power spectrum coefficients Cl [1]
        """
        # Todo add dynamic setting for amin based on the weight function

        ells = np.atleast_1d(ells)
        # TODO This is for a vectorised call - need to remove at some point
        cls = cosmo.projection.cl_limber(ells, self.window[0], self.window[1], obsparams['a_grid'],
                                         cosmo, obsparams['perturb'])

        return cls

    # TODO: These are things that potentially need to go into lin pert approx
    def growth_suba(self, cosmo, a=1.0):
        """
        Returns the growth factor divided by the scale factor a
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param a: scale factor a
        :return growth_suba_temp: growth factor divided by scale factor
        """

        growth_suba_temp = cosmo._lin_pert.growth_a(a=a)/a

        return growth_suba_temp

    def growth_suba_deriv(self, cosmo, a=1.0):
        """
        Returns the derivative of growth_suba by scale factor a
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param a: scale factor a
        :return growth_suba_deriv: derivative of growth_suba w.r.t. z
        """

        delta = a * 1e-5

        growth_min2del = self.growth_suba(cosmo, a=a - 2 * delta)
        growth_min1del = self.growth_suba(cosmo, a=a - delta)
        growth_plus1del = self.growth_suba(cosmo, a=a + delta)
        growth_plus2del = self.growth_suba(cosmo, a=a + 2 * delta)

        growth_suba_deriv = (growth_min2del - 8 * growth_min1del
                             + 8 * growth_plus1del - growth_plus2del) / (12 * delta)

        return growth_suba_deriv

    def growth_ISW(self, a, cosmo, mode='num'):
        """
        Returns the generalised growth factor used in the ISW angular power spectrum
        integrand both for the analytic approximation and the numerical derivative.
        :param a: scale factor
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param mode: numerical or analytic
        :return growth: the value of the generalised growth factor at redshift x
        """

        if mode == 'num':
            growth = cosmo._lin_pert.growth_a(a=a)*self.growth_suba_deriv(cosmo, a=a)
        elif mode == 'fit':
            growth = (-1.)*cosmo._lin_pert.growth_a(a=a)**2 *\
                     (cosmo.background._omega_m_a(a=a)**0.6-1.)

        return growth

    def _cl_ISW(self, ells, cosmo, obsparams):
        """
        Calculate the ISW cls based on
        Cl^iT = 3 Omega_m H0^2 T_CMB/c^2 1/(ell+1/2) int_1^0 da d/da [D(a)/a] D(a) W_i(a) P_lin(k=(l+1/2)/r(chi)(a), 1)
        where W_i is the radial weight function for the LSS probe.
        :param ells: array of inverse angular scale [1]
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param obsparams: dictionary containing specifications for observable
        :return cls: array of spherical harmonic power spectrum coefficients Cl [1]
        """
        # Todo add dynamic setting for amin based on the weight function

        ells = np.atleast_1d(ells)
        # TODO This is for a vectorised call - need to remove at some point
        cls = cosmo.projection.cl_limber_ISW(ells, self.window[0], self.window[1], self.growth_ISW, obsparams['a_grid'],
                                             obsparams['perturb'])
        # cls = []
        # for ell in ells:
        #     cl = cosmo.projection.cl_limber(ell,self._weight_function_clustering,self.params.a_grid,linear)
        #     cls.append(cl)
        # cls = np.array(cls)

        return cls

    def cl(self, ells, cosmo, obsparams):
        """
        Wrapper around all the other cl routines which determines from the
        obsparams dictionary for which cosmological probes the angular power
        spectrum has to be computed.
        This is especially useful when interfacing with CosmoHammer.
        :param ells: array of angular multipoles ell
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param obsparams: dictionary containing specifications for observable
        :return cls: array of values of the angular power spectrum for the desired probes for ells
        """

        self.setup(obsparams)

        if obsparams['probes'].count(obsparams['probes'][0]) == len(obsparams['probes']):
            # We want to compute an auto power spectrum
            if obsparams['probes'][0] == 'deltag':
                cls = self._cl_lss(ells, cosmo, obsparams)
                # Apply a galaxy bias correction if desired
                cls *= obsparams['bias']**2
            elif obsparams['probes'][0] == 'gamma':
                cls = self._cl_lss(ells, cosmo, obsparams)
                # Apply a multiplicative bias correction of desired
                cls *= (1.+obsparams['m'])**2
            elif obsparams['probes'][0] == 'cmbkappa':
                cls = self._cl_lss(ells, cosmo, obsparams)
                # Apply a CMB lensing convergence amplitude correction if desired
                cls *= obsparams['Akcmb']**2
            else:
                print('Only galaxy overdensity, cosmic shear and CMB lensing auto power spectra'
                      'supported.')
                return
        else:
            # We want to compute a cross power spectrum
            # First transform the list to a set; this is an unordered list which
            # can be compared to other sets without caring for the order
            probes = set(obsparams['probes'])
            if probes == set(['temp', 'deltag']):
                cls = self._cl_ISW(ells, cosmo, obsparams)
                # Apply a galaxy bias correction of desired
                cls *= obsparams['bias']
            elif probes == set(['temp', 'gamma']):
                cls = self._cl_ISW(ells, cosmo, obsparams)
                # Apply a multiplicative bias correction of desired
                cls *= (1.+obsparams['m'])
            elif probes == set(['deltag', 'gamma']):
                cls = self._cl_lss(ells, cosmo, obsparams)
                # Apply a galaxy bias correction of desired
                cls *= obsparams['bias']
                # Apply a multiplicative bias correction of desired
                cls *= (1.+obsparams['m'])
            elif probes == set(['temp', 'cmbkappa']):
                cls = self._cl_ISW(ells, cosmo, obsparams)
                # Apply a CMB lensing convergence amplitude correction if desired
                cls *= obsparams['Akcmb']
            elif probes == set(['deltag', 'cmbkappa']):
                cls = self._cl_lss(ells, cosmo, obsparams)
                # Apply a galaxy bias correction of desired
                cls *= obsparams['bias']
                # Apply a CMB lensing convergence amplitude correction if desired
                cls *= obsparams['Akcmb']
            elif probes == set(['gamma', 'cmbkappa']):
                cls = self._cl_lss(ells, cosmo, obsparams)
                # Apply a multiplicative bias correction of desired
                cls *= (1.+obsparams['m'])
                # Apply a CMB lensing convergence amplitude correction if desired
                cls *= obsparams['Akcmb']
            else:
                print('Only cross correlations between CMB temperature/CMB kappa and galaxy density,'
                      'CMB temperature/CMB kappa and cosmic shear, galaxy density and cosmic'
                      'shear and CMB temperature and CMB kappa are currently supported.')
                return

        return cls

    def cl_IG(self, ells, cosmo, obsparams):
        """
        Calculate the angular power spectrum for GI intrinsic alignments (IAs) using the NLA or LA model for the multipole
        array specified by ells. The NLA implementation follows Hildebrandt et al., 2016
        :param ells: array of angular multipoles ell
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param obsparams: dictionary containing specifications for observable
        :return cls: array of values of the angular power spectrum for GI IAs for ells
        """

        self.setup(obsparams)

        ells = np.atleast_1d(ells)
        F = partial(self.F, obsparams=obsparams)

        probes = set(obsparams['probes'])
        if probes == set(['gamma', 'gamma']):
            # GI term between intrinsic alignments and weak lensing shear
            iawindows = [0 for i in range(4)]
            iawindows[0] = self.window[0]
            iawindows[1] = self.n[1]
            iawindows[2] = self.window[1]
            iawindows[3] = self.n[0]

            cls = np.zeros_like(ells)
            for i in [0, 2]:
                cls = cls + cosmo.projection.cl_limber_IG(ells, iawindows[i], iawindows[i + 1], F, obsparams['a_grid'],
                                                          obsparams['IAmodel'])
            # Apply a multiplicative bias correction of desired
            cls *= (1.+obsparams['m'])**2

        elif probes == set(['deltag', 'gamma']):
            # Cross-correlation between intrinsic alignments and galaxies causing these or also
            # tracing the DM halo
            ind1 = obsparams['probes'].index('deltag')
            ind2 = obsparams['probes'].index('gamma')
            iawindows = [0 for i in range(2)]
            iawindows[0] = self.window[ind1]
            iawindows[1] = self.n[ind2]

            cls = cosmo.projection.cl_limber_IG(ells, iawindows[0], iawindows[1], F, obsparams['a_grid'],
                                                obsparams['IAmodel'])
            # Apply a galaxy bias correction of desired
            cls *= obsparams['bias']
            # Apply a multiplicative bias correction of desired
            cls *= (1.+obsparams['m'])

        elif probes == set(['cmbkappa', 'gamma']):
            # Cross-correlation between intrinsic galaxy alignments and CMB convergence;
            # this is because both are produced by the same structures
            ind1 = obsparams['probes'].index('cmbkappa')
            ind2 = obsparams['probes'].index('gamma')
            iawindows = [0 for i in range(2)]
            iawindows[0] = self.window[ind1]
            iawindows[1] = self.n[ind2]

            cls = cosmo.projection.cl_limber_IG(ells, iawindows[0], iawindows[1], F, obsparams['a_grid'],
                                                obsparams['IAmodel'])
            # Apply a multiplicative bias correction of desired
            cls *= (1.+obsparams['m'])
            # Apply a CMB lensing convergence amplitude correction if desired
            cls *= obsparams['Akcmb']
        else:
            print('Only intrinsic alignments between weak lensing/weak lensing, weak lensing/galaxy density, '
                  'and weak lensing/CMB kappa are supported.')
            return

        return cls

    def cl_II(self, ells, cosmo, obsparams):
        """
        Calculate the angular power spectrum for II intrinsic alignments (IAs) using the NLA or LA model for the
        multipole array specified by ells. The NLA implementation follows Hildebrandt et al., 2016
        :param ells: array of angular multipoles ell
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param obsparams: dictionary containing specifications for observable
        :return cls: array of values of the angular power spectrum for II IAs for ells
        """

        self.setup(obsparams)

        ells = np.atleast_1d(ells)
        F = partial(self.F, obsparams=obsparams)

        probes = set(obsparams['probes'])
        if probes == set(['gamma', 'gamma']):
            iawindows = [0 for i in range(2)]
            iawindows[0] = self.n[0]
            iawindows[1] = self.n[1]
        else:
            print('II correlation only exists for gamma x gamma.')
            return

        cls = cosmo.projection.cl_limber_II(ells, iawindows[0], iawindows[1], F, obsparams['a_grid'],
                                            obsparams['IAmodel'])
        # Apply a multiplicative bias correction of desired
        cls *= (1.+obsparams['m'])**2

        return cls

    def F(self, a, cosmo, obsparams):
        """
        Return the F function of the linear alignment model. This follows Eq. (8) of Hildebrandt et al.
        Here we set eta = beta = 0 i.e. no redshift and luminosity dependence
        :param a: array of scale factor values
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :param obsparams: dictionary containing specifications for observable
        :return f: value of f at scale factors a
        """

        C1 = self.C1(cosmo)
        rhocrit = self.rhocrit(cosmo)

        if obsparams['fzmodel'] == 'old':
            # Formula for f before the erratum of Hirata & Seljak, 2004
            f = (-1)*C1*rhocrit*cosmo.background._H2_H02_Omegam_a(a=a) /\
                (cosmo._lin_pert.growth_a(a=a)/a)

        elif obsparams['fzmodel'] == 'corr':
            # Formula for f after correction of Hirata & Seljak, 2010
            f = (-1)*C1*rhocrit*cosmo.params.omega_m/cosmo._lin_pert.growth_a(a=a)

        return f

    def C1(self, cosmo):
        """
        Return the linear intrinsic alignment amplitude C1.
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :return c1: linear intrinsic alignment amplitude for current value of h
        """

        c1 = 5.*10**-14*cosmo.params.h**-2*Msun**-1

        return c1

    def rhocrit(self, cosmo):
        """
        Return the critical density of the Universe at a0 = 1
        :param cosmo: instance of PyCosmo.Cosmo (specifies cosmological model)
        :return rhoc: critical density today, [rhoc] = kg/Mpc^3
        """

        rhoc = 3.*((cosmo.params.h*100)*10**3)**2/(8.*np.pi*G)  # factor 1000 converts from km to m
        # Convert rhoc to kg/Mpc^3
        rhoc *= Mpc2m

        return rhoc

    # def (self, cosmo, thetas, output_cls=True, linear=False, ells=None, cls=None, lmax=None):
    #     """Calculates the theory prediction for the cosmic shear correlation function
    #     xip = <gamma_t gamma_t> + <gamma_cross gamma_cross>
    #     xim = <gamma_t gamma_t> - <gamma_cross gamma_cross>
    #     based on the relations:
    #     xip = int dl l/(2 pi) J0(l theta) * [P_E(l) + P_B(l)]
    #     xim = int dl l/(2 pi) J4(l theta) * [P_E(l) - P_B(l)]
    #     where we set P_B(l) = 0
    #     :param: cosmo: instance of cosmo class
    #     :param: thetas: array of angular separations [arcmin]
    #     :param: output_cls: flag indicating if cls are output as well [1]
    #     :param: linear: flag indicating if linear or nonlinear power spectrum is used [1]
    #     :return: xi: dictionary xi with structure depending on output_cls
    #         if output_cls=True: xi = {theta [arcmin], xip, xim, ells, cls}
    #         if output_cls=False: xi = {theta [arcmin], xip, xim}
    #     """
    #
    #     # Calculate the cls for a large enough l range
    #     if cls is None:
    #         if lmax is None:
    #             # Default lmax and resolution - chosen to allow the integration for low and high theta to be
    #             # performed on the same grid
    #             #TODO: This scale needs to be thoroughly checked
    #             lmax = 2.*10**4
    #
    #         ells = np.linspace(1, lmax+1, int(lmax/10.)+1)
    #         cls = self._cl_weak_lensing(cosmo,ells,linear)
    #
    #     xips, xims, xip_integrand, xim_integrand = cosmo.projection._cl2xis(thetas, ells, cls)
    #
    #     if output_cls:
    #         xi = {'theta': thetas, 'xip': xips, 'xim': xims, 'ell': ells, 'cl': cls}
    #     else:
    #         xi = {'theta': thetas, 'xip': xips, 'xim': xims}
    #
    #     return xi
    #
    # def xi2cl(self, cosmo, ells, thetas, xips=None, xims=None):
    #     """Calculates the theory prediction for the cosmic shear cls from the
    #     correlation functions xip, xim using:
    #     cl = int dtheta (2 pi) * theta * xip(theta) * J0(l theta)
    #     cl = int dtheta (2 pi) * theta * xim(theta) * J4(l theta)
    #     This function is mainly used for debugging/testing.
    #     :param: ells: array of inverse angular scales [1]
    #     :param: thetas: array of angular separations [arcmin]
    #     :param: xips: xips, can be set to None, then only xims is used [1]
    #     :param: xims: xims, can be set to None, then only xips is used [1]
    #     :return: cls: array of cls [1]
    #     """
    #
    #     cls_xim, cls_xip = cosmo.projection._xi2cl(ells, thetas, xips, xims)
    #
    #     return cls_xim, cls_xip
    #
    # def xip2xim(self, cosmo, thetas, xip):
    #     """Computes xim from xip using the orthonormality relations for the Bessel function
    #     xim(theta) = xip(theta) + int_0_theta d phi phi/theta^2 xip(phi) (4-12 phi^2/theta^2)
    #     :param: theta: array of angular separations [arcmin], needs to start at zero and be fine ![arcmin]
    #     :param xip: xip shear correlation function [1]
    #     :return: xim: cosmic shear correlation function xim [1] """
    #
    #     xims = cosmo.projection._xip2xim(thetas, xip)
    #
    #     return xims
    #
    # def xim2xip(self, cosmo, thetas, xim):
    #     """Computes xim from xip using the orthonormality relations for the Bessel function
    #     xip(theta) = xim(theta) + int_theta_infty d phi 1/phi xip(phi) (4-12 theta^2/phi^2)
    #     :param: theta: array of angular separations [arcmin], needs to start at zero and be fine ![arcmin]
    #     :param xim: xim shear correlation function [1]
    #     :return: xip: cosmic shear correlation function xip [1] """
    #
    #     xips = cosmo.projection._xim2xip(thetas, xim)
    #
    #     return xips
    #
