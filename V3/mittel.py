#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def gewichtetes_mittel_in_aus(y, ey):
    w = 1/ey**2
    s = sum(w*y)
    wsum = sum(w)
    xm = s/wsum
    sx_in = np.sqrt(1./wsum)
    # Quadratische Abweichung vom Mittelwert
    ab_q = (y-xm)**2
    s_ab = sum(w*ab_q) # summiert
    sx_au = sx_in*np.sqrt(1./(len(y)-1)*s_ab)
    
    return (xm, sx_in, sx_au)