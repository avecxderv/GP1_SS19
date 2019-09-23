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

'''
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
        plt.text(3500,0.8*amp[ymax],s='Peak='+"{0:.1f}".format(freq[ymax]) + ' Hz',fontsize='13',color='red')
        plt.text(3500,0.75*amp[ymax],s='Peak-Schwerpunkt='+"{0:.1f}".format(peak) + ' Hz',fontsize='13',color='green')
        #plt.savefig('plots/fft/fft_schwingung'+str(i)+"_"+str(j)+'.pdf', format='pdf', dpi=1200)
        #plt.show()
        plt.close()
fr = np.full((6,2),0.1)
for i in range(0,6,1):
    mu, inn, aus = gewichtetes_mittel_in_aus(res_fft[i],efft[i])
    fr[i][0] = mu
    fr[i][1] = max(inn,aus)
freq = 2*np.pi*np.array([fr[0][0],fr[1][0],fr[2][0],fr[3][0],fr[4][0]])
efreq =2*np.pi*np.array([fr[0][1],fr[1][1],fr[2][1],fr[3][1],fr[4][1]])
'''

#Die in schwingung.py bestimmten Frequenzen werden von nun an verwendet:
freq = 2*np.pi*np.array([1696.93,1696.33,1695.12,1689.19,1628.66])
efreq = 2*np.pi*np.array([0.599133,0.695859,0.991429,2.12677,4.84287])
R = np.array([1.008,5.101,9.99,19.82,46.67])+4.93
eR = np.array([0.001,0.001,0.002,0.01,0.01])
delta = np.array([ 341.01810569, 565.81381857, 860.23879874, 1421.9702776,2820.46265235])
edelta = np.array([ 0.25891746,  0.56634525,  1.25160131,  3.57130468, 16.18687673])

k = np.sqrt(freq**2-delta**2)/(2*np.pi)

reg = analyse.lineare_regression_xy(R**2,freq**2,2*eR*R,efreq*freq*2)

ye = 2*efreq*freq
xe = 2*R*eR

f, (ax1 , ax2) = plt.subplots(2,1,sharex = 'col',gridspec_kw={'height_ratios': [5, 2]})
ax1.plot(R**2,(reg[0]*R**2+reg[2]), linestyle="--", color = 'black')
ax1.errorbar(R**2,freq**2, yerr = ye, xerr = xe, color='red', fmt='.', marker ='o')
ax1.grid()
ax1.text(0.97,0.92,s='Steigung: (' + "{0:.2f}".format(reg[0]) + r'$\pm$' + "{0:.2f}".format(reg[1]) + ')1/$\Omega$s', 
         fontsize = '13', color='blue',ha='right',transform=ax1.transAxes)
ax1.text(0.97,0.85,s='y-Achsenabschnitt: (' + "{0:.1f}".format(reg[2]) + r'$\pm$' + "{0:.1f}".format(reg[3]) + ')Hz', 
         fontsize = '13', color='blue',ha='right',transform=ax1.transAxes)
ax1.text(0.97,0.78,s='$\chi^2$/ndf: ' + "{0:.1f}".format(reg[4]/(3)),
         fontsize = '13', color='blue',ha='right',transform=ax1.transAxes)
ax1.set_ylabel('$\omega^2$ / $Hz^2$')
ax2.set_xlabel('$(R+R_0)^2$ / $\Omega^2$')
ax2.set_ylabel(r'$\omega^2 - \left(-\frac{1}{4L^2} (R+R_0)^2 + \omega_0^2\right)$ / $Hz^2$')
ax2.axhline(y=0., color='black', linestyle='--')
ax2.errorbar(R**2, (freq**2-(reg[0]*R**2+reg[2])), yerr=np.sqrt(xe**2+ye**2), color='red', fmt='.', marker='o', markeredgecolor='red')
plt.tight_layout()
#Plotparameter
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
f.subplots_adjust(hspace=0.0)
plt.savefig('plots/reg_Rome.pdf', format='pdf', dpi=1200)
#plt.close(f)