import pygame, sys
import numpy as np
import math
import csv
import pandas as pd
pygame.init()
HEIGHT, WIDTH = 800,800
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
# variables
segundero = 0
with open("Concrete_Data_Yeh.csv") as datafile:
    data = pd.read_csv(datafile)
varnum3 = data[["cement","slag","flyash"]]
tabla = varnum3.to_numpy()
col = data[["flyash"]]
col1 = data[["cement"]]
col2 = data[["slag"]]
col = col.to_numpy()
col1 = col1.to_numpy()
col2 = col2.to_numpy()
first = col1[0:(len(col1)-1),:]
second = col1[1:(len(col1)),:]
third = col2[0:(len(col2)-1),:]
fourth = col2[1:(len(col2)),:]
d = max(col)-min(col)
for i in range(len(col)):
    tabla[i,2] = int((tabla[i,2]/d)*255)
    tabla[i,0] = tabla[i,0] -min(tabla[:,0])
    tabla[i,1] = tabla[i,1] -min(tabla[:,1])
    col1[i] =col1[i] -min(col1[:])
    col2[i] =col2[i] -min(col2[:])
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Data analisys for Cement content', True, (255,255,255), (0,0,0))
# otras cosas


while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_f:
                pass
    screen.fill((0,0,0))
    # A partir de aqui dibujas
    print(segundero)
    segundero = segundero + 1
    n = math.sin(segundero/99)*200+200
    #la matematica va aqui
    # en puntos
    screen.blit(text, (200,n-100))
    for i in range(len(col)-1):
        pygame.draw.line(screen,(255,255,255),(int(first[i]),int(n+third[i])),(int(second[i]),int(n+fourth[i])),1)
    #en linea
    for i in range(len(col)):
        pygame.draw.circle(screen,[int(255-tabla[i,2]),(100),int(tabla[i,2])],[int(tabla[i,0]),int(tabla[i,1]+n)],5)
    
    #Aqui termina el loop
    
    pygame.display.update()
    clock.tick(30)
