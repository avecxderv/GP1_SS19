# -*- coding: utf-8 -*-

from praktikum import analyse
import numpy as np
import matplotlib.pyplot as plt
import scipy.odr

delta = np.array([ 341.01810569, 565.81381857, 860.23879874, 1421.9702776,2820.46265235])
edelta = np.array([ 0.25891746,  0.56634525,  1.25160131,  3.57130468, 16.18687673])
omega = 2*np.pi*np.array([1696.93,1696.33,1695.12,1689.19,1628.66])
eomega = 2*np.pi*np.array([0.599133,0.695859,0.991429,2.12677,4.84287])

omega2 = omega**2
eomega2 = 2*omega*eomega

delta2 = delta**2
edelta2 = 2*delta*edelta

# Lineare Regression mit festgesetzer Steigung -1
def lineare_regression_minus1(x,y,ex,ey):

    def f(B, x):
        return -x + B[0]

    model  = scipy.odr.Model(f)
    data   = scipy.odr.RealData(x, y, sx=ex, sy=ey)
    odr    = scipy.odr.ODR(data, model, beta0=[0])
    output = odr.run()
    ndof = len(x)-1
    chiq = output.res_var*ndof

    return output.beta[0], np.sqrt(output.cov_beta[0,0]), chiq


# Regression
reg = lineare_regression_minus1(delta2, omega2, edelta2, eomega2)


# Kapazitaet berechnen
L = 0.008759471427456488
eL = 0.000079
C = 1/(L*reg[0])
eC = C*np.sqrt( (reg[1]/reg[0])**2 + (eL/L)**2)

# Plot
fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize=(12,6), gridspec_kw={'height_ratios': [5, 2]})

ax1.errorbar(delta2,omega2, color='red', xerr=edelta2, yerr=eomega2, fmt='.', marker='o', markeredgecolor='red')
ax1.plot(delta2, -delta2+reg[0], color='black', linestyle='--')
ax1.set_ylabel('$\omega^2$ / $1/s^2$')
ax1.text(0.97,0.92,s='Steigung: ' + str(-1) + ' (festgesetzt)', 
         fontsize = '13', color='blue',ha='right',transform=ax1.transAxes)
ax1.text(0.97,0.85,s='y-Achsenabschnitt: (' + "{0:.3f}".format(reg[0]) + r'$\pm$' + "{0:.3f}".format(reg[1]) + ')$1/s^2$', 
         fontsize = '13', color='blue',ha='right',transform=ax1.transAxes)
ax1.text(0.97,0.78,s='$\chi^2$/ndf: ' + "{0:.1f}".format(reg[2]/4),
         fontsize = '13', color='blue',ha='right',transform=ax1.transAxes)
reserr = np.sqrt(edelta2**2 + eomega2**2)
ax2.errorbar(delta2, omega2+delta2-reg[0], yerr=reserr, color='red', fmt='.', marker='o', markeredgecolor='red')
ax2.axhline(y=0, color='black', linestyle='--')
ax2.set_xlabel('$\delta^2$ / $1/s^2$')
ax2.set_ylabel('$\omega^2 + \delta^2 - \omega_0^2$ / $1/s^2$')
#Plotparameter
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.subplots_adjust(hspace=0)
#plt.savefig('plots/reg_delomega.pdf', format='pdf', dpi=1200)
plt.show()

