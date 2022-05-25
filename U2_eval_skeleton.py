# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:28:25 2020

@author: mei
"""
import numpy as np
import matplotlib.pyplot as plt
from intrect_skeleton import intrect

# Berechnung der exakten Flächeninhalte

# %% Integrationsfehler in Abhängingkeit von der Schrittweite der Teilintervalle
a= 0
b= 10
anzahl_h = 1000
h = np.logspace(-4, -1, anzahl_h)# logarithmisch äquidistanter Vektor der Schrittweiten

diff = np.zeros(shape=(anzahl_h,3))# Initialisierung der arrays

def fun1(x):# Definition der Funktionen (vgl. MatLab function handles)
    return x
def fun2(x):
    return x**2
def fun3(x):
    return np.exp(x)

def stamm1(x):
    return 0.5*(x**2)
def stamm2(x):
    return (x**3)/3
def stamm3(x):
    return np.exp(x)

fig, ax = plt.subplots()

for counter in range(h.size):# Schleife über alle h zur Berechnung von Integral und dessen Fehler
        area1, xwerte1, stamm_funk1 = intrect(fun1, a, b, h[counter])
        diff[counter,0] = np.abs(area1 - (stamm1(b)-stamm1(a)))
        
        area2, xwerte2, stamm_funk2 = intrect(fun2, a, b, h[counter])
        diff[counter,1] = np.abs(area2 - (stamm2(b)-stamm2(a)))
        
        area3, xwerte3, stamm_funk3 = intrect(fun3, a, b, h[counter])
        diff[counter,2] = np.abs(area3- (stamm3(b)-stamm3(a)))
        
ax.set_xscale('log')# logarithmischer Plot Fehler vs. Schrittweite h
ax.set_yscale('log')
# Darstellung als Linienplot        
ax.plot(h, diff[:,0], label='fehler des Integrals von f(x)= x')
ax.plot(h, diff[:,1], label='fehler des Integrals von f(x)= x^2')    
ax.plot(h, diff[:,2], label='fehler des Integrals von f(x)= exp(x)') # Plotbeschriftung

ax.set_xlabel('Schrittweite h')
ax.set_ylabel('Differenz')
ax.set_title('fehler des Integrals')
ax.legend(loc='best')
fig.tight_layout()
plt.grid(True)
plt.show()

# %% Abhaengigkeit der Integrationskonstante vom linken Intervallrand
# am Bsp. der Stammfunktion F von x^2
a = np.linspace(-100, 100, 1000) # linke Intervallgrenze mit verschiedenen Werten
b = 1000 # rechte Intervallgrenze fest
h= 0.01
y = np.zeros(1000)
for i in range (a.size):
    area, xwerte, stamm_funk = intrect(fun2, a[i], b, h) 
    y[i] = stamm_funk[-1] # Auswertung des numerischen Integrals
y1 =stamm2(b)

fig, ax= plt.subplots() # Darstellung als Linienplot
ax.plot(a, y, label='berechneten Stammfunktion von f(x)= x^2')
ax.axhline(y1, label='analytische Stammfunktion',color='r')
ax.set_xlabel('a')
ax.set_ylabel('F(b)')
ax.set_title('berechneten Stammfunktion')
ax.legend(loc='best')
fig.tight_layout()
plt.show()


