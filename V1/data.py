# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

#gemessene Laengen
rp = 0.5*0.07995
lp = 0.615+0.02535+rp

#Daten laden
data_s = cassy.CassyDaten('daten1.lab')
data_p = cassy.CassyDaten('daten2.lab')
timeVal = data_s.messung(1).datenreihe('t').werte
voltage_s = data_s.messung(1).datenreihe('U_A1').werte
voltage_p = data_p.messung(1).datenreihe('U_A1').werte

#Bestimmte Zeitpunkte der Maxima in s
n = np.arange(0,200,10)
n[0] = 1
period_p = [0.48, 15.38, 31.94, 48.48, 65.04, 81.56, 98.11, 114.68,
            131.28, 147.84, 164.36, 180.9, 197.46, 214.02, 230.56,
            247.12, 263.68, 280.22, 296.8, 313.34]

period_s = [1.5, 16.44, 33.01, 49.59, 66.14, 82.73, 99.32,
          115.86, 132.46, 149.05, 165.64, 182.18, 198.8,
          215.34, 231.92, 248.47, 265.08, 281.62, 298.23, 314.83]

eperiod_p = np.full((20,),0.02)
eperiod_s = np.full((20,),0.02)

nreg = np.arange(0,200,1)

#Lineare Regression der Daten zur Bestimmung der Frequenz
res_p = analyse.lineare_regression(n,period_p,eperiod_p)
omega_p = 2*np.pi/res_p[0]
eomega_p = 2*np.pi/(res_p[0]**2)*res_p[1]
res_s = analyse.lineare_regression(n,period_s,eperiod_s)
omega_s = 2*np.pi/res_s[0]
eomega_s = 2*np.pi/(res_s[0]**2)*res_s[1]

"""
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', gridspec_kw={'height_ratios': [5, 2]})
ax1.plot(nreg,res_p[0]*nreg+res_p[2], linestyle="--", color = 'black')
ax1.errorbar(n,period_p, yerr = 0.02, color='red', fmt='.', marker ='o')
ax1.set_ylabel('$t$ / $s$')
ax1.grid()
ax1.set_ylim(-10,350)
ax1.set_title('Messung mit Pendelkörper')

ax2.plot(nreg,res_s[0]*nreg+res_s[2], linestyle="--", color = 'black')
ax2.errorbar(n,period_s, yerr = 0.02, color='red', fmt='.', marker = 'o')
ax2.grid()
ax2.set_title('Messung ohne Pendelkörper')

ax3.axhline(y=0., color='black', linestyle='--')
ax3.errorbar(n, period_p-(res_p[0]*n+res_p[2]), yerr=eperiod_p, color='red', fmt='.', marker='o', markeredgecolor='red')
ax3.set_xlim(0,200) 
ax3.set_xlabel('Anzahl an Schwingungen')
ax3.set_ylabel('($t - (T\, n + t_{off})$) / s')

ax4.axhline(y=0., color='black', linestyle='--')
ax4.errorbar(n,period_s-(res_s[0]*n+res_s[2]), yerr=eperiod_s, color='red', fmt='.', marker='o', markeredgecolor='red')
ax4.set_xlim(0,200)
ax4.set_xlabel('Anzahl an Schwingungen')

plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.tight_layout()
f.subplots_adjust(hspace=0.0)
plt.savefig('plots/regression.pdf', format='pdf', dpi=1200)
plt.close(f)
"""

#Fouriertransoformationen
f, (ax1,ax2) = plt.subplots(2,1, sharex='all')
fourier = analyse.fourier_fft(timeVal,voltage_p)
frequency = fourier[0]
amplitude = fourier[1]
ax1.scatter(frequency, amplitude,color='red')
ax1.grid()
ax1.set_ylabel('Amplitude')

maximumIndex = amplitude.argmax();
ax1.set_xlim(frequency[max(0, maximumIndex-10)], frequency[min(maximumIndex+10, len(frequency))])
peak_p = analyse.peakfinder_schwerpunkt(frequency, amplitude)
ax1.axvline(peak_p, linestyle="--",color='black')

fourier2 = analyse.fourier_fft(timeVal, voltage_s)
frequency2 = fourier2[0]
amplitude2 = fourier2[1]
ax2.scatter(frequency2, amplitude2, color='red')
ax2.grid()
ax2.set_xlabel('Frequenz / Hz')
ax2.set_ylabel('Amplitude')

maximumIndex = amplitude2.argmax();
ax2.set_xlim(frequency2[max(0, maximumIndex-10)], frequency2[min(maximumIndex+10, len(frequency2))])
peak_s = analyse.peakfinder_schwerpunkt(frequency2, amplitude2)
ax2.axvline(peak_s, linestyle= "--",color='black')

plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.tight_layout()
f.subplots_adjust(hspace=0.0)
plt.close(f)

#Gebe das chi^2 an
print('chi_p^2/ndf:')
print(res_p[4]/18)
print('chi_s^2/ndf:')
print(res_s[4]/18)

releomega = 0.2*np.abs(omega_p**2-omega_s**2)/omega_p**2

stor1 = np.power(omega_p,2)
stor2 = 1+0.5*np.power(rp,2)/np.power(lp,2)
g = stor1*lp*stor2
eg = np.sqrt(eomega_p**2*4*stor1*np.power(lp,2)*np.power(stor2,2) +
     np.power(0.0007,2)*stor1**2*np.power(1-0.5*np.power(rp,2)/np.power(lp,2),2))