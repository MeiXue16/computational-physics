# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:54:25 2021

@author: mei
"""
import numpy as np


def elimination(L, U, b):
    
    n = U.shape[0]
    x= np.zeros((n,))
    y= np.zeros((n,)) 
    sumLY= np.zeros((n,)) 
    sumUX = np.zeros((n,)) 
    y[0] =b[0]
    for i in range(1, n):
        for j in range(i):
            sumLY[i]= sumLY[i] + L[i,j] * y[j]    
        y[i]= b[i]- sumLY[i]  # Vorwärtselimination
    #print('b:',b,'\ny:',y)
    
    x[n-1]= y[n-1]/U[n-1,n-1]
    for k in range(1, n):
        i = n-1-k
        for j in range(1+i, n):
            sumUX[i]= sumUX[i] + U[i,j] * x[j]
        x[i] = (1/U[i,i]) *(y[i]-sumUX[i])  # Rückwärtselimination
        
        
    #print('x:',x)

    return x


def myLU(A):
    
    n= A.shape[0]
    L= np.identity(n)
    U= A
    for j in range (n):
        for i in range(j+1, n) :
            L[i,j] = U[i,j]/U[j,j]
            U[i,j] = 0
            for k in range(j+1, n):
                U[i,k] = U[i,k] -L[i,j]* U[j,k]

    return L, U

