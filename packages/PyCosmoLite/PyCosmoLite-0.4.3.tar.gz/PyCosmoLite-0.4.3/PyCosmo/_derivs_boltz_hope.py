import hope
import numpy as np

# hope.config.cxxflags += ["-mllvm", "-force-vector-width=8", "-mllvm", "-force-vector-unroll=2", "-fslp-vectorize-aggressive"]


# @hope.jit
def _hubble(a, H0, rh, omega_r, omega_m, omega_k, omega_l):
    """
    HOPE friendly version of Background.hubble

    :param a:
    :param H0:
    :param rh:
    :param omega_r:
    :param omega_m:
    :param omega_k:
    :param omega_l:

    :return ha:
    """
    ha = (H0 *
          (omega_r * a ** -4 + omega_m * a ** -3 + omega_k * a ** -2 + omega_l) ** 0.5) / (H0 * rh)
    return ha


# @hope.jit
def _r_bph_a(a, omega_b, omega_gamma):
    """
    baryon to photon ratio

    :param a:
    :param omega_b:
    :param omega_gamma:
    """
    return 3. / 4. * omega_b / omega_gamma * a


# @hope.jit
def _f_boltz_nu_hope(y, x, dydlna, k, lmax, xc_damp, a_tca, xvar, eins, scalars, table_lna, table_eta, table_a, table_taudot, table_cs2, J):
    # k units: [h Mpc^-1]    - this version includes neutrinos and oscillation damping
    # y=[phi,delta,u,deltab,ub,theta_0,thetap_0,..,theta_lmax,thetap_lmax,n_0,..n_lmax] all real with u=i*v,ub=i*vb

    omega_k = scalars[0]
    omega_r = scalars[1]
    omega_m = scalars[2]
    H0 = scalars[3]
    rh = scalars[4]
    omega_gamma = scalars[5]
    omega_neu = scalars[6]
    omega_l = scalars[7]
    omega_b = scalars[8]
    omega_dm = scalars[9]

    # compute background quantities
    if xvar == 0:   # x=ln(a)
        lna = x
        a = np.exp(x)
        eta = np.interp(lna, table_lna, table_eta)
        dlnadx = 1.   # dln(a)/dx
    if xvar == 2:   # x=eta  [h^1 Mpc]
        eta = x
        a = np.interp(eta, table_eta, table_a)
        lna = np.interp(eta, table_eta, table_lna)

    ha = _hubble(a, H0, rh, omega_r, omega_m, omega_k, omega_l)
    if xvar == 2:
        dlnadx = a * ha  # dln(a)/dx=aH(a)   [h Mpc^-1]

    r_bph_a = _r_bph_a(a, omega_b, omega_gamma)

    tdot = np.interp(lna, table_lna, table_taudot)
    cs2 = np.interp(lna, table_lna, table_cs2)

    psi = -y[0] - 12. / (rh * k * a)**2 * (omega_gamma * y[9] + omega_neu * y[6 + 2 * lmax + 3])
    aha = a * ha
    k_aha = k / aha
    a2 = a * a
    a4 = a2 * a2

    # choose Einstein equation to use for integration
    if eins == 0:  # time-time equation
        dphidlna = psi - k * k / (3. * aha * aha) * y[0] \
                   + 0.5 / (ha * ha * rh * rh) * \
                   (
                      a * (omega_dm * y[1] + omega_b * y[3])
                      + 4. * (omega_gamma * y[5] + omega_neu * y[6 + 2 * lmax + 1])
                    ) / a4  # time-time einstein equation
    else:        # time-space equation
        dphidlna = -y[0] - 1 / (rh * k * a)**2 * (
                 12. * (omega_gamma * y[9] + omega_neu * y[6 + 2 * lmax + 3]) +
                 1.5 / ha * k * (omega_dm * y[2] + omega_b * y[4]
                                 + 4. / a * (omega_gamma * y[7] + omega_neu * y[6 + 2 * lmax + 2])
                                 )
                 )   # alternative einstein equation

    ppi = y[9] + y[6] + y[10]    # polarisation term

    dydlna[:] = 0

    dydlna[0] = dphidlna  # d/dlna[phi]
    dydlna[1] = -k_aha * y[2] - 3. * dphidlna  # d/dlna[delta]
    dydlna[2] = -y[2] + k_aha * psi  # d/dlna[u]
    dydlna[3] = -k_aha * y[4] - 3. * dphidlna  # d/dlna[deltab]

    w_c = 40.  # warning: set w_c=50, need to set as general parameter
    if xc_damp < 0 or (k * eta - xc_damp) / w_c < 20.:

        dydlna[5] = -k_aha * y[7] - dphidlna                                   # d/dlna[theta_0]
        if a < a_tca:   # use TCA approximation if appropriate and requested
            dh_dlna = -1. / (2. * ha) * (4. * omega_r * a**(-4) + 3. * omega_m * a **
                                   (-3) + 2. * omega_k* a **(-2)) / rh**2   # is this better?
            slip = 2. / (1. + r_bph_a) * (y[4] - 3. * y[7]) + 1. / tdot / (1 + 1. / r_bph_a) * ((2. * a * ha + a * dh_dlna) * y[4] + k * (
                2.*y[5]+psi) + k*(dydlna[5]-cs2*dydlna[3]))  # slip=dub/dln(a)-3 dtheta1/dln(a) to first orfer in tdot^-1
            # # d/dlna[ub] - could perhaps be combined to above equation for speed up
            dydlna[4] = -y[4]/(1.+1./r_bph_a)+k_aha*((y[5]-2.*y[9])/(1.+r_bph_a) +
                                                     psi + cs2/(1.+1./r_bph_a)*y[3])+slip/(1.+r_bph_a)
            # d/dlna[theta_1] - exact equation to implement TCA (should not make a difference)
            dydlna[7] = k/(3.*a*ha)*(y[5]-2.*y[9]+(1.+r_bph_a)*psi) - \
                r_bph_a/3.*(dydlna[4]+y[4] - k_aha*cs2*y[3])
            # dydlna[8] = k_aha/3.*(y[6]-2.*y[10])+tdot/aha*(y[8])            # d/dlna[thetap_1]  - note: higher photon moment derivatives set to 0
        # else:   # exact explicit equations (TCA off)
        if a >= a_tca:   # exact explicit equations (TCA off)
            dydlna[4] = -y[4]+k_aha*psi+tdot/r_bph_a/aha * \
                (y[4]-3.*y[7])+k_aha*y[3]*cs2  # d/dlna[ub] - new expression with cs term
            dydlna[6] = k_aha*(-y[8])+tdot/aha*(y[6]-ppi/2.)                # d/dlna[thetap_0]
            # d/dlna[theta_1] - exact equation to implement TCA (should not make a difference)
            dydlna[7] = k_aha / 3. * (y[5]-2.*y[9]+(1.+r_bph_a)*psi) - \
                r_bph_a/3.*(dydlna[4]+y[4] - k_aha * cs2 * y[3])
            dydlna[8] = k_aha/3.*(y[6]-2.*y[10])+tdot/(aha)*(y[8])            # d/dlna[thetap_1]
            dydlna[9] = k_aha / 5. * (2.*y[7]-3.*y[11])+tdot/aha*(y[9]-ppi/10.)  # d/dlna[theta_2]
            dydlna[10] = k_aha/5.*(2.*y[8]-3.*y[12])+tdot/aha*(y[10]-ppi/10.)  # d/dlna[thetap_2]
            f = 3
            for i in range(3, lmax):   # i=3..lmax-1
                dydlna[5+2*i] = k_aha / (2. * f + 1.)*(f * y[5+2*(i-1)] - (f + 1.)
                                                       * y[5+2*(i+1)]) + tdot/aha * y[5+2*i]  # d/dlna[theta_i]
                dydlna[6+2*i] = k_aha / (2. * f + 1.)*(f * y[6+2*(i-1)] - (f + 1.)
                                                       * y[6+2*(i+1)]) + tdot/aha * y[6+2*i]  # d/dlna[thetap_i]
                f += 1
            # d/dlna[theta_lmax] - truncate hierarchy
            dydlna[5+2*lmax] = 1./aha*(k*y[5+2*(lmax-1)]-((lmax+1.)/eta-tdot)*y[5+2*lmax])
            # d/dlna[thetap_lmax] - truncate hierarchy
            dydlna[6+2*lmax] = 1./aha*(k*y[6+2*(lmax-1)]-((lmax+1.)/eta-tdot)*y[6+2*lmax])

        dydlna[6+2*lmax+1] = -k_aha*y[6+2*lmax+2]-dphidlna                 # d/dlna[N_0]
        dydlna[6+2*lmax+2] = k_aha / 3. * (y[6+2*lmax+1]-2.*y[6+2*lmax+3]+psi)    # d/dlna[N_1]
        for j in range(2, lmax):   # j=2..lmax-1
            dydlna[6+2*lmax+1+j] = k_aha / \
                (2.*j+1.)*(j*y[6+2*lmax+1+j-1]-(j+1.)*y[6+2*lmax+1+j+1])  # d/dlna[N_l]
        # d/dlna[N_lmax] - truncate hierarchy
        dydlna[6+2*lmax+1+lmax] = 1. / aha * \
            (k*y[6+2*lmax+1+lmax-1]-(lmax+1.)/eta*y[6+2*lmax+1+lmax])

        if xc_damp > 0 and (k * eta - xc_damp) / w_c > -20.:
            dydlna[5:] = dydlna[5:] * 0.5 * (1. - np.tanh((k * eta - xc_damp) / w_c))

    else:

        if a < a_tca:   # use TCA approximation if appropriate and requested
            dh_dlna_1 = -1./(2.*ha)*(4.*omega_r*a**(-4)+3. * omega_m * a **
                                     (-3)+2.*omega_k*a**(-2))/rh**2   # is this better?
            slip_1 = 2./(1.+r_bph_a)*(y[4]-3.*y[7])+1./tdot/(1+1./r_bph_a)*((2.*a*ha + a*dh_dlna_1)*y[4]+k*(
                2.*y[5]+psi) + k*(dydlna[5]-cs2*dydlna[3]))  # slip=dub/dln(a)-3 dtheta1/dln(a) to first orfer in tdot^-1
            # # d/dlna[ub] - could perhaps be combined to above equation for speed up
            dydlna[4] = -y[4]/(1.+1./r_bph_a)+k_aha*((y[5]-2.*y[9])/(1.+r_bph_a) +
                                                     psi + cs2/(1.+1./r_bph_a)*y[3])+slip_1/(1.+r_bph_a)
        # else:   # exact explicit equations (TCA off)
        if a >= a_tca:   # exact explicit equations (TCA off)
            dydlna[4] = -y[4]+k_aha*psi+tdot/r_bph_a/aha * \
                (y[4]-3.*y[7])+k/aha*y[3]*cs2  # d/dlna[ub] - new expression with cs term

    dydlna *= dlnadx
    return dydlna

#
