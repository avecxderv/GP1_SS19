# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:48:00 2019

@author: Marius
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt


'''
# Rohdaten
data = cassy.CassyDaten('daten/fundamental_1.lab')
time = data.messung(1).datenreihe('t').werte
vol1 = data.messung(1).datenreihe('U_A1').werte
vol2 = data.messung(1).datenreihe('U_A2').werte

fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize=(12,6))

ax1.plot(1000*time,vol1)
ax1.set_ylabel('$U_1$ / V')
ax1.grid()

ax2.plot(1000*time, vol2)
ax2.set_ylabel('$U_2$ / V')
ax2.set_xlabel('$t$ / ms')
ax2.set_xlim(0,10)
ax2.grid()

plt.subplots_adjust(hspace=0)
plt.savefig('plots/fundamental_roh.pdf', format='pdf', dpi=1200)
plt.show()
'''

# Frequenzspektrum
data1 = cassy.CassyDaten('daten/fundamental_3.lab')
time1 = data1.messung(1).datenreihe('t').werte
vol1_1 = data1.messung(1).datenreihe('U_A1').werte
vol1_2 = data1.messung(1).datenreihe('U_A2').werte
fre1_1, amp1_1 = analyse.fourier_fft(time1, vol1_1)
fre1_2, amp1_2 = analyse.fourier_fft(time1, vol1_2)

data2 = cassy.CassyDaten('daten/fundamental_2.lab')
time2 = data2.messung(1).datenreihe('t').werte
vol2_1 = data2.messung(1).datenreihe('U_A1').werte
vol2_2 = data2.messung(1).datenreihe('U_A2').werte
fre2_1, amp2_1 = analyse.fourier_fft(time2, vol2_1)
fre2_2, amp2_2 = analyse.fourier_fft(time2, vol2_2)

peak1_1 = analyse.peakfinder_schwerpunkt(fre1_1[5:600], amp1_1[5:600])
peak1_2 = analyse.peakfinder_schwerpunkt(fre1_2[5:600], amp1_2[5:600])
peak2_1 = analyse.peakfinder_schwerpunkt(fre2_1[5:600], amp2_1[5:600])
peak2_2 = analyse.peakfinder_schwerpunkt(fre2_2[5:600], amp2_2[5:600])


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex='col', sharey='row',figsize=(12,6))

ax1.plot(fre1_1[0:600], amp1_1[0:600])
ax1.set_ylabel('Amplitude')
ax1.axvline(x=peak1_1, color='black', linestyle='--')
ax1.axvline(x=peak2_1, color='gray', linestyle='--')
ax1.text(100,1000,s='peak ='+"{0:.2f}".format(peak1_1)+' Hz',fontsize='13')

ax2.plot(fre1_2[0:600], amp1_2[0:600])
ax2.axvline(x=peak1_2, color='black', linestyle='--')
ax2.axvline(x=peak2_2, color='gray', linestyle='--')
ax2.text(100,1000,s='peak ='+"{0:.2f}".format(peak1_2)+' Hz',fontsize='13')

ax3.plot(fre2_1[0:600], amp2_1[0:600])
ax3.set_xlim(0,3500)
ax3.set_xlabel('Frequenz / Hz')
ax3.set_ylabel('Amplitude')
ax3.axvline(x=peak2_1, color='black', linestyle='--')
ax3.axvline(x=peak1_1, color='gray', linestyle='--')
ax3.text(100,900,s='peak ='+"{0:.2f}".format(peak2_1)+' Hz',fontsize='13')

ax4.plot(fre2_2[0:600], amp2_2[0:600])
ax4.set_xlim(0,3500)
ax4.set_xlabel('Frequenz / Hz')
ax4.axvline(x=peak2_2, color='black', linestyle='--')
ax4.axvline(x=peak1_2, color='gray', linestyle='--')
ax4.text(100,900,s='peak ='+"{0:.2f}".format(peak2_2)+' Hz',fontsize='13')

plt.subplots_adjust(hspace=0.05, wspace=0.08)
plt.savefig('plots/fundamental_fft.pdf', format='pdf', dpi=1200)
plt.show()

