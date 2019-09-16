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
from scipy.optimize import curve_fit


# Grenzen bis zu denen die Schwingungen sauber sind
tgrenz = {'kleine_45_1': 2.8, 'kleine_45_2': 3.5, 'kleine_45_3': 3.5, 'kleine_45_4': 4.2, 'kleine_45_5': 3.6,
        'kleine_40_1': 4.0, 'kleine_40_2': 3.4, 'kleine_40_3': 2.8, 'kleine_40_4': 3.0, 'kleine_40_5': 4.5,
        'kleine_35_1': 3.1, 'kleine_35_2': 4.6, 'kleine_35_3': 4.1, 'kleine_35_4': 4.5, 'kleine_35_5': 4.2,
        'kleine_30_1': 4.6, 'kleine_30_2': 4.5, 'kleine_30_3': 4.7, 'kleine_30_4': 4.9, 'kleine_30_5': 4.8,
        'kleine_25_1': 4.7, 'kleine_25_2': 5.0, 'kleine_25_3': 4.3, 'kleine_25_4': 4.4, 'kleine_25_5': 4.6,
        'kleine_20_1': 5.0, 'kleine_20_2': 4.5, 'kleine_20_3': 5.5, 'kleine_20_4': 4.7, 'kleine_20_5': 5.8,
        'kleine_15_1': 4.5, 'kleine_15_2': 4.6, 'kleine_15_3': 4.7, 'kleine_15_4': 5.6, 'kleine_15_5': 4.4,
        'mittel_50_1': 3.2, 'mittel_50_2': 3.2, 'mittel_50_3': 3.2, 'mittel_50_4': 3.2, 'mittel_50_5': 3.2,
        'mittel_45_1': 5.7, 'mittel_45_2': 8.0, 'mittel_45_3': 4.8, 'mittel_45_4': 8.0, 'mittel_45_5': 8.0,
        'mittel_40_1': 8.0, 'mittel_40_2': 7.4, 'mittel_40_3': 8.0, 'mittel_40_4': 7.7, 'mittel_40_5': 8.0,
        'mittel_35_1': 8.0, 'mittel_35_2': 8.0, 'mittel_35_3': 8.0, 'mittel_35_4': 7.0, 'mittel_35_5': 8.0,
        'mittel_30_1': 6.1, 'mittel_30_2': 7.4, 'mittel_30_3': 8.0, 'mittel_30_4': 6.5, 'mittel_30_5': 6.8,
        'mittel_25_1': 8.0, 'mittel_25_2': 8.0, 'mittel_25_3': 8.0, 'mittel_25_4': 8.0, 'mittel_25_5': 8.0, 
        'mittel_20_1': 8.0, 'mittel_20_2': 4.3, 'mittel_20_3': 8.0, 'mittel_20_4': 8.0, 'mittel_20_5': 8.0, 
        'grosse_45_1': 8.0, 'grosse_45_2': 8.0, 'grosse_45_3': 8.0, 'grosse_45_4': 8.0, 'grosse_45_5': 8.0, 
        'grosse_40_1': 8.0, 'grosse_40_2': 8.0, 'grosse_40_3': 8.0, 'grosse_40_4': 8.0, 'grosse_40_5': 8.0, 
        'grosse_35_1': 8.0, 'grosse_35_2': 8.0, 'grosse_35_3': 8.0, 'grosse_35_4': 8.0, 'grosse_35_5': 8.0, 
        'grosse_30_1': 8.0, 'grosse_30_2': 8.0, 'grosse_30_3': 8.0, 'grosse_30_4': 8.0, 'grosse_30_5': 8.0, 
        'grosse_25_1': 8.0, 'grosse_25_2': 8.0, 'grosse_25_3': 8.0, 'grosse_25_4': 8.0, 'grosse_25_5': 6.9, 
        'grosse_20_1': 8.0, 'grosse_20_2': 8.0, 'grosse_20_3': 8.0, 'grosse_20_4': 8.0, 'grosse_20_5': 7.1}



m = 16e-3
em = 0.1/np.sqrt(12)

def func(x, a, b, c, d,e):
    return a*np.exp(-b*x)*np.sin(c*x+e) + d

def korrektur(time,pres):
    popt, pcov = curve_fit(func, time,pres)
    return popt[1]

def fft_analysis(groesse,hoehe,nummer):
    #Daten mit Korrektur
    dataname = groesse + '_' + hoehe + '_' + nummer
    
    data = cassy.CassyDaten('daten/' + dataname + '.lab')
    time = data.messung(1).datenreihe('t').werte
    pres = data.messung(1).datenreihe('p_A1').werte
    
    #Signale abschneiden
    time, pres = analyse.untermenge_daten(time, pres, 0, tgrenz[dataname])
    
    fourier = analyse.fourier_fft(time,pres)
    freq = fourier[0]
    amp = fourier[1]
    peak = analyse.peakfinder_schwerpunkt(freq[10:100],amp[10:100])
    kor = korrektur(time,pres)
    return np.sqrt(peak**2+kor**2)

def fft_analysis_ohnekor(groesse,hoehe,nummer):
    #Daten ohne Korrektur
    dataname = 'daten/' + groesse + '_' + hoehe + '_' + nummer + '.lab'
    data = cassy.CassyDaten(dataname)
    time = data.messung(1).datenreihe('t').werte
    pres = data.messung(1).datenreihe('p_A1').werte
    fourier = analyse.fourier_fft(time,pres)
    freq = fourier[0]
    amp = fourier[1]
    peak = analyse.peakfinder_schwerpunkt(freq[10:100],amp[10:100])
    return peak

def mittel(groesse,hoehe):
    #Standardmaessig mit Korrektur
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