__author__ = 'AR & AA'

import numpy as np
from _Cosmics import cosmics
import os

# TODO: tidy up this class

class ctable:   # table of precalculated quantities for the Boltzman integration
    def __init__(self,cosmo,aran=[1e-11,1.],na=1000):
        print 'building ctable'
        self.aran=aran    # range of a values in the table
        self.na=na        # number of a values in the table
        self.a=np.logspace(np.log10(aran[0]), np.log10(aran[1]), na) #  Warning: need to be careful about range
        self.lna = np.log(self.a)
        self.eta= np.array(cosmo.background._eta_a(self.a))
        self.etaran=[self.eta[0],self.eta[na-1]]

        # TODO: this choice should be made, if at all, in the recombination CLASS
        if cosmo.params.recomb=='recfast++':   # evaluate taudot and cs^2 internally (using recfast++)
            # TODO: enforce check on recfast++ table a range
            self.taudot= cosmo.background._rec.taudot(self.a)
            self.cs2 = cosmo.background._cs(self.a)**2

        if cosmo.params.recomb=='cosmics':     # warning: need to ensure a range is not outside cosmics table
            tab_cosmics=cosmics(os.path.join(os.path.dirname(__file__), cosmo.params.recomb_dir))
            if self.etaran[0] < np.min(tab_cosmics.eta_th) or self.etaran[1] > np.max(tab_cosmics.eta_th):
                print 'ctable: error: cosmics table interpolation out of bound'
                #print self.etaran[0],self.etaran[1],np.min(tab_cosmics.eta_th),np.max(tab_cosmics.eta_th)
                #sys.exit('ctable: error: cosmics table interpolation out of bound')
            self.cs2 = np.interp(self.eta,tab_cosmics.eta_th,tab_cosmics.cs2_th)
            #self.taudot= cosmo.rec.taudot(self.a, cosmo)   # temporary
            #self.taudot=2.3048e-9*(1-cosmo.Yp)*cosmo.omega_b*cosmo.H0**2/cosmo.h   # dtau/deta [h Mpc^-1]- Warning: should use COSMICS cosmo parameters, esp H0 whcih has been nudged in PyCosmo
            #self.taudot=-tab_cosmics.opaca2/tab_cosmics.h/self.a**2
            self.taudot=-np.interp(self.eta, tab_cosmics.eta_th, tab_cosmics.opaca2_th / tab_cosmics.h) / self.a**2   # [h Mpc^-1]

        if cosmo.params.recomb=='class':  # warning: need to ensure a range is not outside CLASS table
            # TODO: ensure a range is not outside CLASS table
            # TODO: to be safer use h values from class rather than from PyCosmo
            tab_class=np.loadtxt(os.path.join(os.path.dirname(__file__), cosmo.params.recomb_dir)+'test_thermodynamics.dat')
            #class_a=1./(1.+class_dat[:,0])  # a
            class_z=tab_class[:,0]                          # z [1]
            class_a=1./(1.+class_z)                               # a [1]
            class_eta=tab_class[:,1]*cosmo.params.h         # eta [h^-1 Mpc]
            class_taudot=tab_class[:,3]/cosmo.params.h      # -taudot [h Mpc^-1]
            #class_tb=tab_class[:,6]                        # baryon temperature [K]
            class_cs2=tab_class[:,7]                        # baryon sound speed squared [1]
            if self.etaran[0] < np.min(class_eta) or self.etaran[1] > np.max(class_eta):
                print 'ctable: error: CLASS table interpolation out of bound'
            # note: np.interp needs the table to be in same order as eta
            self.cs2=np.interp(self.eta,class_eta[::-1],class_cs2[::-1]*class_a[::-1])/self.a
            #self.taudot=-np.interp(self.eta,class_eta[::-1],class_taudot[::-1])
            self.taudot=-np.interp(self.eta,class_eta[::-1],class_taudot[::-1]*class_a[::-1]**2)/self.a**2   # extrapolate to constant taudot*a^2 at early times
            #self.class_eta=class_eta
            #self.class_taudot=class_taudot
            #self.class_cs2=class_cs2

