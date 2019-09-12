# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

# Daten laden
data = cassy.CassyDaten('daten/schwebung_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte


'''
t = [0, 8]
plt.plot(timeVal, voltage)

plt.xlim(t[0], t[1])
#plt.ylim(-0.3,0.3)

plt.xticks(np.arange(t[0], t[1], 0.02))
#plt.xticks(np.arange(t[0],t[1], 2*0.0069))

plt.grid()
plt.tight_layout()
plt.show()
'''

'''
# Rohdaten visualisieren

data = cassy.CassyDaten('daten/schwebung_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte

plt.figure(figsize=(12,4))
plt.xlim(0,3.2)
plt.plot(timeVal, voltage)
plt.ylabel('$U$ / V')
plt.xlabel('$t$ / s')
plt.tight_layout()

plt.savefig('plots/rohdaten_schwebung.pdf', format='pdf', dpi=1200)
plt.show()
'''

'''
# Beispiel zur Bestimmung der Maxima

data1 = cassy.CassyDaten('daten/schwebung_1.lab')
time1 = data1.messung(1).datenreihe('t').werte
volt1 = data1.messung(1).datenreihe('U_A1').werte

data2 = cassy.CassyDaten('daten/schwebung_4.2.lab')
time2 = data2.messung(1).datenreihe('t').werte
volt2 = data2.messung(1).datenreihe('U_A1').werte

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))

t1 = [1.3996,1.4074]
ax1.plot(time1, volt1)
ax1.set_xlim(t1[0], t1[1])
ax1.set_ylim(-1.5,1.5)
ax1.set_xticks(np.arange(t1[0], t1[1], 0.001))
ax1.set_xticks(np.arange(t1[0], t1[1], 0.0002), minor=True)

ax1.axvline(x=1.4036, color='red', label='$t_m$')
ax1.axvline(x=1.4038, color='red', linestyle='--', label='$t_m \pm \sigma_t$')
ax1.axvline(x=1.4034, color='red', linestyle='--')
ax1.legend()

ax1.grid(which='both')



t2 = [1.2,1.35]
ax2.plot(time2, volt2)
ax2.set_xlim(t2[0], t2[1])
ax2.set_ylim(-0.8,0.8)
ax2.set_xticks(np.arange(t2[0]+0.01, t2[1], 0.02))
ax2.set_xticks(np.arange(t2[0], t2[1], 0.005), minor=True)

ax2.grid()
ax2.axvline(x=1.27, color='red', label='$t_m$')
ax2.axvline(x=1.265, color='red', linestyle='--', label='$t_m \pm \sigma_t$')
ax2.axvline(x=1.275, color='red', linestyle='--')
ax2.set_xlabel('$t$ / s')
ax2.set_ylabel('$U$ / V')
ax2.legend()

plt.tight_layout()
plt.savefig('plots/bspMaxima.pdf', format='pdf', dpi=1200)
plt.show()
'''


# Messwerte für Maxima der resultierenden Schwingung in s
tR1 = np.array([0.0308, 0.1614, 0.4378, 0.5754, 0.7136, 0.8512, 0.9892, 1.1276, 1.4036, 1.6518, 1.7902, 1.9278, 2.0660, 2.3418, 2.6178, 2.7562, 2.8936, 3.0322])
nR1 = np.array([1, 20, 60, 80, 100, 120, 140, 160, 200, 236, 256, 276, 296, 336, 376, 396, 416, 436])

tR2 = np.array([0.1548, 0.2848, 0.4426, 0.5802, 0.8548, 0.9920, 1.1292, 1.2662, 1.5410, 1.6782, 1.8156, 2.0900, 2.2274, 2.3648, 2.5022, 2.7762, 2.9136, 3.0510])
nR2 = np.array([-2, 17, 40, 60, 100, 120, 140, 160, 200, 220, 240, 280, 300, 320, 340, 380, 400, 420])

tR3 = np.array([0.007, 0.137, 0.2395, 0.3765, 0.5135, 0.7865, 0.9235, 1.0605, 1.1975, 1.3345, 1.471, 1.608, 1.745, 1.882, 2.0185, 2.291, 2.4285, 2.5655, 2.7025, 2.8395, 2.9765, 3.1135])
nR3 = np.array([6, 25, 40, 60, 80, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 360, 380, 400, 420, 440, 460])

tR4 = np.array([0.08, 0.206, 0.3446, 0.4844, 0.6234, 0.7636, 0.9026, 1.3214, 1.4604, 1.5996, 1.7388, 2.0188, 2.1576, 2.2968, 2.4366, 2.5966, 2.7162, 2.8552, 2.9942, 3.1338])
nR4 = np.array([2, 20, 40, 60, 80, 100, 120, 180, 200, 220, 240, 280, 300, 320, 340, 363, 380, 400, 420, 440])


# Messwerte für Maxima/Minima der Schwebungsschwingung in s
tS1 = np.array([0.155, 0.465, 0.78, 1.085, 1.41, 1.72, 2.035, 2.345, 2.655, 2.975])
mS1 = np.arange(1,11,1)

tS2 = np.array([0.38, 1.02, 1.66, 2.33, 2.99])
mS2 = np.arange(1,6,1)

tS4 = np.array([0.075, 0.24, 0.42, 0.595, 0.76, 0.93, 1.10, 1.27, 1.445, 1.62, 1.795, 1.965, 2.135, 2.305, 2.47, 2.64, 2.81, 2.975])
mS4 = np.arange(1,19,1)


# Lineare Regressionen resultierende Schwingung
errtR1 = np.full((len(tR1),),0.0002)
errtR3 = np.full((len(tR3),),0.0005)
errtR4 = np.full((len(tR4),),0.0004)

regR1 = analyse.lineare_regression(nR1, tR1, errtR1)

regR2 = analyse.lineare_regression(nR2, tR2, errtR1)

regR3 = analyse.lineare_regression(nR3, tR3, errtR3)

regR4 = analyse.lineare_regression(nR4, tR4,errtR4)


# Lineare Regressionen Schwebungsschwingung
errtS1 = np.full((len(tS1),),0.005)
errtS2 = np.full((len(tS2),),0.01)
errtS4 = np.full((len(tS4),),0.005)

regS1 = analyse.lineare_regression(mS1, tS1, errtS1)

regS2 = analyse.lineare_regression(mS2, tS2, errtS2)

regS4 = analyse.lineare_regression(mS4, tS4, errtS4)




'''
# Residuenplots Schwebungsschwingung

plt.figure(figsize=(12,6))
ax1 = plt.subplot(211)
ax1.axhline(y=0, color='black', linestyle='--')
ax1.errorbar(mS4, tS4-(regS4[0]*mS4+regS4[2]), yerr=errtS4, color='red', fmt='.', marker='o', markeredgecolor='red')
ax1.set_xlim(0,19)
ax1.set_xticks(np.arange(1,19,1))
ax1.set_title('Schwebung 4')
ax1.set_ylabel('$t-(T/2m+c)$ / s')
ax1.set_xlabel('m')

ax2 = plt.subplot(223)
ax2.axhline(y=0, color='black', linestyle='--')
ax2.errorbar(mS1, tS1-(regS1[0]*mS1+regS1[2]), yerr=errtS1, color='red', fmt='.', marker='o', markeredgecolor='red')
ax2.set_xlim(0,11)
ax2.set_xticks(np.arange(1,11,1))
ax2.set_title('Schwebung 1')
ax2.set_ylabel('$t-(T/2m+c)$ / s')
ax2.set_xlabel('m')

ax3 = plt.subplot(224)
ax3.axhline(y=0, color='black', linestyle='--')
ax3.errorbar(mS2, tS2-(regS2[0]*mS2+regS2[2]), yerr=errtS2, color='red', fmt='.', marker='o', markeredgecolor='red')
ax3.set_xlim(0,6)
ax3.set_xticks(np.arange(1,6,1))
ax3.set_title('Schwebung 2')
ax3.set_ylabel('$t-(T/2m+c)$ / s')
ax3.set_xlabel('m')


plt.subplots_adjust(hspace=0.5)
plt.tight_layout()

plt.savefig('plots/residuenSch.pdf', format='pdf', dpi=1200)
plt.show()
'''



'''
# Residuenplots resultierende Schwingung

fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2,2, figsize=(12,6))


ax1.axhline(y=0., color='black', linestyle='--')
ax1.errorbar(nR1, tR1-(regR1[0]*nR1+regR1[2]), yerr=errtR1, color='red', fmt='.', marker='o', markeredgecolor='red')
ax1.set_ylabel('$t-(Tn+b)$ / s')
ax1.set_xlabel('$n$')
ax1.set_title('Schwebung 1')

ax2.axhline(y=0., color='black', linestyle='--')
ax2.errorbar(nR3, tR3-(regR3[0]*nR3+regR3[2]), yerr=errtR3, color='red', fmt='.', marker='o', markeredgecolor='red')
ax2.set_ylabel('$t-(Tn+b)$ / s')
ax2.set_xlabel('$n$')
ax2.set_title('Schwebung 2')

ax3.axhline(y=0, color='black', linestyle='--')
ax3.errorbar(nR2, tR2-(regR2[0]*nR2+regR2[2]), yerr=errtR1, color='red', fmt='.', marker='o', markeredgecolor='red')
ax3.set_ylabel('$t-(Tn+b)$ / s')
ax3.set_xlabel('$n$')
ax3.set_title('Schwebung 3')

ax4.axhline(y=0, color='black', linestyle='--')
ax4.errorbar(nR4, tR4-(regR4[0]*nR4+regR4[2]), yerr=errtR4, color='red', fmt='.', marker='o', markeredgecolor='red')
ax4.set_ylabel('$t-(Tn+b)$ / s')
ax4.set_xlabel('$n$')
ax4.set_title('Schwebung 4')

plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'

plt.tight_layout()
#plt.show()
plt.savefig('plots/residuenRes.pdf', format='pdf', dpi=1200)
plt.close(fig)
'''


'''
# Beispiel Spektrum
data = cassy.CassyDaten('daten/schwebung_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte

fourier = analyse.fourier_fft(timeVal,voltage)
frequency = fourier[0]
amplitude = fourier[1]
plt.figure(figsize=(12,6))
plt.plot(frequency, amplitude, color='orange')
plt.xlim(0, 800)
plt.ylabel('Amplitude')
plt.xlabel('$f$ / Hz')

plt.grid()
plt.tight_layout()
plt.savefig('plots/schwebungsspektrum.pdf', format='pdf', dpi=1200)
plt.show()
'''



## FFT mit Peakfinder


# Schwebung 1
data1 = cassy.CassyDaten('daten/schwebung_1.lab')
time1 = data1.messung(1).datenreihe('t').werte
volt1 = data1.messung(1).datenreihe('U_A1').werte

fourier1 = analyse.fourier_fft(time1,volt1)
fre1 = fourier1[0]
amp1 = fourier1[1]

fre1_1, amp1_1 = analyse.untermenge_daten(fre1, amp1, 142, 145)
fre1_2, amp1_2 = analyse.untermenge_daten(fre1, amp1, 145, 148)

fS1_1 = analyse.peakfinder_schwerpunkt(fre1_1, amp1_1)
fS1_2 = analyse.peakfinder_schwerpunkt(fre1_2, amp1_2)


# Schwebung 2
data2 = cassy.CassyDaten('daten/schwebung_2.2.lab')
time2 = data2.messung(1).datenreihe('t').werte
volt2 = data2.messung(1).datenreihe('U_A1').werte

fourier2 = analyse.fourier_fft(time2,volt2)
fre2 = fourier2[0]
amp2 = fourier2[1]

fre2_1, amp2_1 = analyse.untermenge_daten(fre2, amp2, 144, 145.5)
fre2_2, amp2_2 = analyse.untermenge_daten(fre2, amp2, 145.5, 147.5)

fS2_1 = analyse.peakfinder_schwerpunkt(fre2_1, amp2_1)
fS2_2 = analyse.peakfinder_schwerpunkt(fre2_2, amp2_2)


# Schwebung 3
data3 = cassy.CassyDaten('daten/schwebung_3.1.lab')
time3 = data3.messung(1).datenreihe('t').werte
volt3 = data3.messung(1).datenreihe('U_A1').werte

fourier3 = analyse.fourier_fft(time3,volt3)
fre3 = fourier3[0]
amp3 = fourier3[1]

fre3_1, amp3_1 = analyse.untermenge_daten(fre3, amp3, 144, 146.2)
fre3_2, amp3_2 = analyse.untermenge_daten(fre3, amp3, 146.1, 148)

fS3_1 = analyse.peakfinder_schwerpunkt(fre3_1, amp3_1)
fS3_2 = analyse.peakfinder_schwerpunkt(fre3_2, amp3_2)

# Schwebung 4
data4 = cassy.CassyDaten('daten/schwebung_4.1.lab')
time4 = data4.messung(1).datenreihe('t').werte
volt4 = data4.messung(1).datenreihe('U_A1').werte

fourier4 = analyse.fourier_fft(time4,volt4)
fre4 = fourier4[0]
amp4 = fourier4[1]

fre4_1, amp4_1 = analyse.untermenge_daten(fre4, amp4, 138, 143.5)
fre4_2, amp4_2 = analyse.untermenge_daten(fre4, amp4, 143.5, 149)

fS4_1 = analyse.peakfinder_schwerpunkt(fre4_1, amp4_1)
fS4_2 = analyse.peakfinder_schwerpunkt(fre4_2, amp4_2)

# Unsicherheiten
sigf1 = 0.31
sigf2 = 0.12
sigf3 = 0.12
sigf4 = 0.12


'''
# Plot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(12,6))


ax1.scatter(fre1, amp1, color='orange')

ax1.set_xlim(140, 150)
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('$f$ / Hz')
ax1.set_xticks(np.arange(140,151,1))

ax1.axvline(x=fS1_1, color='black', linestyle='--')
ax1.axvline(x=fS1_1+sigf1, color='grey', linestyle='dotted')
ax1.axvline(x=fS1_1-sigf1, color='grey', linestyle='dotted')

ax1.axvline(x=fS1_2, color='black', linestyle='--')
ax1.axvline(x=fS1_2+sigf1, color='grey', linestyle='dotted')
ax1.axvline(x=fS1_2-sigf1, color='grey', linestyle='dotted')

ax1.grid()
ax1.set_title('Schwebung 1')


ax2.scatter(fre2, amp2, color='orange')

ax2.set_xlim(142, 150)
ax2.set_ylabel('Amplitude')
ax2.set_xlabel('$f$ / Hz')
ax2.set_xticks(np.arange(142,151,1))

ax2.axvline(x=fS2_1, color='black', linestyle='--')
ax2.axvline(x=fS2_1+sigf2, color='grey', linestyle='dotted')
ax2.axvline(x=fS2_1-sigf2, color='grey', linestyle='dotted')

ax2.axvline(x=fS2_2, color='black', linestyle='--')
ax2.axvline(x=fS2_2+sigf2, color='grey', linestyle='dotted')
ax2.axvline(x=fS2_2-sigf2, color='grey', linestyle='dotted')

ax2.grid()
ax2.set_title('Schwebung 2')


ax3.scatter(fre3, amp3, color='orange')

ax3.set_xlim(143, 149)
ax3.set_ylabel('Amplitude')
ax3.set_xlabel('$f$ / Hz')
ax3.set_xticks(np.arange(143,150,1))

ax3.axvline(x=fS3_1, color='black', linestyle='--')
ax3.axvline(x=fS3_1+sigf3, color='grey', linestyle='dotted')
ax3.axvline(x=fS3_1-sigf3, color='grey', linestyle='dotted')

ax3.axvline(x=fS3_2, color='black', linestyle='--')
ax3.axvline(x=fS3_2+sigf3, color='grey', linestyle='dotted')
ax3.axvline(x=fS3_2-sigf3, color='grey', linestyle='dotted')

ax3.grid()
ax3.set_title('Schwebung 3')


ax4.scatter(fre4, amp4, color='orange')

ax4.set_xlim(138, 149)
ax4.set_ylabel('Amplitude')
ax4.set_xlabel('$f$ / Hz')
ax4.set_xticks(np.arange(138,150,1))

ax4.axvline(x=fS4_1, color='black', linestyle='--')
ax4.axvline(x=fS4_1+sigf4, color='grey', linestyle='dotted')
ax4.axvline(x=fS4_1-sigf4, color='grey', linestyle='dotted')

ax4.axvline(x=fS4_2, color='black', linestyle='--')
ax4.axvline(x=fS4_2+sigf4, color='grey', linestyle='dotted')
ax4.axvline(x=fS4_2-sigf4, color='grey', linestyle='dotted')

ax4.grid()
ax4.set_title('Schwebung 4')

plt.tight_layout()
plt.savefig('plots/FFT_freq.pdf', format='pdf', dpi=1200)
plt.show()
'''
