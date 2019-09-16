#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:19:03 2019

@author: simon
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

data = cassy.CassyDaten('daten/mittel_20_3.lab')
timeVal = data.messung(1).datenreihe('t').werte
pres = data.messung(1).datenreihe('p_A1').werte
f, (ax1,ax2) = plt.subplots(2,1)
ax1.plot(timeVal,pres,color='red')
freq, amp = analyse.fourier_fft(timeVal,pres)
ax2.plot(freq[0:8000],amp[0:8000],color='red')
ax1.set_ylabel("Druckdifferenz / hPa")
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("$f$ / Hz")
ax1.set_xlabel("$t$ / $s$")
ax1.set_xlim(0,8)
ax2.set_xlim(0,5)
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
f.tight_layout()
plt.savefig('plots/rohdaten.pdf')
plt.show()
plt.close()