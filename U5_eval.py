# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:45:41 2021

@author: mei
"""
import numpy as np
import matplotlib.pyplot as plt
from fft import my_fft
#%%
# AUfgabe 1: sampling einer Schwebung
N=256
p=15
t = np.linspace(0,20*np.pi, N)
w = np.linspace(1,15,p)


spektren = np.zeros((N,p))

fig, ax =plt.subplots()
X, Y= np.meshgrid(w,t)
signal = np.sin(5*X)+np.sin(Y*X)
for i in range (p):
    spektren[:,i] =abs( my_fft(N, signal[:,i]))
image = ax.pcolormesh(X,Y,spektren, cmap='PiYG')
fa =fig.colorbar(image) 
   
fa.set_label('Absolutbeträge der berechneten Spektren')
ax.set_title('Spektralamplituden')
ax.set_xlabel('Kreisfrequenz w')
ax.set_ylabel('t')

fig.tight_layout()
plt.show()

#%%
#Aufgabe 2:Scheinbare Verbesserung der Auflösung durch 
#Einfügen von Nullsignalen

fig, ax =plt.subplots()
n=16
t=np.linspace(0,2*np.pi,n)

signal2 = np.exp(-((t-np.pi)**2)*2)
spek = np.zeros((n,),dtype = 'complex_')
spek = my_fft(n, signal2)
x1 = np.arange(len(spek))
ax.plot(x1, spek)
for i in range (1,6):
    fig, ax =plt.subplots()
    a = n*(2**i)
    t2 = np.insert(t,0, np.zeros((a-n,)) )
    si = np.exp(-((t2-np.pi)**2)*2)
    spe = np.zeros((a,),dtype = 'complex_')
    spe = my_fft(a, si)
    x2 = np.arange(len(spe))
    ax.plot(x2, spe)
    ax.set_title('Spektren von Signalen der verschiednen N= %.0f'%a)
    ax.set_xlabel('N')
    ax.set_ylabel('Spektrum')

plt.show()
