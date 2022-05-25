# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:34:50 2020

@author: mei
"""

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from simplex import simplex

def himmelblau(coordvals):
  
    x = coordvals[...,0]
    y = coordvals[...,1]

    fvalues = (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

    return fvalues

n_max=100
p = 1e-18

a= np.linspace(-10,10,20)
b= np.linspace(-10,10,20)

for i in a:
    for j in b:
        x_start = np.array([[i,j]])
        x_min,f_min,N =simplex(himmelblau, x_start, n_max, p )
        if f_min ==0:
            print('\n',x_start,'\n' , x_min,'\n' )
            #print('Schritte',N,'\nx_start',x_start,'\nx_min:' , x_min, '\nf_min:',f_min, '\n')

#%% 
#x_start=[-1,-1]
#f_min in Abhangigkeit von N_max:
x_start = np.array([[-1,-1]])
N_max= np.arange(0,100,1)

fig, ax = plt.subplots()
f_m = np.zeros((len(N_max),1))
for i in N_max:
    x_min,f_min,N =simplex(himmelblau, x_start, i, 0 )
    f_m[i]=f_min

ax.plot(N_max, f_m)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_title('Konvergenzverhalten von f_min')
ax.set_xlabel('N_max')
ax.set_ylabel('f_min')
plt.show()
    
    
    



