# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:54:50 2021

@author: mei
"""
import numpy as np
import matplotlib.pyplot as plt
from lu_crout import myLU
from lu_crout import elimination
import time

#%% Initialisiere gemeinsame Parameter

A= np.matrix('1 1 0;\
              4 0 2;\
              0 2 1') # Matrix A des aufgestellten Grundstoff-Gleichungssystems
zutaten = np.matrix('6  2 4 6;\
                     12 6 6 8;\
                     6  1 6 7') # Inhomogenitätenvektoren für diverse Glühweinzutaten

#%% Beispiel 1: Glühweinproduktion

# Zerlege Matrix A
L,U = myLU(A)
# Berechne für jede Glühweinzutat die nötige Menge an Grundstoffen
xln = np.zeros((3,4))
x = np.zeros((3,4))
for i in range(4):
    xln[:,i] =elimination(L, U,  zutaten[:,i]) #x/n, z.B. x[:,0] ist vektor Glühweinzutat C6H12O6 die nötige Menge an Grundstoffen
    #print('xln[:,i]',xln[:,i])
    for n in range(1,1000):
        for j in range(3):
            x[j,i] = xln[j,i] * n
        if(x[0,i] % 1== 0 and x[1,i] % 1== 0 and x[2,i] % 1== 0):
            break
    print('n=',n,',Stoffmenge der Ausgangsstoffe für ',i+1,'-ten Zutaten des Glühweins:\n',x[:,i])    
    # Konsolenausgabe

#%% Beispiel 2: Laufzeit der LU-Zerlegung in Abhängigkeit von der Matrixgröße

# Variiere die Matrixgröße NxN
N = np.arange(3,100,1)
t = np.zeros((len(N),))

np.random.seed(0)
for i in range(len(N)):
    B= np.random.rand(N[i],N[i])
    t0 =time.process_time()
    L,U =myLU(B)
    t[i] = time.process_time() -t0 # Teste die Rechenzeit der LU-Zerlegung für ansteigende Matrixgrößen
# Darstellung
fig, ax=plt.subplots()
ax.loglog(N, t, '*')
ax.set_title('Rechnenzeitverhalten von LU-Zerlegung')
ax.set_xlabel('Matrix Größe N')
ax.set_ylabel('Zeit t')
plt.show()

