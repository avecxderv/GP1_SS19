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
ed5 =  0.0019e-1
d6 = 11.978e-1
ed6 = 5.6218e-4
d9 = 11.944e-1
ed9 = 3.0358e-5
d11 = 11.989e-1
ed11 = 6.4265e-5

m5 = 1295
m6 = 1237.2
m9 = 407.3
m11 = 1157.6

el = 0.69e-3
em = 0.1e-3/np.sqrt(12)

rho_cu = 4*m5/(np.pi*d5**2*l5)
rho_messing = 4*m6/(np.pi*d6**2*l6)
rho_al = 4*m9/(np.pi*d9**2*l9)
rho_stahl = 4*m11/(np.pi*d11**2*l11)

'''
data = cassy.CassyDaten('daten/Nr11_4.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
fourier = analyse.fourier_fft(timeVal, voltage)
freq = fourier[0]
amp = fourier[1]
peak = analyse.peakfinder_schwerpunkt(freq[1200:1600],amp[1200:1600])

plt.plot(freq[0:8000],amp[0:8000])
'''

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