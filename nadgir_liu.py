import numpy as np
import math

#entrada de datos
b = 1
while b == 1:
    print('Cuantos componentes tiene su mezcla?')
    componentes = int(input('>>> '))
    print('Ingrese la lista de sus masas')
    masas = input('>>> ')
    #(12,23,34,45)
    # (300,70,1000,400,800,10)
    listamasas= np.zeros((componentes))#aqui guardaremos los flujos ya obtenidos
    plus = 0
    w = 0
    canasta = ''
    for i in range(len(masas)):
        if masas[i + plus] == '(':
            pass
        elif masas[i + plus] == ')':
            listamasas[w] = int(canasta)
            w = w +1
        elif masas[i + plus] == ',':
            listamasas[w] = int(canasta)
            w = w +1
            canasta = ''
        elif masas[i + plus] == '0':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '1':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '2':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '3':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '4':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '5':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '6':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '7':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '8':
            canasta = canasta + masas[i]
        elif masas[i + plus] == '9':
            canasta = canasta + masas[i]
        #print(canasta)
    
    if len(listamasas) != w:
        print('No concuerdan los datos')
        b = 1
    else:
        b = 0
print(listamasas, w)
v = 1
listaki = np.zeros((componentes))
listateb= np.zeros((componentes))
while v == 1:
    print('Que datos le han provisto?:')
    print('Ojo ya deben estar acomodados')
    print('Ki ( 0) Teb (1)')
    opcion = int(input('>>> '))
    if opcion == 1:
        print('Ingrese la lista de  T eb')
        teb = input('>>> ')
        # (10.274,4.049,3.564,2.91,0.395,0.009)
        v = 0
        plus = 0
        w = 0
        canasta = ''
        for i in range(len(teb)):
            if teb[i + plus] == '(':
                pass
            elif teb[i + plus] == ')':
                listateb[w] = float(canasta)
                w = w +1
            elif teb[i + plus] == ',':
                listateb[w] = float(canasta)
                w = w +1
                canasta = ''
            elif teb[i + plus] == '.':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '0':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '1':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '2':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '3':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '4':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '5':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '6':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '7':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '8':
                canasta = canasta + teb[i]
            elif teb[i + plus] == '9':
                canasta = canasta + teb[i]
            print(teb)
    elif opcion == 0:
        print('Ingrese la lista de  Ki')
        ki = input('>>> ')
        v = 0
        plus = 0
        w = 0
        canasta = ''
        for i in range(len(ki)):
            if ki[i + plus] == '(':
                pass
            elif ki[i + plus] == ')':
                listaki[w] = float(canasta)
                w = w +1
            elif ki[i + plus] == ',':
                listaki[w] = float(canasta)
                w = w +1
                canasta = ''
            elif ki[i + plus] == '.':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '0':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '1':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '2':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '3':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '4':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '5':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '6':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '7':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '8':
                canasta = canasta + ki[i]
            elif ki[i + plus] == '9':
                canasta = canasta + ki[i]
        print(listaki)
    
#Coeficiente de Facilidad de Separacion
#primero obtenemos las deltas, estas permanecen constantes


