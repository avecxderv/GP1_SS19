# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:51:05 2019

@author: Marius
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt


'''
# Rohdaten
data = cassy.CassyDaten('daten/schwebung_ohne2_1.lab')
time = data.messung(1).datenreihe('t').werte
vol1 = data.messung(1).datenreihe('U_A1').werte
vol2 = data.messung(1).datenreihe('U_A2').werte

fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize=(12,6))

ax1.plot(1000*time,vol1)
ax1.set_ylabel('$U_1$ / V')

ax2.plot(1000*time, vol2)
ax2.set_ylabel('$U_2$ / V')
ax2.set_xlabel('$t$ / ms')
ax2.set_xlim(0,20)

plt.subplots_adjust(hspace=0)
#plt.savefig('plots/schwebung_roh.pdf', format='pdf', dpi=1200)
plt.show()
'''

'''
# Beispiel zur Bestimmung von Delta t
data = cassy.CassyDaten('daten/schwebung_ohne2_1.lab')
time = data.messung(1).datenreihe('t').werte
vol1 = data.messung(1).datenreihe('U_A1').werte
vol2 = data.messung(1).datenreihe('U_A2').werte

fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize=(12,6))

ax1.plot(1000*time,vol1)
ax1.set_ylabel('$U_1$ / V')
ax1.grid(which='both')
ax1.axhline(y=0.06, color='black', linestyle='--')
ax1.axvline(x=2.4, color='red')
ax1.axvline(x=2.5, color='red', linestyle='--')
ax1.axvline(x=2.3, color='red', linestyle='--')

ax2.plot(1000*time, vol2)
ax2.set_ylabel('$U_2$ / V')
ax2.set_xlabel('$t$ / ms')
ax2.set_xlim(0,5)
ax2.set_xticks(np.arange(0,5.1,0.1), minor=True)
ax2.set_xticks(np.arange(0,5.1,0.2))
ax2.grid(which='both')
ax2.axvline(x=2.0, color='red')
ax2.axvline(x=2.1, color='red', linestyle='--')
ax2.axvline(x=1.9, color='red', linestyle='--')

plt.subplots_adjust(hspace=0)
plt.savefig('plots/delta_t_bsp.pdf', format='pdf', dpi=1200)
plt.show()
'''



fplus = np.array([])
fminus = np.array([])

dic_file = {1:'ohne2', 2:'ohne3', 3:'eisen2'}
dic_fre = {1: np.array([57,67,70,78]), 2:np.array([64,68,68,72]), 3:np.array([20,29,40,49])}

freqs = np.array([])
amps = np.array([])

for i in range(1,4,1):
    data = cassy.CassyDaten('daten/schwebung_' + dic_file[i] + '_1.lab')
    time = data.messung(1).datenreihe('t').werte
    vol = data.messung(1).datenreihe('U_A1').werte
    vol2 = data.messung(1).datenreihe('U_A2').werte
    
    freq, amp = analyse.fourier_fft(time, vol)
    freq2, amp2 = analyse.fourier_fft(time, vol2)
    (freq, amp) = analyse.untermenge_daten(freq, amp, 0, 50000)
    (freq2, amp2) = analyse.untermenge_daten(freq2, amp2, 0, 50000)
    peak1 = analyse.peakfinder_schwerpunkt(freq[dic_fre[i][0]:dic_fre[i][1]], amp[dic_fre[i][0]:dic_fre[i][1]])
    peak2 = analyse.peakfinder_schwerpunkt(freq[dic_fre[i][2]:dic_fre[i][3]], amp[dic_fre[i][2]:dic_fre[i][3]])
    ymax1 = amp[dic_fre[i][0]:dic_fre[i][1]].argmax()
    ymax2 = amp[dic_fre[i][2]:dic_fre[i][3]].argmax()
    
    fplus = np.concatenate((fplus, np.array([peak1, np.abs(peak1-freq[dic_fre[i][0]+ymax1])])))
    fminus = np.concatenate((fminus, np.array([peak2, np.abs(peak2-freq[dic_fre[i][2]+ymax2])])))
    
    amps = np.concatenate((amps, amp))
    freqs = np.concatenate((freqs, freq))

''' 
# FFT der verschiedenen Konfigurationen  
plt.figure(figsize=(12,6))    
    
plt.plot(freqs[4002:6002], amps[4002:6002], color='green', label='Schwebung 3')
plt.plot(freqs[2001:4001], amps[2001:4001], color='orange', label='Schwebung 2')
plt.plot(freqs[0:2000], amps[0:2000], color='blue', label='Schwebung 1')

plt.xlim(0, 4000)
plt.xlabel('Frequenz / Hz')
plt.ylabel('Amplitude')

# Peaks
plt.axvline(x=fplus[0], color='blue', linestyle='--')
plt.axvline(x=fminus[0], color='blue', linestyle='--')
plt.axvline(x=fplus[2], color='orange', linestyle='--')
plt.axvline(x=fminus[2], color='orange', linestyle='--')
plt.axvline(x=fplus[4], color='green', linestyle='--')
plt.axvline(x=fminus[4], color='green', linestyle='--')

plt.legend()
plt.savefig('plots/FFT_schwebungen.pdf', format='pdf', dpi=1200)
plt.show()
'''


# Berechne Kopplungsgrad k und dessen Fehler
i = np.arange(0,3,1)                
k = (fminus[2*i]**2 - fplus[2*i]**2)/(fminus[2*i]**2+fplus[2*i]**2)
temp = (4*fminus[2*i]*fplus[2*i])/((fminus[2*i]**2+fplus[2*i]**2)**2)
ek = temp*np.sqrt(fplus[2*i]**2*fminus[2*i+1]**2 + fminus[2*i]**2*fplus[2*i+1]**2)

'''
data = cassy.CassyDaten('daten/schwebung_eisen2_1.lab')
time = data.messung(1).datenreihe('t').werte
vol = data.messung(1).datenreihe('U_A1').werte

freq, amp = analyse.fourier_fft(time, vol)
(freq, amp) = analyse.untermenge_daten(freq, amp, 0, 50000)
plt.plot(freq, amp)
plt.xlim(0,5000)
#plt.axvline(x=peak1, color='black', linestyle='--')
#plt.axvline(x=peak2, color='black', linestyle='--')
    
plt.show()
'''