#examen segundo parcial cynthia
# gauss seidel
import numpy as np
coeficientes = np.array([[7,3,1],[2,-9,2],[5,1,12]])
b = np.array([150,250,95])
# valores iniciales
x = np.zeros((3))
#por gauss seidel
iteraciones = 20
for k in range(iteraciones):
    suma = 0
    for r in range(3):
        suma = 0
        for s in range(3):
            if s != r:
                suma = suma + coeficientes[r,s]*x[s]
        x[r] = (b[r] - suma)/coeficientes[r,r]
print('la respuesta es x1 = ',x[0],'  x2 = ',x[1],'   x3 = ',x[2])        
    
