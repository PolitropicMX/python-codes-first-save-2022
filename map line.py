import pygame, sys
import numpy as np
import math
pygame.init()
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
# variables
segundero = 0
der = 0
vel = 5
cuantaslineas = 6
espaciado = WIDTH/cuantaslineas
verticallines = np.arange(0,WIDTH,espaciado)
xi = np.zeros(cuantaslineas)
for i in range(cuantaslineas):
        xi[i] = verticallines[i]
# otras cosas
yi = 0
yf = HEIGHT

def pasala(x):
    return x

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
                cuantaslineas = cuantaslineas + 1
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_e:
                cuantaslineas = cuantaslineas - 1
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                der = der - vel
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_d:
                der = der + vel
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                cuantaslineas = cuantaslineas
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_e:
                cuantaslineas = cuantaslineas
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                der = 0
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_d:
                der = 0
            if event.key == pygame.K_f:
                pass
    screen.fill((0,0,0))
    # A partir de aqui dibujas
    #print(segundero)

    
    print(der,cuantaslineas)
    for i in range(cuantaslineas):
       pygame.draw.line(screen,(255,255,255), [xi[i],yi],[xi[i],yf],1)
    for i in range(cuantaslineas):
        if xi[i] > WIDTH:
            xi[i] = 0
        if xi[i] < 0:
            xi[i] = WIDTH
        xi[i] = xi[i] + der
    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
