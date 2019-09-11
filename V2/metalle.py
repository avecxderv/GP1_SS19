#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:22:34 2019

@author: simon
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

#Gemessene Groessen
#5 = Kupfer, 6 = Messing, 9 = Alu, 11 = Stahl

l5 = 129.9
l6 = 130
l9 = 129.9
l11 = 130.1

d5 = 11.991e-1
ed5 =  0.0801e-1
d6 = 11.978e-1
ed6 = 0.0042e-1
d9 = 11.944e-1
ed9 = 0.031e-1
d11 = 11.989e-1
ed11 = 0.0451e-1

m5 = 1295
m6 = 1237.2
m9 = 407.3
m11 = 1157.6

el = 0.69e-3
em = 0.1e-3/np.sqrt(12)

rho_cu = 4*m5/(np.pi*d5**2*l5)
erho_cu = rho_cu*np.sqrt( 0.1**2/(m5**2) + 0.0069**2/(l5**2) + 4*(ed5**2)/(d5**2))
rho_messing = 4*m6/(np.pi*d6**2*l6)
erho_messing = rho_messing*np.sqrt( 0.1**2/(m6**2) + 0.0069**2/(l6**2) + 4*ed6**2/(d6**2))
rho_al = 4*m9/(np.pi*d9**2*l9)
erho_al = rho_al*np.sqrt( 0.1**2/(m9**2) + 0.0069**2/(l9**2) + 4*(ed9**2)/(d9**2))
rho_stahl = 4*m11/(np.pi*d11**2*l11)
erho_stahl = rho_stahl*np.sqrt( 0.1**2/(m11**2) + 0.0069**2/(l11**2) + 4*ed11**2/(d11**2))

'''
#Plot Rohdaten
data = cassy.CassyDaten('daten/Nr5_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
f, (ax1,ax2) = plt.subplots(2,1)
ax1.plot(timeVal,voltage)
ax1.set_ylabel("Schalldruck")
ax2.set_ylabel("Schalldruck")
ax2.plot(timeVal[0:250], voltage[0:250])
ax2.set_xlabel("$t$ / $s$")
ax1.set_xlim(0,1.6)
ax2.set_xlim(0,0.025)
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.savefig('plots/rohdaten.pdf')
plt.show()
plt.close()
'''

'''
#Beispiel Sepektrum
data = cassy.CassyDaten('daten/Nr5_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
fourier = analyse.fourier_fft(timeVal, voltage)
freq = fourier[0]
amp = fourier[1]
plt.plot(freq[0:8000],amp[0:8000], color='orange')
plt.xlim(0,5000)
plt.xlabel('$f$ / Hz')
plt.ylabel('Amplitude')
plt.grid()
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.savefig('plots/spektrum1.pdf')
'''


data = cassy.CassyDaten('daten/Nr5_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
fourier = analyse.fourier_fft(timeVal, voltage)
freq = fourier[0]
amp = fourier[1]
plt.scatter(freq,amp,color='orange')
maximumIndex = amp.argmax();
plt.xlim(freq[max(0, maximumIndex-10)], freq[min(maximumIndex+10, len(freq))])
peak = analyse.peakfinder_schwerpunkt(freq, amp)
plt.axvline(peak, linestyle= "--",color='black')
#plt.plot(freq[0:8000],amp[0:8000])




f0_5 = [1458.77, 1458.8, 1458.82, 1458.83, 1458.83]
f_5 = np.sum(f0_5)/5
v_5 = 2*l5*1e-2*f_5

f0_6 = [1348.16, 1348.13, 1348.12, 1348.12, 1348.08]
f_6 = np.sum(f0_6)/5
v_6 = 2*l6*1e-2*f_6

f0_9 = [1966.17, 1966.29, 1966.34, 1966.35, 1966.52]
f_9 = np.sum(f0_9)/5
v_9 = 2*l9*1e-2*f_9

f0_11 = [1883.91, 1883.94, 1883.97, 1884, 1883.95]
f_11 = np.sum(f0_11)/5
v_11 = 2*l11*1e-2*f_11