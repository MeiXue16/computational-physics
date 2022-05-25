# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:00:31 2020

@author: mei
"""
import numpy as np

def intrect(fhandle, a, b, h):
    
    xwerte= np.arange(a, b, h) # Mittelpunkte der Intervalle ermitteln
    xmittel= 0.5*h + xwerte # --> Vektor der Intervall-Mittelpunkte durch Verschiebung um h/2

    f = fhandle(xmittel) # Funktionswerte an den Intervallmittelpunkten

    cumsumf = np.cumsum(f) # Aufsummierung von Teilintervallen durch cumsum

    stamm_funk = h* cumsumf # Berechnung der Fläche

    xwerte = h+ xwerte # Berechnung der xwerte für Darstellung der Stammfunktion, jeweils am
      
    xwerte= np.insert(xwerte, 0, a)# rechten Rand des Teilintervalls
    stamm_funk= np.insert(stamm_funk, 0 ,0)
     

     
    area = stamm_funk[-1] # linke Intervallgrenze hinzufügen

    return area, xwerte, stamm_funk
    
    
