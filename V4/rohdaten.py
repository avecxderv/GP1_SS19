# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:39:02 2019

@author: Marius
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

data_s = cassy.CassyDaten('daten/schwingung_10Ohm_1.lab')
data_k = cassy.CassyDaten('daten/schwingung_1000Ohm_1.lab')
data_a = cassy.CassyDaten('daten/aperiodisch_3_186.lab')

time = data_s.messung(1).datenreihe('t').werte
# Zeit in ms
time = time*1000
volt_s = data_s.messung(1).datenreihe('U_B1').werte
volt_k = data_k.messung(1).datenreihe('U_B1').werte
volt_a = data_a.messung(1).datenreihe('U_B1').werte

plt.figure(figsize=(12,6))

plt.plot(time, volt_s, color='blue', label='Schwingung')
plt.plot(time, volt_k, color='green', label='Kriechfall')
plt.plot(time, volt_a, color='red', label='Aperiodischer Grenzfall')
plt.xlim(0,5)
plt.grid()
plt.xlabel('$t$ / ms')
plt.ylabel('$U_C$ / V')
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams['axes.titlesize'] = 'large'
plt.rcParams['axes.labelsize'] = 'large'
plt.legend()

plt.savefig('plots/rohdaten_ska.pdf', format='pdf', dpi=1200)

plt.show()