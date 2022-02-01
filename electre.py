# Metodo Electre
import numpy as np
import math

def booleanoc(x1,x2):
    if x1 >= x2:
        return 1
    else:
        return 0
def suma(A):
    d = 0
    
    for i in range(f):
        for j in range(c):
            d += A[i,j]
    return d

def booleanod(x1,x2):
    c = 0
    if x1 > x2:
        c = x1-x2

    return c
    
# vamos a hacer un programa donde la demos datos de entrada y los trabaje

#valores de prueba (8,6,5,4;6,8,5,9;7,3,6,8;4,5,7,4;1,4,3,5)
# (5,4,6,8;4,6,9,7;7,6,5,6;5,5,7,7;1,3,2,3)
# (10,20,5,10,16;0,5,5,16,10;0,10,0,16,7;20,5,10,10,13;20,10,15,10,13;20,10,20,13,13;3,2,3,1,1)

# (6,4,8,8,7;9,6,8,4,7;7,8,7,7,6;2,1,2,3,2)
# (2,1,1,1,2,1;3,1,3,2,3,1;5,5,4,1,3,4;5,4,4,3,3,3)
# (7,4,9,8;10,6,7,9;6,3,6,7;8,5,5,4;2,1,3,4)

# (4,9,3,7,7;5,7,2,2,6;9,3,7,3,7;7,5,7,4,6;2,7,4,9,2;3,2,1,4,5)

print('Ingrese los datos de entrada')
entrada = input('>>> ')
semicolons = 0
coma = 0
isopen = 0
filas = 1
columnas = 1
shut = 0
racha = 0
building = 0
for i in range(len(entrada)):
    if entrada[i] == ';':
        semicolons = semicolons +1
        shut = 1
    elif entrada[i] == ',' and shut == 0:
        coma = coma + 1
filas = filas + semicolons
columnas =  coma + columnas
elementos = filas*columnas
calificaciones = np.zeros((elementos))
#print(calificaciones)
d = 0
for i in range(len(entrada)):
    if entrada[i] == ';':
        if d < elementos and racha != 0:
            calificaciones[d] = int(building)
            d = d +1
        racha = 0
    elif entrada[i] == ',' and racha != 0:
        if d < elementos:
            calificaciones[d] = int(building)
            d = d +1
        racha = 0
    elif entrada[i] == '(' and racha != 0:
        if d < elementos:
            calificaciones[d] = int(building)
            d = d +1
        isopen = 1
        racha = 0
    elif entrada[i] == ')' and racha != 0:
        if d < elementos:
            calificaciones[d] = int(building)
            d = d +1
        isopen = 0
        racha = 0
    elif entrada[i] == ' ':
        if d < elementos and racha != 0:
            calificaciones[d] = int(building)
            d = d +1
        racha = 0
    elif entrada[i] == '0':
        racha = racha + 1
    elif entrada[i] == '1':
        racha = racha + 1
    elif entrada[i] == '2':
        racha = racha + 1
    elif entrada[i] == '3':
        racha = racha + 1
    elif entrada[i] == '4':
        racha = racha + 1
    elif entrada[i] == '5':
        racha = racha + 1
    elif entrada[i] == '6':
        racha = racha + 1
    elif entrada[i] == '7':
        racha = racha + 1
    elif entrada[i] == '8':
        racha = racha + 1
    elif entrada[i] == '9':
        racha = racha + 1
    
    if racha != 0:
        building = (entrada[(i-racha+1):(i+1)])
    else:
        building =0
    #print(entrada[i],racha,building)
calificaciones = calificaciones.reshape((filas,columnas))
print('Tabla de calificaciones')
print(calificaciones)
print('filas',filas,' columnas',columnas)

# Ahora vamos a formar la tabla de concordancias
concordancia = np.zeros(((filas-1),(filas-1)))
for i in range((filas-1)):
    for j in range((filas-1)):
        if i != j:
            suma = 0
            for k in range(columnas):
                suma = suma + calificaciones[(filas-1),k]*booleanoc(calificaciones[i,k],calificaciones[j,k])
            concordancia[i,j] = suma
print('Tabla de concordancias')
print(concordancia)

discordancia = np.zeros(((filas-1),(filas-1)))
for i in range((filas-1)):
    for j in range((filas-1)):
        if i != j:
            memory = np.zeros((1,columnas))
            for k in range(columnas):
                memory[0,k] = int(booleanod(calificaciones[i,k],calificaciones[j,k]))
                #print(calificaciones[i,k],calificaciones[j,k])
                #print(memory[0,k])
            discordancia[j,i] = np.amax(memory)
print('Tabla de Discordancia')
print(discordancia)
#factor de concordancia
sumac = np.sum(concordancia)
denominator = (filas-1)**2-(filas-1)
facc = sumac/denominator
factorc = math.ceil(facc)
print('Factor de Concordancia')
print(facc,' ==> ',factorc)
sdf = np.reshape(concordancia,-1)
for d in sdf:
    if d >= factorc:
        print(d)
        
#factor de discordancia

sumad = np.sum(discordancia)
facd = (sumad/denominator)
print('Factor de Discordancia')
factord = math.floor(facd)
print(facd,' ==> ',factord)
asd = np.reshape(discordancia,-1)
for f in asd:
    if f <= factord:
        print(f)
opcion = 0
while opcion == 0:
    #Tabla de dominancia
    domifila = np.zeros((filas-1))
    domicolumna = np.zeros((filas-1))
    e = 0
    for i in range((filas-1)):
        #print(i,'  iteracion')
        filai = concordancia[i,:]
        columnai = concordancia[:,i]
        filaj = discordancia[i,:]
        columnaj = discordancia[:,i]
        filai = np.delete(filai,i)
        filaj = np.delete(filaj,i)
        columnai = np.delete(columnai,i)
        columnaj = np.delete(columnaj,i)
        #print('concorfil concorcol discorfil discorcol')
        #print(filai,columnai,filaj,columnaj)
        e = e + 1
        n1 = 0
        m1 = 0
        n2 = 0
        m2 = 0
        for j in range((filas-2)):
            if int(filai[j]) >= factorc & int(filaj[j]) <= factord:
                n1 = n1 +1
            if int(columnai[j]) >= factorc & int(columnaj[j]) <= factord:
                n2 = n2 +1
        domifila[i] = n1
        domicolumna[i] = n2
        #print(i,'iteracion',n1,n2)
    fc = domifila-domicolumna
    print('Tabla de Dominancia')
    print('por fila      por columna    Alternativa F-C')
    for d in range(len(domifila)):
        print(domifila[d],'           ',domicolumna[d],'                  ',(d+1),'              ',fc[d])
    print('No salio como esperaba? Presione 1 para modificar los factores')
    siono = input('>>> ')
    if siono == '1':
        print('Los factores actualmente son: factorc = ',factorc,', factord = ',factord)
        print('para factor c')
        factorc = int(input('>>> '))
        print('para factor d')
        factord = int(input('>>> '))
    else:
        opcion = 1
