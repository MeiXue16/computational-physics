# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:38:25 2021

@author: Mei Xue
"""
import numpy as np
from alpha import alpha_osci
import matplotlib.pyplot as plt
# Startparameter

x0 = 1
v0 = 0
w  = 1
T  = 20

# Analytische Lösungen
def x_anal(t):
    return x0 * np.cos(w*t)+ np.sin(w*t)*v0/w
def v_anal(t):
    return -x0 *w* np.sin(w*t) + v0* np.cos(w*t)

x_max = np.sqrt(x0**2 + (v0/w)**2)
v_max = w* x_max

# %% Beispiel 1: Globaler Fehler der Lösung in Abhängigkeit von der Schrittweite in der Zeit

# Variiere alpha und dt
alpha = np.array([0 , 0.5, 0.501, 0.51, 1])
dt = np.logspace(-3, 0, 21)
I= np.size(dt)
N  = np.ceil(T/dt)

# definieren globaler Fehler
def fehler_global(x,v):
    return np.sqrt((( x[-1]- x_anal(T) )/x_max)**2 + (( v[-1] - v_anal(T) )/ v_max)**2 )

fig, ax =plt.subplots()
# Berechne globalen Fehler
e_global = np.zeros((I, 5))
for j in range (5):
    for i in range (I):
        x, v ,t = alpha_osci(x0, v0, w, alpha[j], int(N[i]), T)
        e_global[i,j] = fehler_global(x,v)
# Darstellung

e_plot = ax.loglog(dt, e_global , dt , 15*dt, 'k:', dt, dt**2, 'k-.')
ax.set_title('Konvergenzverhalten des globalen Fehler für verschiedene Werte des α')
ax.set_xlabel('Zeitschritt dt = T/N')
ax.set_ylabel('globaler Fehler ε(T)')
for i in range (5):
    e_plot[i].set_label('α = %g' %alpha[i])
    
e_plot[-2].set_label('~dt')
e_plot[-1].set_label('~dt^2')
ax.legend()
ax.grid()
fig.tight_layout()
plt.show()


# %% Beispiel 2: Energieerhaltung -- Konvergenzverhalten
def E(x,v):
    return v**2+ (w*x)**2

# Variiere Zeitschritt
alpha = np.array([0, 0.5, 1])
dt = np.logspace(-4, 0, 20)
N  = np.ceil(T/dt)

I = np.size(dt)

# Berechne Energie zur Stoppzeit
E_T = np.zeros((I, 3))
for j in range (3):
    for i in range (I):
        x, v ,t = alpha_osci(x0, v0, w, alpha[j], int(N[i]), T)
        E_T[i,j] = E(x[-1],v[-1])

# Darstellung
fig, ax =plt.subplots()

E_plot = ax.loglog(dt, E_T)
ax.set_title('Konvergenzverhalten der Energie')
ax.set_xlabel('Zeitschritt dt = T/N')
ax.set_ylabel('Energie des harmonischen Oszillators E(T)')
for i in range (3):
    E_plot[i].set_label('α = %g' %alpha[i])
ax.legend()
ax.grid()
fig.tight_layout()
plt.show()

# %% Beispiel 3: Energieerhaltung -- Zeitverhalten
def E(x,v):
    return v**2+ (w*x)**2
# Wähle Zeitschritt
alpha = np.array([0, 0.5, 1])
dt = 0.01
N  = int(T/dt)

# Berechne zeitliche Entwicklung der Energie und der Systemvariablen
Ez =np.zeros((N+1, 3))

for i in range (3):
    x, v ,t = alpha_osci(x0, v0, w, alpha[i], N, T)
    Ez[:,i] = E(x, v)

# Darstellung
fig, ax =plt.subplots()

E2_plot = ax.plot(t, Ez)
ax.set_title('Zeitverhalten der Energie mit dt = 0.01')
ax.set_xlabel('Zeitpunkt t ')
ax.set_ylabel('Energie des harmonischen Oszillators E(t)')
for i in range (3):
    E2_plot[i].set_label('α = %g' %alpha[i])
ax.legend()
ax.grid()
fig.tight_layout()
plt.show()


