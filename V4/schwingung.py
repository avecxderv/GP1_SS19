#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:11:09 2019

@author: simon
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

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

reg1 = np.array([])
reg2 = np.array([])

#Frequenzen und Dämpfungen bestimmen
for i in range(1,6,1):
    n = np.arange(1,1+dic1[i].size,1)
    data = cassy.CassyDaten(dic2[i])
    time = data.messung(1).datenreihe('t').werte
    vol = data.messung(1).datenreihe('U_B1').werte
    x = time[dic1[i]]
    ex = np.full((dic1[i].size,),1e-05/np.sqrt(12))
    y = np.log(np.abs(vol[dic1[i]])-dic3[i])
    temp = 4.8e-03/np.sqrt(12)+0.01*np.abs(vol[dic1[i]])
    ey = temp*1/(np.abs(vol[dic1[i]])-dic3[i])
    res1 = analyse.lineare_regression(n,x,ex)
    res2 = analyse.lineare_regression_xy(x,y,ex,ey)
    reg1 = np.concatenate((reg1,res1))
    reg2 = np.concatenate((reg2,res2))
    
    #Plot
    f, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, sharex='col', gridspec_kw={'height_ratios': [5, 2]})
    #1. Regression Vanilla Plot [Zeiten in Mikrosekunden]
    ax1.plot(n,(res1[0]*n+res1[2])*1e+6, linestyle="--", color = 'black')
    ax1.errorbar(n,x*1e+6, yerr = 1e+6*ex, color='red', fmt='.', marker ='o')
    ax1.set_ylabel('$t$ / $\mu s$')
    ax1.grid()
    ax1.set_title('Regression zur Bestimmung der Periodendauer')
    #2. Regression Vanilla Plot
    ax2.plot(1e+6*x,res2[0]*x+res2[2], linestyle="--", color = 'black')
    ax2.errorbar(1e+6*x,y, yerr = ey, xerr = 1e+6*ex, color='red', fmt='.', marker = 'o')
    ax2.grid()
    ax2.set_ylabel('$\log | U | $')
    ax2.set_title('Regression zur Bestimmung der Dämpfung')
    #1. Regression Residuenplot
    ax3.axhline(y=0., color='black', linestyle='--')
    ax3.errorbar(n, 1e+6*(x-(res1[0]*n+res1[2])), yerr=ex*1e+6, color='red', fmt='.', marker='o', markeredgecolor='red')
    ax3.set_xlabel('Anzahl an Extrema')
    ax3.set_ylabel('($t - (T\, n + t_{off})$) / $\mu s$')
    #2. Regression Residuenplot
    ax4.axhline(y=0., color='black', linestyle='--')
    ax4.errorbar(1e+6*x,y-(res2[0]*x+res2[2]), yerr=np.sqrt(ex**2+ey**2), color='red', fmt='.', marker='o', markeredgecolor='red')
    ax4.set_xlabel('$t$ / $\mu s$')
    ax4.set_ylabel('$(\log |U| - (\delta t + \log U_0)$')
    #Plotparameter
    plt.rcParams["figure.figsize"] = (12,6)
    plt.rcParams['axes.titlesize'] = 'large'
    plt.rcParams['axes.labelsize'] = 'large'
    plt.tight_layout()
    f.subplots_adjust(hspace=0.0)
    plt.savefig('plots/reg_schwingung'+str(i)+'.pdf', format='pdf', dpi=1200)
    plt.close(f)    

#relevante Größen aus Regressionergebnissen ablesen
cond1 = np.arange(0,30,1)
cond2 = (np.mod(cond1,6) == 0)
T = reg1[cond2]
delta = -reg2[cond2]
cond1 = cond1+1
cond2 = (np.mod(cond1,6) == 0)
eT = reg1[cond2]
edelta = reg2[cond2]
R = np.array([1,5.1,10,20,47])

'''
#Omega korrigieren?
w = 2*np.pi/T
w = np.sqrt(w**2-delta**2)
'''

reg = analyse.lineare_regression(R,delta,edelta)