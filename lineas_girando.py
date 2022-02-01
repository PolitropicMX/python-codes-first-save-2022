import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 800,600
screen = pygame.display.set_mode((HEIGHT,WIDTH))

square = np.array([200,100,80,80])
contador = 0
clock = pygame.time.Clock()
poligon = np.array([[100,100],[200,100],[200,200],[100,200]])
centro = np.array([[150,150],[150,150],[150,150],[150,150]])
linea = []
movingthrought = np.array([400,300])
radio = np.array([-100, 0])
centro1 = np.array([-50,0])
step = 1
spin = 1
num = 1
def rotacion (contador):
    rotation = np.array([[math.cos(contador),math.sin(contador)],[-math.sin(contador),math.cos(contador)]])
    return rotation
def rotacion2(v):
    rotation = np.array([[math.cos(v),math.sin(v)],[-math.sin(v),math.cos(v)]])
    return rotation
 

while True:
    
    
    for event in pygame.event.get():
        
        #print(event)
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               step = step + 1
               print(step,spin
                     )
            if event.key == pygame.K_UP:
               step = step - 1
               print(step,spin)
            if event.key == pygame.K_LEFT:
               spin = spin - 1
               print(step,spin)
            if event.key == pygame.K_RIGHT:
               spin = spin + 1
               print(step,spin)
            if event.key == pygame.K_p:
                num = num + 1
            if event.key == pygame.K_s:
                num = num - 1    

    # dibujar una animacion
    screen.fill((0,0,0))
    contador = contador + math.pi/10
    R1 = movingthrought-np.matmul(radio,rotacion(step*contador))
    pygame.draw.line(screen,(255,250,0),(400,300),(R1))
    R2 = R1-np.matmul(centro1,rotacion(spin*contador))
    pygame.draw.line(screen,(255,250,0),R1,(R2))
    pygame.draw.line(screen,(255,0,255),(50,50),R2)

    pygame.display.update()
    clock.tick(30)
    

    #pygame.display.flip()
    
