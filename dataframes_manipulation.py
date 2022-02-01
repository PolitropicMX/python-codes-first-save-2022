import pygame, sys
import numpy as np
import math
import csv
import pandas as pd

with open("Concrete_Data_Yeh.csv") as datafile:
    data = pd.read_csv(datafile)

print(data)
print(data.size)
print(data.head())
# haremos un extractor de columnas

# extraemos 3 variables/ columnas
varnum3 = data[["cement","slag","flyash"]]
col1 = data[["cement"]]
col2 = data[["slag"]]
col = data[["flyash"]]
print("___________________________________")
print(varnum3)
print(type(varnum3))
print("___________________________________")
tabla = varnum3.to_numpy()
col = col.to_numpy()
col1 = col1.to_numpy()
col2 = col2.to_numpy()
print(tabla)

### no modificar
##print(max(col))
##print(min(col))
d = max(col)-min(col)
for i in range(len(col)):
    tabla[i,2] = int((tabla[i,2]/d)*255)
    tabla[i,0] = tabla[i,0] - min(tabla[:,0])
    tabla[i,1] = tabla[i,1] - min(tabla[:,1])
print(tabla)
print("___________________________________")
first = col1[0:(len(col1)-1),:]
second = col1[1:(len(col1)),:]
third = col2[0:(len(col2)-1),:]
fourth = col2[1:(len(col2)),:]
print((first))
print(second)
print(third)
print(fourth)
