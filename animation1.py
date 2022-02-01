# tiss is going to be a shitty game animation programm i'm goin' to make with pygame

import pygame, sys
import numpy as np
import math

HEIGHT, WIDTH = 800,600
screen = pygame.display.set_mode((HEIGHT,WIDTH))

square = np.array([200,100,80,80])
contador = 0

poligon = np.array([[100,100],[200,100],[200,200],[100,200]])
centro = np.array([[150,150],[150,150],[150,150],[150,150]])

def rotacion (contador):
    rotation = np.array([[math.cos(contador+math.pi/4),math.sin(contador+math.pi/4)],[-math.sin(contador+math.pi/4),math.cos(contador+math.pi/4)]])
    return rotation



while True:
    
    for event in pygame.event.get():
        #print(event)
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                screen.fill((0,0,0))
                contador = contador + 5
                poligon = np.matmul((poligon-centro),rotacion(contador))+centro
                pygame.draw.polygon(screen,(0,255,0),(poligon))
                square = np.array([200,100,80,80])
                square[0] = square[0] + contador
                pygame.draw.rect(screen,(255,0,0),square)
    
    pygame.display.update()
    


    #pygame.display.flip()
    
    

