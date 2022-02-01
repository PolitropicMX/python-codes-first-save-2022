# quiero programar un pendulo
import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()

centropendulo = np.array([200,50])
tb = 200
side = 0
speedr = 0
speedt = 0

while True:

    for event in pygame.event.get():
        
        #print(event)
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speedr = -5
            if event.key == pygame.K_s:
                speedr =5
            if event.key == pygame.K_a:
                speedt = -math.pi/100
            if event.key == pygame.K_d:
                speedt = math.pi/100
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speedr = 0
            if event.key == pygame.K_s:
                speedr = 0
            if event.key == pygame.K_a:
                speedt = 0
            if event.key == pygame.K_d:
                speedt = 0


    screen.fill((0,0,0))
    tb = tb + speedr
    side = side +speedt
    playerposition = np.array([(tb*math.cos(-side + math.pi/2)),(tb*math.sin(-side+math.pi/2))])+centropendulo
    pygame.draw.line(screen,(255,0,0),centropendulo,playerposition)

# A partir de aqui terminas
    pygame.display.update()
    clock.tick(30)
