#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:22:34 2019

@author: simon
"""

from praktikum import analyse
from praktikum import cassy
import numpy as np
import matplotlib.pyplot as plt

#Gemessene Groessen
#5 = Kupfer, 6 = Messing, 9 = Alu, 11 = Stahl

l5 = 129.9
l6 = 130
l9 = 129.9
l11 = 130.1
el = 0.069

d5 = 11.991e-1
ed5 =  0.0801e-1
d6 = 11.978e-1
ed6 = 0.0042e-1
d9 = 11.944e-1
ed9 = 0.031e-1
d11 = 11.989e-1
ed11 = 0.0451e-1

m5 = 1295
m6 = 1237.2
m9 = 407.3
m11 = 1157.6

el = 0.69e-3
em = 0.1e-3/np.sqrt(12)

rho_cu = 4*m5/(np.pi*d5**2*l5)
erho_cu = rho_cu*np.sqrt( 0.1**2/(m5**2) + 0.0069**2/(l5**2) + 4*(ed5**2)/(d5**2))
rho_messing = 4*m6/(np.pi*d6**2*l6)
erho_messing = rho_messing*np.sqrt( 0.1**2/(m6**2) + 0.0069**2/(l6**2) + 4*ed6**2/(d6**2))
rho_al = 4*m9/(np.pi*d9**2*l9)
erho_al = rho_al*np.sqrt( 0.1**2/(m9**2) + 0.0069**2/(l9**2) + 4*(ed9**2)/(d9**2))
rho_stahl = 4*m11/(np.pi*d11**2*l11)
erho_stahl = rho_stahl*np.sqrt( 0.1**2/(m11**2) + 0.0069**2/(l11**2) + 4*ed11**2/(d11**2))

ef = np.full((5,),0.5)

f0_5 = [1458.77, 1458.8, 1458.82, 1458.83, 1458.83]
f_5 = analyse.gewichtetes_mittel(f0_5,ef)
v_5 = 2*l5*1e-2*f_5[0]

f0_6 = [1348.16, 1348.13, 1348.12, 1348.12, 1348.08]
f_6 = analyse.gewichtetes_mittel(f0_6,ef)
v_6 = 2*l6*1e-2*f_6[0]

f0_9 = [1966.17, 1966.29, 1966.34, 1966.35, 1966.52]
f_9 = analyse.gewichtetes_mittel(f0_9,ef)
v_9 = 2*l9*1e-2*f_9[0]

f0_11 = [1883.91, 1883.94, 1883.97, 1884, 1883.95]
f_11 = analyse.gewichtetes_mittel(f0_11,ef)
v_11 = 2*l11*1e-2*f_11[0]

ev5 = v_5*np.sqrt(f_5[1]**2/(f_5[0]**2)+el**2/(l5**2))
ev6 = v_6*np.sqrt(f_6[1]**2/(f_6[0]**2)+el**2/(l6**2))
ev9 = v_9*np.sqrt(f_9[1]**2/(f_9[0]**2)+el**2/(l9**2))
ev11 = v_11*np.sqrt(f_11[1]**2/(f_11[0]**2)+el**2/(l11**2))

E5 = 16*f_5[0]**2*l5*1e-5*m5*1/(np.pi*(d5*1e-2)**2)
E6 = 16*f_6[0]**2*l6*1e-1*m6*1/(np.pi*d6**2)
E9 = 16*f_9[0]**2*l9*1e-1*m9*1/(np.pi*d9**2)
E11 = 16*f_11[0]**2*l11*1e-1*m11*1/(np.pi*d11**2)

eE5 = E5*np.sqrt(4*f_5[1]**2/(f_5[0]**2) + el**2/(l5**2) + 0.1**2/(m5**2) + 4*ed5**2/(d5**2))
eE6 = E6*np.sqrt(4*f_6[1]**2/(f_6[0]**2) + el**2/(l6**2) + 0.1**2/(m6**2) + 4*ed6**2/(d6**2))
eE9 = E9*np.sqrt(4*f_9[1]**2/(f_9[0]**2) + el**2/(l9**2) + 0.1**2/(m9**2) + 4*ed9**2/(d9**2))
eE11 = E11*np.sqrt(4*f_11[1]**2/(f_11[0]**2) + el**2/(l11**2) + 0.1**2/(m11**2) + 4*ed11**2/(d11**2))