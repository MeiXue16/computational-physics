# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:25:05 2020

@author: mei
"""

# -*- coding: utf-8 -*-
import numpy as np

def simplex(fhandle, x_start, N_max, p):
#==================================================
# Initialisierung
#==================================================

# Die Skalierungsfaktoren des Downhill-Simplex Verfahrens
    alpha_  = 1.0  # empfohlener Faktor für die Spiegelung
    beta_   = 0.5  # empfohlener Faktor für die Kontraktion
    gamma_  = 2.0  # empfohlener Faktor für die Expansion
    lambda_ = 0.1  # empfohlene Größe des Startsimplex
    e1 =np.array([[1,0]])
    e2 =np.array([[0,1]])
    def x_init(x_st):
        x = x_st
        x=np.append(x, x_st+e1*lambda_,axis=0)
        x=np.append(x, x_st+e2*lambda_,axis=0)
        return x
    
    x =x_init(x_start)
    f = np.array([0,0,0])
   
    N     = 0
    while (N <= N_max):
       
         #Spiegelung
        for i in range(3):
           f[i] = fhandle(x[i,:]) 
           
        N = N+1  
        idx = np.argsort(f)  
        f =f[idx]  #sorted f-value von min bis max
        
        #print('f:',f,'\n')
       
        x_min=x[idx[0], :]
        
        #print('x:',x, '\n')
        
        x_s = np.mean(x,axis=0)-(x[idx[-1], :]/2)  #mittelwert mit Ausnahme des Schlechsten (Spiegelzentrum)
        x_r = x_s - alpha_ * ( x[idx[-1], :] - x_s) #Spiegelung des schlechtesten Punktes am Spiegelzentrum
        f_r = fhandle(x_r)   
        
        if f_r < f[0]:
            x_e = x_s + gamma_ * (x_r - x_s) #Expansionspunkt
            f_e = fhandle(x_e)
            #print('expansion')
            if f_e < f_r:
                x[idx[-1], :]= x_e
                f[-1]= f_e    
            else:
                x[idx[-1], :]= x_r
                f[-1]= f_r
            if np.std(f) > p:
                continue
            else:
                break
            
        elif f_r >=f[0]:
            if f_r <f[1]:
                x[idx[-1], :]= x_r
                f[-1]= f_r
                if np.std(f) > p:
                    continue
                else:
                    break    
              
            elif f_r >= f[1]:
                if f_r < f[-1]:
                    x[idx[-1], :]= x_r
                    f[-1]= f_r
                x_c= x_s + beta_ * (x[idx[-1], :]- x_s) #Berechne Kontraktionspunkt
                f_c =fhandle(x_c)
                #print('kontraktion')
                if f_c < f[-1]:
                   x[idx[-1], :]= x_c
                   f[-1]= f_c
                   if np.std(f) > p:
                       continue
                   else:
                        break
                else:
                    for j in range(3):
                        x[j, :]= (x[j,:] +x_min)/2 # Kompression
                        f[j] = fhandle(x[j,:])
                    #print('kompression')
                    if np.std(f) > p:
                        continue
                    else:
                        break
        
    return x[idx[0], :], f[0], N
    

            
            
        
                
    
    
    
    

