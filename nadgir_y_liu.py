#diseño basico de procesos
import numpy as np
import pandas as pd
import math

#nadgir y liu

#valores de flujo y volatilidad relativa
data = np.array([[10,100,341,187,40],[8.1,3.7,3.1,2.7,1.0]])
data = np.transpose(data)
n = len(data[:,0])
#funciones cuando se da en volatilidad relativa

def alfa(data,n):# se pasan como parametros un vector y un valor que es el len(del vector)
    x = np.zeros((n,1))
    for i in range(n-1):
        x[i] = data[i]/data[i+1]
    return x

def numbersequences(n):
    return (math.factorial(2*(n-1)))/(math.factorial(n)*math.factorial(n-1))

def cfs(alfa,flujos,n):
    f = np.zeros((n,1))
    for i in range(n-1):
        numerador = 0
        denominador = 0
        for k in range(n):
            if k <= i:
                numerador = numerador + flujos[k]
            if k > i:
                denominador =denominador + flujos[k]
        basket = numerador/denominador
        if basket < 1:
            f[i] = basket*(alfa[i]-1)*100
        else:
            f[i] = (1/basket)*(alfa[i]-1)*100
    return f
    
def cfs2(A,n):
    cfs2 = np.zeros((n,1))
    basket = 0
    maxi = np.max(A)
    print(maxi)
    i = 0
    dot = 0
    for cfs in A:
        dot = dot +cfs
        if cfs == maxi:           
            basket = i
            print(basket)
        i += 1
    cfs2[basket] = 0
 

x = alfa(data[:,1],n)
data = np.hstack((data,x)) 

#numero de secuencias


print(numbersequences(n))        
# necesitamos construir la CFS
d = cfs(data[:,2],data[:,0],n)
data = np.hstack((data,d))
    
print(data)



        

