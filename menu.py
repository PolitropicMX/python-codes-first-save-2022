import pygame, sys
import numpy as np
import math
from pygame.locals import *
pygame.init()
HEIGHT, WIDTH = 400,400
WHITE = (255,255,255)
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
fuente = pygame.font.Font(None,30)
texto1 = fuente.render("Menu",0,WHITE)
opcion1 = fuente.render("opcion 1",0,WHITE)
opcion2 = fuente.render("opcion 2",0,WHITE)
opcion3 = fuente.render("opcion 3",0,WHITE)
opcion4 = fuente.render("opcion 4",0,WHITE)
position = 0
up=0
while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                up = up +1 
            if event.key == pygame.K_UP:
                up = up -1
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
    b = 30*up
    if up <= -1:
        up = 0
    elif  up >= 5:
        up = 4

    pygame.draw.circle(screen,(200,200,0),(300,65+b),10)
    screen.blit(texto1,(40,50))
    screen.blit(opcion1,(40,50+30))
    screen.blit(opcion2,(40,50+60))
    screen.blit(opcion3,(40,50+90))
    screen.blit(opcion4,(40,50+120))

    #Aqui termina el loop
    pygame.display.update()
