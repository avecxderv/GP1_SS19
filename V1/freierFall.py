# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from praktikum import analyse

# Daten der Messungen
s = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
t1 = np.array([0.1407, 0.2, 0.2456, 0.284, 0.318, 0.348, 0.3763, 0.4025, 0.427])
t2 = np.array([0.1408, 0.2, 0.2452, 0.2838, 0.3182, 0.3484, 0.3766, 0.4027, 0.4272])
t12 = t1*t1
t22 = t2*t2

# Unsicherheiten
sigmas = np.full((9,), 0.001)
sigmatOs = 0.0001
sigmatDz = 0.00029
sigmat2Os = 2*sigmatOs*t2
sigmat2Dz = 2*sigmatDz*t1

# Regressionen
m1, em1, b1, eb1, chi21, corr1 = analyse.lineare_regression_xy(t12, s, sigmat2Dz, sigmas)
print('m = (%g +- %g) m/s^2,   b = (%g +- %g) m,  chi2/dof = %g / %g  corr = %g' % (m1, em1, b1, eb1, chi21, len(t12)-2, corr1))
m2, em2, b2, eb2, chi22, corr2 = analyse.lineare_regression_xy(t22, s, sigmat2Os, sigmas)
print('m = (%g +- %g) m/s^2,   b = (%g +- %g) m,  chi2/dof = %g / %g  corr = %g' % (m2, em2, b2, eb2, chi22, len(t12)-2, corr2))

# Residuen fuer die Residuenplots
sigmaRes1 = np.sqrt((m1*sigmat2Dz)**2 + sigmas**2)
sigmaRes2 = np.sqrt((m2*sigmat2Os)**2 + sigmas**2)


# Alternative Auswertung
m = []
sigmam = []
for i in range(4):
	m.append((s[2+2*i]-s[1+2*i])/(t12[2+2*i]-t12[1+2*i]))
	sigrelt2 = 2*sigmatDz*np.sqrt(t12[2+2*i]+t12[1+2*i])/(t12[2+2*i]-t12[1+2*i])
	sigrels = np.sqrt(2)*sigmas[0]/(s[2+2*i]-s[1+2*i])
	sigmam.append(m[i]*np.sqrt(sigrelt2**2 + sigrels**2))
	print('m = (%g +- %g) m/s^2' %(m[i], sigmam[i]))
m = np.array(m)
sigmam = np.array(sigmam)
# Gewichtetes Mittel der Einzelwerte
w = 1/sigmam**2
sm = sum(w*m)
wsum = sum(w)
mm = sm/wsum
# Innerer und aeußerer Fehler des Mittelwertes
sigmammin = np.sqrt(1./wsum)
qm = (m-mm)**2
qmsum = sum(w*qm)
sigmamma = sigmammin*np.sqrt(1./3*qmsum)
print('mm = (%g +- %g(in) +- %g(auß)) m/s^2' %(mm, sigmammin, sigmamma))	


# Plot für Digitalzähler
fig1, ax1 = plt.subplots(2, 1, figsize=(12,6), sharex='all', gridspec_kw={'height_ratios': [5, 2]})

ax1[0].plot(t12, m1*t12+b1, linestyle="--", color = 'black')
ax1[0].errorbar(t12, s, xerr=sigmat2Dz, yerr=sigmas, color='red', fmt='.', marker ='o')
ax1[0].grid()
ax1[0].set_ylabel('$s$ / m', size=18)

ax1[1].axhline(y=0., color='black', linestyle='--')
ax1[1].errorbar(t12, s-(m1*t12+b1), yerr=sigmaRes1, color='red', fmt='.', marker='o', markeredgecolor='red')
ax1[1].set_xlabel('$t^2$ / s$^2$', size=18)
ax1[1].set_ylabel('$s-(mt^2+s_0)$ / m', size=18)


for tick in ax1[1].xaxis.get_major_ticks():
    tick.label.set_fontsize(18)

for tick in ax1[0].yaxis.get_major_ticks():
    tick.label.set_fontsize(18)

for tick in ax1[1].yaxis.get_major_ticks():
    tick.label.set_fontsize(18)

plt.tight_layout()

fig1.subplots_adjust(hspace=0.0)
plt.savefig('plots/regression_fF1.pdf', format='pdf', dpi=1200)
plt.close(fig1)

# Plot für Oszilloskop
fig2, ax2 = plt.subplots(2, 1, figsize=(12,6), sharex='all', gridspec_kw={'height_ratios': [5, 2]})

ax2[0].plot(t22, m2*t22+b2, linestyle="--", color = 'black')
ax2[0].errorbar(t22, s, xerr=sigmat2Os, yerr=sigmas, color='red', fmt='.', marker ='o')
ax2[0].grid()
ax2[0].set_ylabel('$s$ / m', size=18)

ax2[1].axhline(y=0., color='black', linestyle='--')
ax2[1].errorbar(t22, s-(m2*t22+b2), yerr=sigmaRes1, color='red', fmt='.', marker='o', markeredgecolor='red')
ax2[1].set_xlabel('$t^2$ / s$^2$', size=18)
ax2[1].set_ylabel('$s-(mt^2+s_0)$ / m', size=18)


for tick in ax2[1].xaxis.get_major_ticks():
    tick.label.set_fontsize(18)

for tick in ax2[0].yaxis.get_major_ticks():
    tick.label.set_fontsize(18)

for tick in ax2[1].yaxis.get_major_ticks():
    tick.label.set_fontsize(18)

plt.tight_layout()

fig2.subplots_adjust(hspace=0.0)
plt.savefig('plots/regression_fF2.pdf', format='pdf', dpi=1200)
plt.close(fig2)

