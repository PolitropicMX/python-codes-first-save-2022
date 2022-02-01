import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 400,400
pygame.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
segundero = 0
flujoA = np.array([[100,0],[300,400]])
#pedazos del flujo
ch = 100
ciclos = 4
#los n pendientes de las chunks divididos entre el numero de las chunks
dx = (flujoA[1,0]-flujoA[0,0])/ch
dy = (flujoA[1,1]-flujoA[0,1])/ch
#el vector donde se almacenara los puntos iniciales y finales de cada chunk
listpositions = np.ones((ch+1,2))
#se guardan los incrementos dx y dy sumados a la posicion del punto inicial
for it in range(ch+1):
    listpositions[it,0] = flujoA[0,0] + it*dx
    listpositions[it,1] = flujoA[0,1] + it*dy
print(listpositions)
f = 0
colorstep = int(255/5)

bol = 1
while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bol = -1
            if event.key == pygame.K_UP:
                bol = 1 
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
    x = int((127*math.sin((segundero)/20)+127))

    for i in range(ch):
        f = int((255*math.sin(0.2*i+bol*segundero)**2))
        # por que 255*math.sin()**2?
        #   como sin()**2 tiene un rango entre 0 y 1, al multriplicarlo por un
        #   numero n da una variacion entre cero y ese numero n
        # el segundero es lo que actua como un desfasador lo que hace que se mueva en un sentido
        pygame.draw.line(screen,(f,f,f),(listpositions[i,:]),(listpositions[i+1,:]),100)
    
    #pygame.draw.line(screen,(x,x,x),(50,0),(50,400),100)
    segundero = segundero +1
    print(segundero)

    
    # A partir de aqui dibujas
    # primero creamos una linea

    #Aqui termina el loop
    pygame.display.update()
    clock.tick(20)
