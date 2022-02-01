import pygame, sys
import numpy as np
import math
pygame.init()
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
# variables
segundero = 0
horizonte = 50
n = 10
road = np.arange(horizonte,HEIGHT,10)
print(len(road))

F = np.zeros((n,4))
k = (HEIGHT-horizonte)/(n)
kl = (WIDTH/2)/n
for i in range(n):
    F[i,0] = WIDTH/2 - i*kl
    F[i,1] = i*k + horizonte
    F[i,2] = WIDTH/2 + i*kl
    F[i,3] = F[i,1]
print(F)


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
    #print(segundero)
    
    c = (HEIGHT-horizonte)/1000
    d = (WIDTH/2)/1000
    pygame.draw.line(screen,(255,255,255),[WIDTH/2,horizonte],[0,HEIGHT])
    pygame.draw.line(screen,(255,255,255),[WIDTH/2,horizonte],[WIDTH,HEIGHT])
    pygame.draw.line(screen,(255,255,255),[0,horizonte],[WIDTH,horizonte])
    print(F)
    
    for i in range(n):
        F[i,0] = F[i,0] -  segundero*d
        F[i,2] = F[i,2] + segundero*d
        F[i,1] = F[i,1] + c*segundero
        F[i,3] = F[i,1]
        
        if F[i,1] > HEIGHT:
            #print('ya')
            F[i,3] = horizonte
            F[i,1] = horizonte
            F[i,0] = WIDTH/2
            F[i,2] = WIDTH/2
            print(F)
    for i in range(n):
        pygame.draw.line(screen, (255,255,255), (F[i,0],F[i,1]),(F[i,2],F[i,3]),1)
    #pygame.draw.line(screen,(255,255,255),[(WIDTH/2-segundero*d),(horizonte+segundero*c)],[(WIDTH/2+segundero*d),(horizonte+segundero*c)])
    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)

