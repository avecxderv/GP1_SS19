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
        
        #Systematik
        vol_sys = (0.01*vol + 0.005*10)/np.sqrt(3)
        vol_oben = vol+vol_sys
        vol_unt = vol-vol_sys
        ex1_ob = analyse.exp_einhuellende(time, vol+vol_oben, np.full((vol.size),4.8e-3))
        ex1_un = analyse.exp_einhuellende(time, vol+vol_unt, np.full((vol.size),4.8e-3))
        ex2_ob = analyse.exp_einhuellende(time, -vol-vol_oben, np.full((vol.size),4.8e-3))
        ex2_un = analyse.exp_einhuellende(time, -vol-vol_unt, np.full((vol.size),4.8e-3))
        ex1_sys = 0.5*(np.abs(ex1_ob[2]-ex1[2])+np.abs(ex1_un[2]-ex1[2]))
        ex2_sys = 0.5*(np.abs(ex2_ob[2]-ex2[2])+np.abs(ex2_un[2]-ex2[2]))
        
        mu, inn, au = gewichtetes_mittel_in_aus(np.array([ex1[2],ex2[2]]),np.array([ex1[3],ex2[3]]))
        mu1, _, _ = gewichtetes_mittel_in_aus(np.array([ex1[2]+ex1_sys,ex2[2]+ex2_sys]),np.array([ex1[3],ex2[3]]))
        mu2, _, _ = gewichtetes_mittel_in_aus(np.array([ex1[2]-ex1_sys,ex2[2]-ex2_sys]),np.array([ex1[3],ex2[3]]))
        delta_e[i-1][j-1] = mu
        edelta_e[i-1][j-1] = max(inn,au)
        delta_sys_e[i-1][j-1] = 0.5*(np.abs(mu-mu1)+np.abs(mu-mu2))
        
        #Plot
        fig, ax = plt.subplots()
        ax.plot(time*1e+6,vol)
        ax.plot(time*1e+6,ex1[0]*np.exp(-ex1[2]*time))
        ax.plot(time*1e+6,-ex2[0]*np.exp(-ex2[2]*time))
        ax.set_xlabel('$t$ / s')
        ax.set_ylabel('$U_C$ / V')
        ax.set_xlim(0,dic5[i])
        fig.text(0.75,0.90,s='Dämpfung, oberer Fit: (' + "{0:.1f}".format(ex1[2]) + r'$\pm$' + "{0:.1f}".format(ex1[3]) + ')Hz', 
                 fontsize = '14', color='orange',ha='right',transform=ax.transAxes)
        fig.text(0.75,0.10,s='Dämpfung, unterer Fit: (' + "{0:.1f}".format(ex2[2]) + r'$\pm$' + "{0:.1f}".format(ex2[3]) + ')Hz', 
                 fontsize = '14', color='green',ha='right',transform=ax.transAxes)
        plt.rcParams["figure.figsize"] = (12,6)
        plt.rcParams['axes.titlesize'] = 'large'
        plt.rcParams['axes.labelsize'] = 'large'
        plt.tight_layout()
        ax.grid()
        plt.savefig('plots/einhuellend/exp_einhuellend'+str(i)+"_"+str(j)+'.pdf', format='pdf', dpi=1200)
        plt.close(fig)
        
dele = np.full((5,3),0.1)
for i in range(0,5,1):
    mu, inn, aus = gewichtetes_mittel_in_aus(delta_e[i],edelta_e[i])
    mu1, _, _ = gewichtetes_mittel_in_aus(delta_e[i]+delta_sys_e[i], edelta_e[i])
    mu2, _, _ = gewichtetes_mittel_in_aus(delta_e[i]-delta_sys_e[i], edelta_e[i])
    dele[i][0] = mu
    dele[i][1] = max(inn,aus)
    dele[i][2] = 0.5*(np.abs(mu-mu1)+np.abs(mu-mu2))
delta = np.array([dele[0][0],dele[1][0],dele[2][0],dele[3][0],dele[4][0]])
edelta = np.array([dele[0][1],dele[1][1],dele[2][1],dele[3][1],dele[4][1]])
edelta_sys = np.array([dele[0][2],dele[1][2],dele[2][2],dele[3][2],dele[4][2]])
R = np.array([1.008,5.101,9.99,19.82,46.67])
eR = np.array([0.001,0.001,0.002,0.01,0.01])


reg = analyse.lineare_regression_xy(R,delta,eR,edelta)

f, (ax1 , ax2) = plt.subplots(2,1,sharex = 'col')
ax1.plot(R,(reg[0]*R+reg[2]), linestyle="--", color = 'black')
ax1.errorbar(R,delta, yerr = edelta, xerr = eR, color='red', fmt='.', marker ='o')
ax2.axhline(y=0., color='black', linestyle='--')
ax2.errorbar(R, (delta-(reg[0]*R+reg[2])), yerr=np.sqrt(edelta**2+eR**2), color='red', fmt='.', marker='o', markeredgecolor='red')
plt.tight_layout()
f.subplots_adjust(hspace=0.0)
#plt.close(f)