__author__ = 'AR & AA'

import numpy as np

#TODO do we want to change the name so that it is easier to PyCsomo.Cosmo with tab completion
class cosmics: # wrapper for the Cosmics package - simple version only for outputs

    def __init__(self,cosmics_dir):
        """
        """
        print 'reading COSMICS tables'
        #cosmics_dir='cosmics-1.04/bin/'
        # read in input file
        input=np.loadtxt(cosmics_dir+'input.dat',skiprows=3)   # read table
        self.z_end=input[3]
        self.a_end=1./(1.+self.z_end)
        input=np.genfromtxt(cosmics_dir+'input.dat',skip_footer=2)
        self.omega_b=input[0,0]
        self.omega_c_0=input[0,1]
        self.omega_l=input[0,2]
        self.H0=input[1,0]
        self.h=self.H0/100.
        self.Yp=input[1,2]
        # read linger.dat
        #head=np.loadtxt(cosmics_dir+'linger.dat')   # read header  - seems unstable
        #self.H0=head[1,0]      # H0 [km/s/Mpc]
        #head=np.genfromtxt(cosmics_dir+'linger.dat',skip_footer=30,skip_header=1)  # caution: this is not robust
        #self.H0=head[0]      # H0 [km/s/Mpc]
        head = open(cosmics_dir+'linger.dat')  # read header
        head_line1 = head.readline()
        head_line2 = head.readline()
        head.close()
        x2 = np.fromstring(head_line2, sep=' ')
        self.H0=x2[0]
        self.h=self.H0*.01   # h [1]      # warning: looks like we need to read in double precision
        trans=np.loadtxt(cosmics_dir+'linger.dat',skiprows=2)   # read table
        self.k=trans[:,1]/self.h   # k [h Mpc^-1]
        self.a=trans[:,2]           # final scale factor a for k value [1]
        self.eta=trans[:,3]*self.h  # final conformal time eta for k value [h^-1 Mpc]
        self.phi_mb=trans[:,5]         # Phi (MB95 conventions)
        self.deltac=trans[:,6]     # delta_c  - warning: need delta_m
        self.deltab=trans[:,7]     # delta_b
        self.deltam=(self.omega_c_0*self.deltac+self.omega_b*self.deltab)/(self.omega_c_0+self.omega_b)   # delta_m
        self.deltag=trans[:,8]     # delta_g=Theta0*4. (photon density)
        self.deltar=trans[:,9]     # delta_r=N0*4. (massless neutrino density)
        self.thc=trans[:,11]    # theta_c=u*k (DM velocity)
        self.thb=trans[:,12]    # theta_b=ub*k (baryon velocity)
        self.thg=trans[:,13]    # theta_g=Theta1*3k (photon velocity)
        self.thr=trans[:,14]    # theta_r=N1*3k (massless neutrino velocity)
        self.shearg=trans[:,16]       # photon shear
        self.shearr=trans[:,17]       # massless neutrino shear
        self.econ=trans[:,19]   # energy conservation
        # convert to Dodelson conventions
        self.phi=-self.phi_mb                   # Phi
        self.u=self.thc/self.k/self.h           # u (DM velocity)
        self.ub=self.thb/self.k/self.h          # ub (velocity velocity)
        self.theta0=self.deltag/4.              # theta_0 (photon monopole)
        self.theta1=self.thg/3./self.k/self.h   # theta_1 (photon dipole)
        self.theta2=self.shearg/2.              # theta_2
        self.n0=self.deltar/4.                  # N_0 (massless neutrino monopole)
        self.n1=self.thr/3./self.k/self.h       # N_1 (massless neutrino dipole)
        self.n2=self.shearr/2.                  # N_2
        self.theta3=trans[:,20]/4.              # theta_3
        self.n3=trans[:,21]/4.                  # N_3
        self.thetap0=trans[:,22]/4.              # thetap_0
        self.thetap1=trans[:,23]/4.              # thetap_1
        self.thetap2=trans[:,24]/4.              # thetap_2

        # arrange in field dictionnary
        #nk=len(self.k)
        #self.field={'phi':np.array(-self.phi).reshape(nk,1),'delta':np.array(self.deltac).reshape(nk,1),
        #        'u':np.array(self.u).reshape(nk,1),'deltab':np.array(self.deltab).reshape(nk,1),
        #        'ub':np.array(self.ub).reshape(nk,1),'theta0':np.array(self.theta0).reshape(nk,1),
        #        'theta1':np.array(self.theta1).reshape(nk,1),
        #        'n0':np.array(self.n0).reshape(nk,1),'n1':np.array(self.n1).reshape(nk,1),
        #        'k':np.array(self.k),'a':np.array(self.a_end)}
        # read initial conditions
        ic=np.loadtxt(cosmics_dir+'initial.dat',skiprows=2)
        self.k_ic=ic[:,0]/self.h    # k [h Mpc^-1]
        self.eta_ic=ic[:,1]*self.h         # conformal time eta [h^-1 Mpc]
        self.a_ic=ic[:,2]           # a
        self.phi_ic=-ic[:,3]         # phi (in dodelson convention)
        self.deltac_ic=ic[:,4]      # delta=delta_c
        self.deltab_ic=ic[:,6]      # delta_b
        self.deltag_ic=ic[:,8]      # delta_g
        self.theta0_ic=ic[:,8]/4.      # Theta0 (photon monopole)
        self.u_ic=ic[:,5]/self.k_ic/self.h      # u (DM velocity)
        self.ub_ic=ic[:,7]/self.k_ic/self.h      # ub (baryon velocity)
        self.thetag_ic=ic[:,9]        # photon velocity
        self.theta1_ic=ic[:,9]/3./self.k_ic/self.h # Theta1 (photon dipole)
        self.n2_ic=ic[:,10]/2.           # N_2 (massless neutrino quadrupole moment)
        self.grhom_ic=ic[:,11]         # grhom [Mpc^-2]
        self.grhog_ic=ic[:,12]         # grhog[Mpc^-2]
        self.grhor_ic=ic[:,13]         # grhor [Mpc^-2]
        self.grho_ic=ic[:,14]         # grho [Mpc^-2]
        self.gpres_ic=ic[:,15]         # gpres [Mpc^-2]
        self.s_ic=ic[:,16]              # s [Mpc^-2]
        self.fracnu_ic=ic[:,17]         # fracnu [1]
        self.yrad_ic=ic[:,18]         # yrad [1]
        self.econ_ic=ic[:,19]         # energy conservation [1]

        # read constants   - note: grhor seems corrupted
        cst=np.loadtxt(cosmics_dir+'constants.dat',skiprows=1)
        self.grhom=cst[0]           # 8*Pi*G*rho_crit/c^2  [Mpc^-2]
        self.grhog=cst[1]           # 8*Pi*G*rho_gam/c^2  [Mpc^-2]
        self.grhor=cst[2]           # 8*Pi*G*rho_neu/c^2  [Mpc^-2]

        # read thermo quantities
        thermo=np.loadtxt(cosmics_dir+'thermo.dat',skiprows=2)
        self.eta_th=thermo[:,0]*self.h     # conformal time eta [h^-1 Mpc]
        self.tempb_th=thermo[:,1]      # tempb
        self.cs2_th=thermo[:,2]     # cs^2
        self.xe_th=thermo[:,3]      # xe
        self.opaca2_th=thermo[:,4]    # opac*a^2=-taudot*a2 [Mpc^-1]
        #self.taudot_th=2.3048e-9*(1-self.Yp)*self.omega_b*self.H0**2/self.h*self.xe_th   # dtau/deta [h Mpc^-1]

        # read derivatives
        dv=np.loadtxt(cosmics_dir+'derivs.dat',skiprows=2)
        self.k_dv=dv[:,1]/self.h         # k [h Mpc^-1]
        self.a_dv=dv[:,2]               # a
        self.eta_dv=dv[:,3]*self.h      # conformal time eta [h^-1 Mpc]
        self.adot_dv=dv[:,4]        # da/deta [h Mpc^-1]
        self.phidot_dv=-dv[:,5]/self.h      # dphi/deta [h Mpc^-1]
        self.deltacdot_dv=dv[:,6]/self.h
        self.udot_dv=dv[:,7]/self.k/self.h/self.h    # du/deta [h Mpc^-1]
        self.deltabdot_dv=dv[:,8]/self.h    # ddeltab/deta [h Mpc^-1]
        self.ubdot_dv=dv[:,9]/self.k/self.h/self.h    # dub/deta [h Mpc^-1]
        self.theta0dot_dv=dv[:,10]/4./self.h   # dtheta0/deta [h Mpc^-1]
        self.theta1dot_dv=dv[:,11]/3./self.k/self.h/self.h   # dtheta1/deta [h Mpc^-1]
        self.theta2dot_dv=dv[:,12]/2./self.h   # dtheta2/deta [h Mpc^-1]
        self.n0dot_dv=dv[:,13]/4./self.h   # dn0/deta [h Mpc^-1]
        self.n1dot_dv=dv[:,14]/3./self.k/self.h/self.h   # dn1/deta [h Mpc^-1]
        self.n2dot_dv=dv[:,15]/2./self.h   # dn2/deta [h Mpc^-1]
        self.psi_dv=dv[:,16]    # psi [1]
        self.adotoa_dv=dv[:,17,]    # adotoa
        self.dgtheta_dv=dv[:,19]    # dgtheta
        self.dgshear_dv=dv[:,20]    # dgshear
