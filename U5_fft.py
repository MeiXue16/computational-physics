# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:45:37 2021

@author: mei
"""
import numpy as np


def my_fft(N, signal):
   
    if N ==1:
        return signal# Rekursionsende

    else:
        # Ab hier laufen wir im Rekursionsbaum nach unten.
        p= round(N/2)
        even = my_fft(p, signal[::2])
        odd =  my_fft(p, signal[1::2])
        spektrum =np.zeros((N,),dtype = 'complex_')
        for k in range (p):
            faktor = np.exp(-2j*(np.pi)*k/N)
            spektrum[k] =even[k] + odd[k] *faktor
            spektrum[k + p] =even[k] - odd[k] * faktor

    return spektrum

