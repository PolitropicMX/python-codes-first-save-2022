# concordancia table
import numpy as np
import math

def booleanoc(x1,x2):
    if x1 >= x2:
        return 1
    else:
        return 0

calificaciones = np.array([[8,6,5,4],[6,8,5,9],[7,3,6,8],[4,5,7,4],[1,4,3,5]])
print(calificaciones)
print(calificaciones[4,:])
concordancia = np.zeros((4,4))

for i in range(4):
    for j in range(4):
        if i != j:
            suma = 0
            for k in range(4):
                suma = suma + calificaciones[4,k]*booleanoc(calificaciones[i,k],calificaciones[j,k])
            print(i,j)
            print(suma)
            concordancia[i,j] = suma
            
            
print(concordancia)
            
                
