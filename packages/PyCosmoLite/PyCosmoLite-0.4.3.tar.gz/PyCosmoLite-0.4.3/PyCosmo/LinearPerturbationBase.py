
import numpy as np
import six

from .PerturbationBase import ClassContractMeta, check_protypes, prototype


@six.add_metaclass(ClassContractMeta)
class LinearPerturbationBase(object):

    """
    created to manage which method is used to do the linear perturbation
    calculations. The options we expect to have are (i) full
    calculations solving the Boltz equations (ii) approximations based
    on fits and (iii) tabulated results for fast access.
    """

    def __new__(clz, *a, **kw):
        check_protypes(clz)
        return super(LinearPerturbationBase, clz).__new__(clz)

    # todo: sigma_r needs to be speeded up and made robust
    # todo: merge this with sigma8
    def sigma_r(self, r=8., a=1.0):
        """Calculates the rms of the density field on a given scale"""
        r = np.atleast_1d(r)
        # TODO: numpy based vecoriztion !
        res = np.zeros(shape=r.shape)
        for i in range(0, len(r)):
            ri = r[i]
            k = np.logspace(-5., 2., num=5000)  # grid of wavenumber k [Mpc^-1]
            lnk = np.log(k)
            w = (
                3. / (k * ri) ** 2 * (np.sin(k * ri) / (k * ri) - np.cos(k * ri))
            )  # top hat window function
            pk = self.powerspec_a_k(a=1., k=k)
            res[i] = np.trapz(k ** 3 * pk[:, 0] * w ** 2, lnk)

        return np.sqrt(1. / (2. * np.pi ** 2) * res)

    def _sigma_intg(self, lnk, r, a):
        """"Integrand for calculating sigma of the density field"""
        k = np.exp(lnk)
        w = 3. / (k * r) ** 2 * (np.sin(k * r) / (k * r) - np.cos(k * r))
        pk_temp = self.powerspec_a_k(a=a, k=k)
        return k ** 3 * pk_temp[0, :] * w ** 2

    def sigma8(self):
        """
        Compute sigma8, the rms density contrast fluctuation smoothed
        with a top hat of radius 8 h^-1 Mpc. This specialised routine is
        to be used for the normalisation of the power spectrum.

        :param: none
        :return: sigma8 [1]
        """

        # TODO: reuse sigma_r ?
        r = 8. / self._params.h  # smoothing radius [Mpc]
        k = np.logspace(-5., 2., num=5000)  # grid of wavenumber k [Mpc^-1]
        lnk = np.log(k)
        w = (
            3. / (k * r) ** 2 * (np.sin(k * r) / (k * r) - np.cos(k * r))
        )  # top hat window function
        pk = self.powerspec_a_k(a=1., k=k)
        res = np.trapz(k ** 3 * pk[:, 0] * w ** 2, lnk)
        return np.sqrt(1. / (2. * np.pi ** 2) * res)

    @prototype
    def growth_a(self, a=1.0, k=None, norm=0, verbose=False):
        pass

    @prototype
    def transfer_k(self, k):
        pass

    def powerspec_a_k(self, a=1.0, k=0.1, diag_only=False):
        a = np.atleast_1d(a)
        k = np.atleast_1d(k)
        if diag_only:
            assert len(a) == len(k)
        T_k = self.transfer_k(k=k)
        growth = self.growth_a(a, k=1)
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
