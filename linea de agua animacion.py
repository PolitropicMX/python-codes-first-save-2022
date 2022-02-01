import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
segundero = 1
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
            
    screen.fill((0,0,0))
    # A partir de aqui dibujas

    print(segundero)
    #el segundero es el tiempo
    segundero = segundero +1
    b = int(127*math.sin(2*segundero) + 127)
    print(b)
    r = int(127*math.cos(segundero) + 127)
    g = int(127*math.cos(4*segundero) + 127)
    x = int(20*math.sin(segundero)+127)
    pygame.draw.line(screen,(r,g,b),(0,0),(400,400),700)
    # reactivos
    #A
    pygame.draw.line(screen,(x,40,1),(10,10),(50,10),100)
    
    
    #Aqui termina el loop
    pygame.display.update()
    clock.tick(20)
