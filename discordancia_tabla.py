#tabla de discordancias
import numpy as np
import math

def booleanod(x1,x2):
    c = 0
    if x1 < x2:
        c = x2-x1
    return c

calificaciones = np.array([[8,6,5,4],[6,8,5,9],[7,3,6,8],[4,5,7,4],[1,4,3,5]])
print(calificaciones)
print(calificaciones[4,:])
discordancia = np.zeros((4,4))

for i in range(4):
    for j in range(4):
        if i != j:
            memory = np.zeros((1,4))#columnas
            for k in range(4):
                print(calificaciones[i,k],calificaciones[j,k])
                memory[0,k] = int(booleanod(calificaciones[i,k],calificaciones[j,k]))
            discordancia[i,j] = np.amax(memory)    
print(discordancia)
            
