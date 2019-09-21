# -*- coding: utf-8 -*-

from praktikum import analyse
import numpy as np
import matplotlib.pyplot as plt
import scipy.odr

delta = np.array([3.475527699156500603e+02, 
         5.671994945727682307e+02, 
         8.622797075022784838e+02, 
         1.423902697807471668e+03, 
         2.817100889200921301e+03])

edelta = np.array([1.291419319783521091e+00,
          1.656171559933282467e+00,
          2.586223358873092959e+00,
          5.865760609950476656e+00,
          1.673288272530401599e+01])


T = 2*np.array([2.946493524283939403e-04,
     2.947543878945637903e-04,
     2.949642877086130002e-04,
     2.960000061041986744e-04,
     3.069999977014959834e-04])

eT = 2*np.array([1.040312973220598787e-07,
      1.209127083516686427e-07,
      1.725163898355886481e-07,
      3.726779962499649375e-07,
      9.128709291752770334e-07])

omega2 = 4*np.pi**2/(T**2)
eomega2 = 2*omega2*eT/T

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
L = 9e-3
C = 1/(L*reg[0])

# Plot
fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize=(12,6))

ax1.errorbar(delta2,omega2, color='red', xerr=edelta2, yerr=eomega2, fmt='.', marker='o', markeredgecolor='red')
ax1.plot(delta2, -delta2+reg[0], color='black', linestyle='--')

reserr = np.sqrt(edelta2**2 + eomega2**2)
ax2.errorbar(delta2, omega2+delta2-reg[0], yerr=reserr, color='red', fmt='.', marker='o', markeredgecolor='red')
ax2.axhline(y=0, color='black', linestyle='--')

plt.subplots_adjust(hspace=0)

plt.show()

