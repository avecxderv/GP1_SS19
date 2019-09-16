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

m = 16e-3
em = 0.1/np.sqrt(12)

def fft_analysis(groesse,hoehe,nummer):
    dataname = 'daten/' + groesse + '_' + hoehe + '_' + nummer + '.lab'
    data = cassy.CassyDaten(dataname)
    time = data.messung(1).datenreihe('t').werte
    volt = data.messung(1).datenreihe('p_A1').werte
    fourier = analyse.fourier_fft(time,volt)
    freq = fourier[0]
    amp = fourier[1]
    peak = analyse.peakfinder_schwerpunkt(freq[10:100],amp[10:100])
    return peak

def mittel(groesse,hoehe):
    #groesse ist aus {'kleine', 'grosse', 'mittel'}
    f = [fft_analysis(groesse,hoehe,'1'), fft_analysis(groesse,hoehe,'2'),
         fft_analysis(groesse,hoehe,'3'), fft_analysis(groesse,hoehe,'4'),
         fft_analysis(groesse,hoehe,'5')]
    ef = np.full((5,),0.5)
    return analyse.gewichtetes_mittel(f,ef)

f_kl_15 = mittel('kleine','15')
f_kl_20 = mittel('kleine','20')
f_kl_25 = mittel('kleine','25')
f_kl_30 = mittel('kleine','30')
f_kl_35 = mittel('kleine','35')
f_kl_40 = mittel('kleine','40')
f_kl_45 = mittel('kleine','45')