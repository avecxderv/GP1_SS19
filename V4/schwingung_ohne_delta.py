#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:23:18 2019

@author: simon
"""


from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt
from mittel import gewichtetes_mittel_in_aus 

dic = {1:'daten/schwingung_1Ohm_',2:'daten/schwingung_5.1Ohm_',3:'daten/schwingung_10Ohm_',
        4:'daten/schwingung_20Ohm_',5:'daten/schwingung_47Ohm_',6:'daten/schwingung_100Ohm_'}


#Frequenzen mit FFT bestimmen
res_fft = np.full((6,3),0.5)
efft = np.full((6,3),0.5)
for i in range(1,7,1):
    for j in range(1,4,1):
        data = cassy.CassyDaten(dic[i]+str(j)+'.lab')
        time = data.messung(1).datenreihe('t').werte
        vol = data.messung(1).datenreihe('U_B1').werte
        freq, amp = analyse.fourier_fft(time,vol)
        peak = analyse.peakfinder_schwerpunkt(freq[2:500],amp[2:500])
        ymax = amp.argmax()
        res_fft[i-1][j-1] = peak
        efft[i-1][j-1] = np.abs(freq[ymax]-peak)
        
        '''
        #Plot
        plt.plot(freq[0:100],amp[0:100])
        plt.axvline(x = freq[ymax], color='red', linestyle='--')
        plt.axvline(x= peak, color='green', linestyle='-.')
        plt.xlabel('Frequenz / Hz')
        plt.ylabel('Amplitude')
        plt.rcParams["figure.figsize"] = (12,6)
        plt.rcParams['axes.titlesize'] = 'large'
        plt.rcParams['axes.labelsize'] = 'large'
        plt.tight_layout()
        plt.xlim(0,5000)
        plt.grid()
        plt.text(15000,0.8*amp[ymax],s='Peak='+"{0:.1f}".format(freq[ymax]) + ' Hz',fontsize='13',color='red')
        plt.text(15000,0.75*amp[ymax],s='Peak-Schwerpunkt='+"{0:.1f}".format(peak) + ' Hz',fontsize='13',color='green')
        plt.savefig('plots/fft/fft_schwingung'+str(i)+"_"+str(j)+'.pdf', format='pdf', dpi=1200)
        #plt.show()
        plt.close()
        '''
fr = np.full((6,2),0.1)
for i in range(0,6,1):
    mu, inn, aus = gewichtetes_mittel_in_aus(res_fft[i],efft[i])
    fr[i][0] = mu
    fr[i][1] = max(inn,aus)
freq = np.array([fr[0][0],fr[1][0],fr[2][0],fr[3][0],fr[4][0]])
efreq = np.array([fr[0][1],fr[1][1],fr[2][1],fr[3][1],fr[4][1]])
R = np.array([1.008,5.101,9.99,19.82,46.67])
eR = np.array([0.001,0.001,0.002,0.01,0.01])
plt.errorbar(R**2,freq**2, yerr = efreq*2*freq, xerr = 2*eR*R)