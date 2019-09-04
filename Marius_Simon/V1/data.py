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
data = cassy.CassyDaten('daten3.lab')
timeVal = data.messung(2).datenreihe('t').werte
voltage = data.messung(2).datenreihe('U_A1').werte

#Fouriertransoformation
fourier = analyse.fourier_fft(timeVal,voltage)
frequency = fourier[0]
amplitude = fourier[1]
plt.plot(frequency, amplitude)
plt.grid()
plt.xlabel('Frequenz / Hz')
plt.ylabel('Amplitude')

maximumIndex = amplitude.argmax();
plt.xlim(frequency[max(0, maximumIndex-10)], frequency[min(maximumIndex+10, len(frequency))])
peak = analyse.peakfinder_schwerpunkt(frequency, amplitude)
plt.axvline(peak)
omega_fft = 2*np.pi*peak

#Bestimmte Zeitpunkte der Maxima in s
n = np.arange(0,200,10)
n[0] = 1
period = [1.5, 16.44, 33.01, 49.59, 66.14, 82.73, 99.32,
          115.86, 132.46, 149.05, 165.64, 182.18, 198.8,
          215.34, 231.92, 248.47, 265.08, 281.62, 298.23,
          314.83]
eperiod = np.full((20,),0.02)

#Lineare Regression der Daten zur Bestimmung der Frequenz
res = analyse.lineare_regression(n,period,eperiod)
omega = 2*np.pi/res[0]

#Gebe das chi^2 an
print('chi^2/ndf:')
print(res[4]/18)

stor1 = np.power(omega,2)
stor2 = 1+0.5*np.power(rp,2)/np.power(lp,2)
g_fft = np.power(omega_fft,2)*lp*stor2
g = stor1*lp*stor2
eg = np.sqrt(np.power(res[1],2)*4*stor1*np.power(lp,2)*np.power(stor2,2)+
             np.power(0.00069,2)*stor1*np.power(1-0.5*np.power(rp,2)/np.power(lp,2),2))