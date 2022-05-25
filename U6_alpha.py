# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:36:08 2021

@author:Mei Xue
"""
import numpy as np
def alpha_osci(x0, v0, w, alpha, N, T):
    dt= T/N
    wx_v =np.zeros(shape=(2,N+1))
    wx_v[:,0] = np.array([w*x0, v0])
    
    m1 = np.array([[1  ,   -(1-alpha)*w*dt],
                   [(1-alpha)*w*dt   ,    1]])
    m1_inv =np.linalg.inv(m1)
    m2 = np.matrix([[1  , alpha*w*dt],
                    [-alpha*w*dt , 1] ])
                 
    #Alpha-Verfahren
    for i in range (1, N+1):
        wx_v[:,i]= np.dot(np.dot(m1_inv, m2) , wx_v[:,i-1] )
    
    x= wx_v[0,:]/w
    v= wx_v[1,:]
    t= dt* np.arange(0, N+1, 1)
    return x,v,t
    """Berechnet die Bewegung eines harmonischen Oszillators mit dem
    alpha-Verfahren.

    Beispiel
    --------
     x0 = 1
     v0 = 0
     w  = 1
     alpha = 0.5
     N = 1000
     T = 20
     x, v, t = alpha_osci(x0, v0, w, alpha, N, T)

    Eingabe
    -------
     x0 : float
         Standort
     v0 : float
         Eingangssignal
     w : float
         Eigenfrequenz
     alpha : float
         Parameter des alpha-Verfahrens
     N : Anzahl der Zeitschritte
     T : Maximalzeit

    Ausgabe
    -------
     x : float (1d-array)
         Ergebnisvektor des Ortes der Länge N+1
     v : float (1d-array)
         Ergebnisvektor der Geschwindigkeit der Länge N+1
     t : float (1d-array)
         Stützstellen der Zeit der Länge N+1
    """
