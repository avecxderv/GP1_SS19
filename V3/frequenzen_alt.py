
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



m = 0.0165
em = 0.0001/np.sqrt(12)
p0 = 99400
d = 16e-3
ed = 0.01e-3/np.sqrt(12)
A = np.pi*d**2/4
rho_h20 = 997
V_kl = (0.4545-0.1457)/rho_h20
V_mi = (1.456-0.3403)/rho_h20
V_gr = 0.011315

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
    peak = analyse.peakfinder_schwerpunkt(freq[3:100],amp[3:100])
    delta = korrektur(time,pres)
    return (2*np.pi*peak, delta)

def mittel(groesse,hoehe):
    #groesse ist aus {'kleine', 'grosse', 'mittel'}
    w = [fft_analysis(groesse,hoehe,'1')[0], fft_analysis(groesse,hoehe,'2')[0],
         fft_analysis(groesse,hoehe,'3')[0], fft_analysis(groesse,hoehe,'4')[0],
         fft_analysis(groesse,hoehe,'5')[0]]
    
    delta = [fft_analysis(groesse,hoehe,'1')[1], fft_analysis(groesse,hoehe,'2')[1],
             fft_analysis(groesse,hoehe,'3')[1], fft_analysis(groesse,hoehe,'4')[1],
             fft_analysis(groesse,hoehe,'5')[1]]
    
    wm, sw = analyse.mittelwert_stdabw(w)
    deltam, sdelta = analyse.mittelwert_stdabw(delta)
    sw = sw/np.sqrt(5)
    sdelta = sdelta/np.sqrt(5)
    print(wm)
    print(sw)
    print(deltam)
    print(sdelta)
    return np.sqrt(wm**2+deltam**2), 2*np.sqrt((wm*sw)**2+(deltam*sdelta)**2)/np.sqrt(wm**2+deltam**2)

groesse='kleine'
w_15, ew_15 = mittel(groesse,'15')
w_20, ew_20 = mittel(groesse,'20')
w_25, ew_25 = mittel(groesse,'25')
w_30, ew_30 = mittel(groesse,'30')
w_35, ew_35 = mittel(groesse,'35')
w_40, ew_40 = mittel(groesse,'40')
w_45, ew_45 = mittel(groesse,'45')
#w_50, ew_50 = mittel(groesse,'50')
#ew = np.array([ew_20,ew_25,ew_30,ew_35,ew_40,ew_45])
w = np.array([w_15,w_20,w_25,w_30, w_35,w_40,w_45])
ew = np.array([ew_15,ew_20, ew_25, ew_30, ew_35, ew_40, ew_45])

x = 1/(w**2)
ex = ew/(w**3)
hoehen = np.array([0.15,0.20,0.25,0.30,0.35,0.40,0.45])
y = V_gr + A*hoehen
ey = np.sqrt(2*(em/rho_h20)**2 + (ed*np.pi*d/2*hoehen)**2)

#Regression für V
res = analyse.lineare_regression_xy(x,y,ex,ey)
fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
ax1.plot(x,res[0]*x+res[2], linestyle="--", color = 'black')

err = np.sqrt((ex*res[0])**2 + ey**2)
ax1.errorbar(x,y, yerr=err, color='red', fmt='.', marker='o', markeredgecolor='red')
ax2.errorbar(x, y-(res[0]*x+res[2]), yerr=err, color='red', fmt='.', marker='o', markeredgecolor='red')
ax2.axhline(y=0, color='black', linestyle='--')

plt.show()