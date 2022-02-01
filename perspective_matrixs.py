import pygame, sys
import numpy as np
import math
pygame.init()
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
# variables
segundero = 0




# otras cosas

def mathpers(fov, aspect, znear, zfar):
    mat = np.zeros((3,3))
    mat[0,0] = aspect*(1/(math.atan(fov/2)))
    mat[1,1] = (1/(math.atan(fov/2)))
    mat[2,2] = zfar/(zfra-znear)
    mat[2,3] = -((zfar*znear)/(zfar-znear))
    mat[3,2] = 1
    return mat

def matmulti(mat,v):
    res = np.matmul(mat,v)
    if res[3] != 0:
        res[0] = res[0]/res[3]
        res[1] = res[1]/res[3]
        res[2] = res[2]/res[3]


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

    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)

