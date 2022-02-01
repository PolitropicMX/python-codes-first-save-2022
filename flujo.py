import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 800,900
pygame.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
segundero = 0
flujoA = np.array([[100,0],[300,400]])
ch = 100
ciclos = 4
dx = (flujoA[1,0]-flujoA[0,0])/ch
dy = (flujoA[1,1]-flujoA[0,1])/ch
listpositions = np.ones((ch+1,2))
reactorposition = np.array([[500,100],[700,300]])


for it in range(ch+1):
    listpositions[it,0] = flujoA[0,0] + it*dx
    listpositions[it,1] = flujoA[0,1] + it*dy
print(listpositions)

colorstep = int(255/5)

bol = 1
first = 0
second = 0
third = 0
fourth = 0
fi = 0
s = 0
t = 0
fo = 0
m=0
while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                 fi = 10
            if event.key == pygame.K_UP:
                fi = - 10
            if event.key == pygame.K_RIGHT:
                s = 10
            if event.key == pygame.K_LEFT:
                s = - 10
            if event.key == pygame.K_i:
                bol = 1 
            if event.key == pygame.K_k:
                bol = -1
            if event.key == pygame.K_w:
                t = - 10
            if event.key == pygame.K_a:
                fo = - 10
            if event.key == pygame.K_s:
                 t = 10
            if event.key == pygame.K_d:
                 fo = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                 fi = 0
            if event.key == pygame.K_UP:
                fi =  0
            if event.key == pygame.K_RIGHT:
                s = 0
            if event.key == pygame.K_LEFT:
                s = 0
            if event.key == pygame.K_w:
                t = 0
            if event.key == pygame.K_a:
                fo = 0
            if event.key == pygame.K_s:
                 t = 0
            if event.key == pygame.K_d:
                 fo = 0
            
    screen.fill((0,0,0))
    first = first + fi
    second = second + s
    third = third + t
    fourth = fourth +fo
    flujoA = np.array([[100+fourth,0+third],[100+second,800+first]])
    print(flujoA)
    dx = (flujoA[1,0]-flujoA[0,0])/ch
    dy = (flujoA[1,1]-flujoA[0,1])/ch
    listpositions = np.ones((ch+1,2))
    for it in range(ch+1):
        listpositions[it,0] = flujoA[0,0] + it*dx
        listpositions[it,1] = flujoA[0,1] + it*dy

    for i in range(ch):
        f = int((255*math.sin(0.2*i+bol*segundero)**2))
        # por que 255*math.sin()**2?
        #   como sin()**2 tiene un rango entre 0 y 1, al multriplicarlo por un
        #   numero n da una variacion entre cero y ese numero n
        # el segundero es lo que actua como un desfasador lo que hace que se mueva en un sentido
        pygame.draw.line(screen,(0,f,f),(listpositions[i,:]),(listpositions[i+1,:]),100)

    pygame.draw.rect(screen,(192,192,192),reactorposition)
    
    #pygame.draw.line(screen,(x,x,x),(50,0),(50,400),100)
    segundero = segundero +1
    print(segundero)

    
    # A partir de aqui dibujas
    # primero creamos una linea

    #Aqui termina el loop
    pygame.display.update()
    clock.tick(20)
