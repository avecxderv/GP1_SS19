#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:17:43 2019

@author: simon
"""


from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt
from mittel import gewichtetes_mittel_in_aus

#Maxima für 1 Ohm (als Indizes)
#max1 = np.array([27,57,86,115,145,174,204,233,263,292,322,351,381,410,439,469,498,528,557,587,617])
max1 = np.array([27,57,86,115,145,174,204,233,263,292,322,351,381,410,439,469,498,528,557,587,617])
offset1 = -0.025
#Maxima für 5.1 Ohm
#max2 = np.array([27,57,86,116,145,175,204,234,263,293,322,352,381,411,440,469,499,528,558])
max2 = np.array([27,57,86,116,145,175,204,234,263,293,322,352,381,411,440,469,499,528,558])
offset2 = 0.015
#Maxima und Minima für 10 Ohm
max3 = np.array([27,56,86,115,145,175,204,234,263,293,322,352,380,410,440])
offset3 = 0.01
#Maxima und Minima für 20 Ohm
max4 = np.array([28,57,86,116,146,176,205,235,264])
offset4 = 0.0175
#Maxima und Minima für 47 Ohm
max5 = np.array([28,59,89,120,151])
offset5 = -0.03
#Maxima und Minima für 100 Ohm
max6 = np.array([33,67])
offset6 = 0.0175

dic1 = {1:max1,2:max2,3:max3,4:max4,5:max5,6:max6}
dic2 = {1:'daten/schwingung_1Ohm_1.lab',2:'daten/schwingung_5.1Ohm_1.lab',3:'daten/schwingung_10Ohm_1.lab',
        4:'daten/schwingung_20Ohm_1.lab',5:'daten/schwingung_47Ohm_1.lab',6:'daten/schwingung_100Ohm_1.lab'}
dic3 = {1:offset1,2:offset2,3:offset3,4:offset4,5:offset5,6:offset6}
dic4 = {1:'daten/schwingung_1Ohm_',2:'daten/schwingung_5.1Ohm_',3:'daten/schwingung_10Ohm_',
        4:'daten/schwingung_20Ohm_',5:'daten/schwingung_47Ohm_',6:'daten/schwingung_100Ohm_'}
dic5 = {1: 15000,2:10000,3:7000,4:5000,5:2500}


#Exp-Einhüllende
delta_e = np.full((5,3),0.5)
edelta_e = np.full((5,3),0.5)
delta_sys_e = np.full((5,3),0.5)
for i in range(1,6,1):
    for j in range(1,4,1):
        data = cassy.CassyDaten(dic4[i]+str(j)+'.lab')
        time = data.messung(1).datenreihe('t').werte
        vol = data.messung(1).datenreihe('U_B1').werte #- dic3[i]
        ex1 = analyse.exp_einhuellende(time, vol, np.full((vol.size),4.8e-3))
        ex2 = analyse.exp_einhuellende(time,-vol,np.full((vol.size),4.8e-3))
        
        
        mu, inn, au = gewichtetes_mittel_in_aus(np.array([ex1[2],ex2[2]]),np.array([ex1[3],ex2[3]]))
        delta_e[i-1][j-1] = ex1[2] #mu
        edelta_e[i-1][j-1] = ex1[3]#max(inn,au)
        
        #Plot
        fig, ax = plt.subplots()
        ax.plot(time*1e+6,vol)
        ax.plot(time*1e+6,ex1[0]*np.exp(-ex1[2]*time))
        #ax.plot(time*1e+6,-ex2[0]*np.exp(-ex2[2]*time))
        ax.set_xlabel('$t$ / s')
        ax.set_ylabel('$U_C$ / V')
        ax.set_xlim(0,dic5[i])
        fig.text(0.75,0.91,s='Dämpfung: (' + "{0:.2f}".format(ex1[2]) + r'$\pm$' + "{0:.2f}".format(ex1[3]) + ')Hz', 
                 fontsize = '16', color='orange',ha='right',transform=ax.transAxes)
        #fig.text(0.75,0.10,s='Dämpfung, unterer Fit: (' + "{0:.1f}".format(ex2[2]) + r'$\pm$' + "{0:.1f}".format(ex2[3]) + ')Hz', 
        #         fontsize = '14', color='green',ha='right',transform=ax.transAxes)
        plt.rcParams["figure.figsize"] = (12,6)
        plt.rcParams['axes.titlesize'] = 'large'
        plt.rcParams['axes.labelsize'] = 'large'
        plt.tight_layout()
        ax.grid()
        #plt.savefig('plots/einhuellend/exp_einhuellend'+str(i)+"_"+str(j)+'.pdf', format='pdf', dpi=1200)
        plt.close(fig)
        
dele = np.full((5,2),0.1)
for i in range(0,5,1):
    mu, inn, aus = gewichtetes_mittel_in_aus(delta_e[i],edelta_e[i])
    dele[i][0] = mu
    dele[i][1] = max(inn,aus)
delta1 = np.array([dele[0][0],dele[1][0],dele[2][0],dele[3][0],dele[4][0]])
edelta1 = np.array([dele[0][1],dele[1][1],dele[2][1],dele[3][1],dele[4][1]])
R = np.array([1.008,5.101,9.99,19.82,46.67])
eR = np.array([0.001,0.001,0.002,0.01,0.01])

#Werte aus schwingung.py importieren
delta2 = np.array([ 341.01810569, 565.81381857, 860.23879874, 1421.9702776, 2820.46265235])
edelta2 = np.array([ 0.25891746,  0.56634525,  1.25160131,  3.57130468, 16.18687673])

reg1 = analyse.lineare_regression_xy(R,delta1,eR,edelta1)
reg2 = analyse.lineare_regression_xy(R,delta2,eR,edelta2)


f, ((ax1 , ax3),(ax2,ax4)) = plt.subplots(2,2,sharex = 'col',gridspec_kw={'height_ratios': [5, 2]})

ax1.set_title('Regression mit Dämpfungswerten aus Exp-Einhüllende')
ax1.plot(R,(reg1[0]*R+reg1[2]), linestyle="--", color = 'black')
ax1.errorbar(R,delta1, yerr = edelta1, xerr = eR, color='red', fmt='.', marker ='o')
ax1.text(0.03,0.92,s='Steigung: (' + "{0:.3f}".format(reg1[0]) + r'$\pm$' + "{0:.3f}".format(reg1[1]) + ')1/$\Omega$s', 
         fontsize = '13', color='blue',transform=ax1.transAxes)
ax1.text(0.03,0.85,s='y-Achsenabschnitt: (' + "{0:.3f}".format(reg1[2]) + r'$\pm$' + "{0:.3f}".format(reg1[3]) + ')Hz', 
         fontsize = '13', color='blue',transform=ax1.transAxes)
ax1.text(0.03,0.78,s='$\chi^2$/ndf: ' + "{0:.1f}".format(reg1[4]/(3)),
         fontsize = '13', color='blue',transform=ax1.transAxes)
ax1.set_ylabel('$\delta$ / Hz')
ax2.set_ylabel(r'$\delta - \frac{1}{2L} \left( R + R_0\right)$')
ax2.set_xlabel('R / $\Omega$')
ax2.axhline(y=0., color='black', linestyle='--')
ax2.errorbar(R, (delta1-(reg1[0]*R+reg1[2])), yerr=np.sqrt(edelta1**2+eR**2), color='red', fmt='.', marker='o', markeredgecolor='red')

ax3.set_title('Regression mit Dämpfungswerten aus Regression von $\log\,U_C$ über $t$')
ax3.plot(R,(reg2[0]*R+reg2[2]), linestyle="--", color = 'black')
ax3.errorbar(R,delta2, yerr = edelta2, xerr = eR, color='red', fmt='.', marker ='o')
ax3.text(0.03,0.92,s='Steigung: (' + "{0:.3f}".format(reg2[0]) + r'$\pm$' + "{0:.3f}".format(reg2[1]) + ')1/$\Omega$s', 
         fontsize = '13', color='blue',transform=ax3.transAxes)
ax3.text(0.03,0.85,s='y-Achsenabschnitt: (' + "{0:.3f}".format(reg2[2]) + r'$\pm$' + "{0:.3f}".format(reg2[3]) + ')Hz', 
         fontsize = '13', color='blue',transform=ax3.transAxes)
ax3.text(0.03,0.78,s='$\chi^2$/ndf: ' + "{0:.1f}".format(reg2[4]/(3)),
         fontsize = '13', color='blue',transform=ax3.transAxes)
ax3.set_ylabel('$\delta$ / Hz')
ax4.set_ylabel(r'$\delta - \frac{1}{2L} \left( R + R_0\right)$')
ax4.set_xlabel('R / $\Omega$')
ax4.axhline(y=0., color='black', linestyle='--')
ax4.errorbar(R, (delta2-(reg2[0]*R+reg2[2])), yerr=np.sqrt(edelta2**2+eR**2), color='red', fmt='.', marker='o', markeredgecolor='red')

#Plotparameter
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.tight_layout()
#plt.savefig('plots/reg_delR.pdf', format='pdf', dpi=1200)
f.subplots_adjust(hspace=0.0)
plt.close(f)