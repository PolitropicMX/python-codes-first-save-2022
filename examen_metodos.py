# pregunta 1
# realizar 3 iteraciones
import numpy as np
import math

r = 3
if r == 1:
        


    f = lambda x: 4*x + 3*math.sin(x)-7.9
    df = lambda x: 4 + 3*math.cos(x)
    x0 = 1.5
    for i in range(3):
        x1 = x0 - f(x0)/df(x0)
        x0 = x1
        print(x0)
    print(f'Solucion x = {x0:.4f}')

elif r == 2:
    pass
##import numpy as np
##def gaussjordan(A):
##    r = A[0,:]
##    columna = len(r)
##    fila = columna - 1
##    for i in range(fila):
##        pivote = A[i,i]
##        A[i,:] = A[i,:]/pivote
##        for k in range(fila):
##            if (k!=i):
##                factor = A[k,i]
##                A[k,:] = A[k,:] - A[i,:]*factor
##    return A
##A = np.array([[5,14,0,7,200],[0,15,6,-4,120],[0,0,2,3,100],[0,8,0,7,-90]],float)
###A = np.array([[3,5,],[],[]])
##print(A)
##s = gaussjordan(A)
##print(s)
elif r == 3:
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-np.pi,np.pi,100)
y1 = x*np.sin(x) + 2
y2 = x*np.cos(x) + 3

plt.plot(x,y1)
plt.plot(x,y2)

plt.show()

