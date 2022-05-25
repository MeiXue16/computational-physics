# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 00:47:28 2020

@author: mei
"""
import numpy as np
import matplotlib.pyplot as plt
from Diffquot import diffquot

# Aufruf der Ableitungsfunktion und Speichern des Ergebnis in zwei Variablen.
# Wir nutzen hier die Werte für den Beispielaufruf der Funktion diffquot.
fhandle = np.sin  # Definition der input-Funktion
a = -50          # untere Intervallgrenze
b = 50           # obere Intervallgrenze
h = 0.1           # Schrittweite

xwerte, ableitung = diffquot(fhandle, a, b, h)

# Darstellung der Funktion und ihrere Ableitung in einem Plot
fig, ax = plt.subplots()
ax.plot(xwerte, np.sin(xwerte), label='sin(x)')
ax.plot(xwerte, ableitung, label='num. diff.')
ax.set_title('Funktion und ihre Ableitung')
ax.legend(loc='best')
fig.tight_layout()
plt.show()

#%% Gesamtfehler in Abhängigkeit der Schrittweite

anzahl_h = 100000
h_min = 0.00001
h_max = 3

# äquidistanter Vektor im Intervall [h_min, h_max] der Länge anzahl_h
h = np.linspace(h_min, h_max, anzahl_h)
h = np.asarray(h)

dh =np.zeros(shape = (anzahl_h, 1)) # Intialisierung des Gesamtfehler-Vektors


for index in range(anzahl_h):

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h[index])

    df= np.cos(xwerte)# berechne die analytische Ableitung
    eh= np.abs(df - ableitung)

    dh[index]= np.sum(eh) * h[index]# berechne den Gesamtfehler für jedes h
    

fig, ax= plt.subplots()
ax.plot(h,dh)# Darstellung als Linienplot
ax.set_title('Gesamtfehler im interval h=[0,3]')
ax.set_xlabel('Schrittweite h')
ax.set_ylabel('delta h')
plt.show()

#%% lokaler Fehler für feste Schrittweiten

# überschreibe h erneut
h = [0.1, 1, 2]

fig, ax = plt.subplots()

for index in range(3):

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h[index])

    df= np.cos(xwerte) # berechne die analytische Ableitung
    eh= np.abs(df - ableitung)
    
    # Darstellung des Betrags der Differenz beider Ableitungen als Linienplot
    ax.plot(xwerte, eh,
            label='h=%.1f' % h[index])

# Plotbeschriftung
ax.legend(loc='best')
ax.set_xlabel('Koordinate x')
ax.set_ylabel('lokaler Fehler')
ax.set_title('Lokaler Fehler')
fig.tight_layout()
plt.show()

