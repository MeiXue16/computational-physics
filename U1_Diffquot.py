# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 23:45:45 2020

@author: mei
"""
import numpy as np
def diffquot(fhandle, a, b, h ):
     xwerte= np.arange(a, b, h)# Bestimmung des Definitionsbereichs der Funktion
     xwerte= np.asarray(xwerte)

     y= fhandle(xwerte)# Evaluierung der Funktion 'fhandle'
     y2= fhandle(xwerte + h)
     
     ableitung= (y2-y)/h# Berechung der numerischen Ableitung mittels des rechtsseitigen
        # Differenzenquotienten

     return (xwerte[:-1], ableitung[:-1])
