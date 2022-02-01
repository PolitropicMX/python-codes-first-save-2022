import numpy as np

a= np.array([[1,2,3],[4,5,6]])
print(a)
#getting a dimension
dimention = a.ndim
print(dimention)
#getting the shape
shape = a.shape
print(shape)
# getting the size
size = a.itemsize
print(size)
#getting the number of the elements in the matrix
totalnumber = a.nbytes
print(totalnumber)

#acessing/changing specific elements, rows, columns
#getting a specific element
print(a[1,1])
#getting a specific row
print(a[1,:])
#getting a specific column
print(a[:,2])

 #changing an old value to another
a[0,0] = 9
print(a)

listaarecorrer = np.array([0,1,2,3,4,5])
for i in listaarecorrer:
    print(i)
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
d = np.zeros((2,6))
print(d)
for i in range(6):
    d[0,i] = i
    d[1,i] = i**2
print(d)
