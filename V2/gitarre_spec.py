#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

# Daten laden
data1 = cassy.CassyDaten('daten/spektrum_1.2.lab')
time1 = data1.messung(1).datenreihe('t').werte
volt1 = data1.messung(1).datenreihe('U_A1').werte

data2 = cassy.CassyDaten('daten/spektrum_2.lab')
time2 = data2.messung(1).datenreihe('t').werte
volt2 = data2.messung(1).datenreihe('U_A1').werte

data3 = cassy.CassyDaten('daten/spektrum_3.1.lab')
time3 = data3.messung(1).datenreihe('t').werte
volt3 = data3.messung(1).datenreihe('U_A1').werte

# Fourier
fourier1 = analyse.fourier_fft(time1,volt1)
fourier2 = analyse.fourier_fft(time2,volt2)
fourier3 = analyse.fourier_fft(time3,volt3)

fre1 = fourier1[0]
amp1 = fourier1[1]
fre2 = fourier2[0]
amp2 = fourier2[1]
fre3 = fourier3[0]
amp3 = fourier3[1]

# Neagtive Frequenzen wegschneiden
fre1, amp1 = analyse.untermenge_daten(fre1, amp1, 0, 5000)
fre2, amp2 = analyse.untermenge_daten(fre2, amp2, 0, 5000)
fre3, amp3 = analyse.untermenge_daten(fre3, amp3, 0, 5000)

# Peaks
peak1 = analyse.peakfinder_schwerpunkt(fre1, amp1)
peak2 = analyse.peakfinder_schwerpunkt(fre2, amp2)
peak3 = analyse.peakfinder_schwerpunkt(fre3, amp3)

f = [0, 5000]

# Plot
fig, (ax1, ax2, ax3) = plt.subplots(3,1, sharex=True, figsize=(12,12))

ax2.set_ylabel('Amplitude')
ax3.set_xlabel('$f$ / Hz')


for i in range(75):
    if i%2 == 0:
        ax1.axvline(x=peak1*i, color='red', alpha=0.5, linestyle='dotted')
    else:
        ax1.axvline(x=peak1*i, color='grey', alpha=0.5, linestyle='dotted')
ax1.plot(fre1, amp1, color='orange')
ax1.set_ylim(1.1,3000)
ax1.set_yscale('log')
ax1.text(4700, 1000, '$d= 1/2$', size=16, ha="right", va="top",
         bbox=dict(boxstyle="square", ec='black', fc='white'))





for i in range(75):
    if i%5 == 0:
        ax2.axvline(x=peak2/2*i, color='red', alpha=0.5, linestyle='dotted')
    else:
        ax2.axvline(x=peak2/2*i, color='grey', alpha=0.5, linestyle='dotted')
ax2.plot(fre2, amp2, color='orange')
ax2.set_ylim(1.5,8000)
ax2.set_yscale('log')
ax2.text(4700, 2000, '$d= 1/5$', size=16, ha="right", va="top",
         bbox=dict(boxstyle="square", ec='black', fc='white'))



for i in range(75):
    if i%3 == 0:
        ax3.axvline(x=peak3/2*i, color='red', alpha=0.5, linestyle='dotted')
    else:
        ax3.axvline(x=peak3/2*i, color='grey', alpha=0.5, linestyle='dotted')
ax3.plot(fre3, amp3, color='orange')
ax3.set_xlim(f[0], f[1])
ax3.set_xticks(np.arange(f[0],f[1],500))
ax3.set_ylim(1.5,7000)
ax3.set_yscale('log')
ax3.text(4700, 2000, '$d= 1/3$', size=16, ha="right", va="top",
         bbox=dict(boxstyle="square", ec='black', fc='white'))

plt.tight_layout()
plt.subplots_adjust(hspace=0)
plt.savefig('plots/anschlagspektrum.pdf', format='pdf', dpi=1200)
plt.show()
