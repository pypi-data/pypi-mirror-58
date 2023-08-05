__author__ = 'AR & AA'

from recfast4py import recfast
import numpy as np
from ._scipy_utils import interp1d

class Recombination:
    """
    Compute recombination and thermodynamic variables as a function of redshift. This is
    based on a call to RECFAST++.
    """
    #TODO: add reference for RECFAST++ and also make it compatible with other recombination codes

    def __init__(self,params):

        # initialise
        self.params = params

        # call RECFAST++ to compute reionisation history tables
        #TODO: change name from RECFAST to RECFAST++ in code
        #TODO: check F and fDM parameters
        # print('Calculating recombination with RECFAST++')

        self.z,self.xe_h,self.xe_he,self.xe,self.tm = recfast.Xe_frac(self.params.Yp,
                                                                      self.params.Tcmb,
                                                                      self.params.omega_m, 
                                                                      self.params.omega_b, 
                                                                      self.params.omega_l,
                                                                      self.params.omega_k,
                                                                      self.params.h,
                                                                      self.params.Nnu,
                                                                      self.params.F,    # F and fDM need testing
                                                                      self.params.fDM)
        self.a=1./(1.+np.array(self.z))     # scale factor [1]

        # build functions of arbitrary a by interpolating and extrapolating for early times
        # TODO: document these functions
        # TODO: check that this extrapolation ot max value at high z and that xe=1.2>1 at early times is OK
        self.xe_a=interp1d(self.a,self.xe,bounds_error=False,fill_value=np.max(self.xe))            # total free electron fraction Xe [1]
        self.xe_h_a=interp1d(self.a,self.xe_h,bounds_error=False,fill_value=np.max(self.xe_h))      # H free electron fraction XeH [1]
        self.xe_he_a=interp1d(self.a,self.xe_he,bounds_error=False,fill_value=np.max(self.xe_he))   # He free electron fraction XeHe [1]

        # Compute logarithmic derivative of the baryon temperature
        lna=np.log(self.a)
        n_a=self.a.size
        dlntmdlna=np.zeros(n_a)        # logarithmic derivative dTm_dln(a) of the baryon temperature [1]
        a_dlntmdlna=np.zeros(n_a)
        for i in range(0,n_a-1):
            a_dlntmdlna[i]=np.exp(0.5*(lna[i]+lna[i+1]))
            dlntmdlna[i]=(np.log(self.tm[i+1])-np.log(self.tm[i]))/(lna[i+1]-lna[i])
        a_dlntmdlna[n_a-1]=1.  # fill in a=1 value - Warning: a bit dangerous
        dlntmdlna[n_a-1]=-2.
        dlntmdlna_max=np.max(dlntmdlna)
        self.dlntmdlna_a=interp1d(a_dlntmdlna,dlntmdlna,bounds_error=False,fill_value=dlntmdlna_max)  # d(Tm)/d(ln a) [1]

    def taudot_a(self,a):
        """
        Return tau_dot the derivative of the optical depth with respect to conformal time
        :param a:
        ;return: taudot: tou_dot=d(tau)/d(eta) [h Mpc^-1]
        """

        taudot_norm=self.params.sigmat*(self.params.rho_crit*self.params.msun/self.params.mpc**3)/(self.params.mp*1e6*self.params.evc2)  # sigma_thomson*rho_crit/m_p= 7.471e-28 h^2 m^-1
        return -taudot_norm * self.params.mpc / a**2 * self.xe_a(a) * self.params.omega_b * self.params.h * (1.-self.params.Yp) # [h Mpc^-1] (see Dodelson eq. 3.44, p73) + 1-Y factor from COSMICS)

    def tm_a(self, a):
        #TODO: should probably rename this temperature as Tb
        #TODO: see if this can be gotten from recfast++
        """
        Return the Baryon (matter) temperature as a function of the scale factor a,
        by interpolating (or extrapolating for early times) the recombination tables.
        :param a: scale factor [1]
        :return: Baryon (matter) temperature Tm [K]
        """

        aa=np.array(a)
        n_a=aa.size
        tm=np.zeros(n_a)
        for i in range(0,n_a):
            if aa[i]<np.min(self.a):
                tm[i] = self.params.Tcmb/aa[i]     # extrapolate at early time by setting tm=t_gamma=TCMB_now/a
            else:
                tm[i] = np.exp(np.interp(np.log(aa[i]), np.log(self.a), np.log(self.tm)))    # interpolate from Recfast++ table
        return tm

    def mu_a(self,a):
        """
        Computes the dimensonless mean molecular weight. It can be multiplied by the hydrogen atom mass to express it in mass units.
        :param a: a - scale factor [1]
        :return: mu: dimensionless mean molecular weight [1] (multiply bu the hydrogen atom mass to express in units of mass)
        """
        
        #return 1. / ((1. + self.xe_a(a)) * (1.-self.params.Yp) + 0.25 * self.params.Yp)
        return 1. / ((1. + self.xe_h_a(a)) * (1.-self.params.Yp) + 0.25 * (1.+2.*self.xe_he_a(a)) * self.params.Yp)

    def cs_a(self, a):
        """
        Returns the baryon sound speed
        :param a: scale factor [1]
        :return : cs: baryon sound speed [1]

        """

        return  np.sqrt(self.params.kb * self.tm_a(a) / self.mu_a(a) / (self.params.mp*1e6) * (1. - self.dlntmdlna_a(a) / 3.))
