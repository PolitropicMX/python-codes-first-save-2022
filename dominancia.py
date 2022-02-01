#table de dominancia
import numpy as np
import math

concordancia = np.array([[ 0,  4,  5, 10],[12,  0,  9, 10],[ 8,  4,  0,  6],[ 8,  3,  7,  0]])
discordancia = np.array([[0, 5, 4, 2],[2, 0, 1, 2],[3, 5, 0, 2],[4, 5, 4, 0]])
domifila = np.zeros((4))
domicolumna = np.zeros((4))

#print(concordancia, discordancia)
e = 0
factorc = 8
factord = 3

for i in range(4):
    print(i,'  iteracion')
    filai = concordancia[i,:]
    columnai = concordancia[:,i]
    filaj = discordancia[i,:]
    columnaj = discordancia[:,i]
    s = np.sum(filai)/3#concordancia fila
    ss = np.sum(filaj)/3#discordancia fila
    sss = np.sum(columnai) /3#concordancia columna
    ssss = np.sum(columnaj)/3#discordancia columna
    print(s,ss,sss,ssss)
    filai = np.delete(filai,i)
    filaj = np.delete(filaj,i)
    columnai = np.delete(columnai,i)
    columnaj = np.delete(columnaj,i)
    print('concorfil concorcol discorfil discorcol')
    print(filai,columnai,filaj,columnaj)
    e = e + 1
    n1 = 0
    m1 = 0
    n2 = 0
    m2 = 0
    for j in range(3):
        if filai[j] >= factorc:
            n1 = n1 +1
        if filaj[j] < factord:
            m1 = m1 + 1
        if columnai[j] >= factorc:
            n2 = n2 +1
        if columnaj[j] < factord:
            m2 = m2 + 1
    print('***************************************************************************')
    print('cf  df  cc  dc')
    print(n1,' ',m1,' ',n2,' ',m2)
    if n1-m1 == 0:
        domifila[i] = n1
    elif n1-m1 > 0:
        domifila[i] = m1
    elif n1-m1 < 0 :
        domifila[i] = n1
    if n2-m2 == 0:
        domicolumna[i] = n2
    elif n2-m2 > 0:
        domicolumna[i] = m2
    elif n2-m2 < 0 :
        domicolumna[i] = n2
    print(filai,columnai,filaj,columnaj)
    print('######################################################')
print('por fila      por columna')
print(domifila,domicolumna)



