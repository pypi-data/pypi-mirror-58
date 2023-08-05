import numpy as np


class RedshitDistribution(object):
    """
    Will be used to manage and deal with the
    redshift distributions that are needed for calculating
    observable quantities.

    """

    def __init__(self, params):
        self.params = params
        self._enrich_params(params)

    def _enrich_params(self, params):

        # To do think about the bounds of this
        self.params.pz_norm = self._calc_pz_int()
        self.params.pz_mean = self._calc_pz_mean()

        pass


    def pz_global(self, z=0.5, norm=True):
        # Todo need to think about default of a (like the Cosmo Class) or z?
        # a = np.atleast_1d(a)

        # z = (1./a) - 1.0

        distribution_type = ['smail']

        assert self.params.zdist_type.lower() in distribution_type, \
            'The redshift distribution type in input parameters is not recognised. Use one of the following: \n %s ' \
            % distribution_type

        if self.params.zdist_type.lower() == 'smail':
            assert np.all([hasattr(self.params, 'z0'), hasattr(self.params, 'beta'), hasattr(self.params, 'alpha')]), \
                'Make sure the Smail distribution parameters z0, alpha and beta are included in the params file'

            pz = np.exp(-(z / self.params.z0) ** self.params.beta) * z ** self.params.alpha
        else:
            pz = None

        if norm is True:
            pz = pz / self.params.pz_norm

        return pz

    def _pchi_global(self,chi,cosmo):
        """

        :return:
        """
        #Todo need get rid of hardcoded numbers
        #Todo figure out when to set up the a_vec and chi_vec
        if not np.all([hasattr(self,'a_vec') ,hasattr(self,'chi_vec')]):
            self.a_vec = np.logspace(0,-4,num = 1000)
            self.chi_vec = cosmo.background.dist_rad_a(self.a_vec)

        a = np.interp(chi,self.chi_vec,self.a_vec)
        z = 1./a - 1.0
        # import pdb; pdb.set_trace()

        return self.pz_global(z)*cosmo.background.H_a(a)


    def weight_function(self, chi,cosmo, window_type=None):
        """
        Calculates the radial weight functions for particular type of measure. This will be used
        to calculate the angular powerspectra
        :return:
        """
        if window_type is None:
            window_type = self.params.experiment_type

        if window_type.lower() == 'galaxy clustering':
            window = self._pchi_global(chi,cosmo)
        else:
            window = None

        return window


    def _calc_pz_int(self):
        z = np.linspace(0., 100., num=100000.)
        pz_temp = self.pz_global(z=z, norm=False)
        return np.trapz(pz_temp, z)


    def _calc_pz_mean(self):
        z = np.linspace(0., 100., num=100000.)
        pz_temp = self.pz_global(z=z, norm=True)
        return np.trapz(pz_temp*z, z)

