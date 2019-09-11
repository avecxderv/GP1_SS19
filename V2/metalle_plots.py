#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:35:44 2019

@author: simon
"""

'''
#Plot Rohdaten
data = cassy.CassyDaten('daten/Nr5_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
f, (ax1,ax2) = plt.subplots(2,1)
ax1.plot(timeVal,voltage)
ax1.set_ylabel("Schalldruck")
ax2.set_ylabel("Schalldruck")
ax2.plot(timeVal[0:250], voltage[0:250])
ax2.set_xlabel("$t$ / $s$")
ax1.set_xlim(0,1.6)
ax2.set_xlim(0,0.025)
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.savefig('plots/rohdaten.pdf')
plt.show()
plt.close()
'''

'''
#Beispiel Sepektrum
data = cassy.CassyDaten('daten/Nr5_1.lab')
timeVal = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
fourier = analyse.fourier_fft(timeVal, voltage)
freq = fourier[0]
amp = fourier[1]
plt.plot(freq[0:8000],amp[0:8000], color='orange')
plt.xlim(0,5000)
plt.xlabel('$f$ / Hz')
plt.ylabel('Amplitude')
plt.grid()
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.savefig('plots/spektrum1.pdf')
'''



'''
data1 = cassy.CassyDaten('daten/Nr11_1.lab')
data2 = cassy.CassyDaten('daten/Nr11_2.lab')
data3 = cassy.CassyDaten('daten/Nr11_3.lab')
data4 = cassy.CassyDaten('daten/Nr11_4.lab')
data5 = cassy.CassyDaten('daten/Nr11_5.lab')

timeVal = data2.messung(1).datenreihe('t').werte

voltage1 = data1.messung(1).datenreihe('U_A1').werte
voltage2 = data2.messung(1).datenreihe('U_A1').werte
voltage3 = data3.messung(1).datenreihe('U_A1').werte
voltage4 = data4.messung(1).datenreihe('U_A1').werte
voltage5 = data5.messung(1).datenreihe('U_A1').werte

fourier1 = analyse.fourier_fft(timeVal, voltage1)
fourier2 = analyse.fourier_fft(timeVal, voltage2)
fourier3 = analyse.fourier_fft(timeVal, voltage3)
fourier4 = analyse.fourier_fft(timeVal, voltage4)
fourier5 = analyse.fourier_fft(timeVal, voltage5)

freq1 = fourier1[0]
amp1 = fourier1[1]
freq2 = fourier2[0]
amp2 = fourier2[1]
freq3 = fourier3[0]
amp3 = fourier3[1]
freq4 = fourier4[0]
amp4 = fourier4[1]
freq5 = fourier5[0]
amp5 = fourier5[1]

f, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1)
ax5.set_xlabel('$f$ / Hz')
ax3.set_ylabel('Amplitude')

ax1.scatter(freq1,amp1,color='orange')
ax2.scatter(freq2,amp2,color='orange')
ax3.scatter(freq3,amp3,color='orange')
ax4.scatter(freq4,amp4,color='orange')
ax5.scatter(freq5,amp5,color='orange')

maximumIndex1 = amp1.argmax();
maximumIndex2 = amp2.argmax();
maximumIndex3 = amp3.argmax();
maximumIndex4 = amp4.argmax();
maximumIndex5 = amp5.argmax();

ax1.set_xlim(freq1[max(0, maximumIndex1-10)], freq1[min(maximumIndex1+10, len(freq1))])
ax2.set_xlim(freq2[max(0, maximumIndex2-10)], freq2[min(maximumIndex2+10, len(freq2))])
ax3.set_xlim(freq3[max(0, maximumIndex3-10)], freq3[min(maximumIndex3+10, len(freq3))])
ax4.set_xlim(freq4[max(0, maximumIndex4-10)], freq4[min(maximumIndex4+10, len(freq4))])
ax5.set_xlim(freq5[max(0, maximumIndex5-10)], freq5[min(maximumIndex5+10, len(freq5))])

peak1 = analyse.peakfinder_schwerpunkt(freq1,amp1)
peak2 = analyse.peakfinder_schwerpunkt(freq2,amp2)
peak3 = analyse.peakfinder_schwerpunkt(freq3,amp3)
peak4 = analyse.peakfinder_schwerpunkt(freq4,amp4)
peak5 = analyse.peakfinder_schwerpunkt(freq5[maximumIndex5-10:maximumIndex5+10],amp5[maximumIndex5-10:maximumIndex5+10])

ax1.axvline(peak1, linestyle= "--",color='black')
ax1.axvline(peak1-0.5, linestyle='dotted', color='grey')
ax1.axvline(peak1+0.5, linestyle='dotted', color='grey')
ax1.text(freq1[maximumIndex1-9],0.5*amp1[maximumIndex1],s='peak ='+"{0:.2f}".format(peak1)+' Hz',fontsize='13')

ax2.axvline(peak2, linestyle= "--",color='black')
ax2.axvline(peak2-0.5, linestyle='dotted', color='grey')
ax2.axvline(peak2+0.5, linestyle='dotted', color='grey')
ax2.text(freq2[maximumIndex2-9],0.5*amp2[maximumIndex2],s='peak ='+"{0:.2f}".format(peak2)+' Hz',fontsize='13')

ax3.axvline(peak3, linestyle= "--",color='black')
ax3.axvline(peak3-0.5, linestyle='dotted', color='grey')
ax3.axvline(peak3+0.5, linestyle='dotted', color='grey')
ax3.text(freq3[maximumIndex3-9],0.5*amp3[maximumIndex3],s='peak ='+"{0:.2f}".format(peak3)+' Hz',fontsize='13')

ax4.axvline(peak4, linestyle= "--",color='black')
ax4.axvline(peak4-0.5, linestyle='dotted', color='grey')
ax4.axvline(peak4+0.5, linestyle='dotted', color='grey')
ax4.text(freq4[maximumIndex4-9],0.5*amp4[maximumIndex4],s='peak ='+"{0:.2f}".format(peak4)+' Hz',fontsize='13')

ax5.axvline(peak5, linestyle= "--",color='black')
ax5.axvline(peak5-0.5, linestyle='dotted', color='grey')
ax5.axvline(peak5+0.5, linestyle='dotted', color='grey')
ax5.text(freq5[maximumIndex5-9],0.5*amp5[maximumIndex5],s='peak ='+"{0:.2f}".format(peak5)+' Hz',fontsize='13')

ax1.set_title('Stab 11, Stahl',fontweight='bold')
f.set_size_inches(8.27, 11.69)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.savefig('plots/anhang4.pdf')
'''
