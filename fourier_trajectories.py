import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 800,1200
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
contador = 0
num = 100
step = 1
spin = 1
numvel = 0
stepvel = 0
spinvel = 0
nums = 1
steps = 1
spins = 1
centro1 = np.array([(WIDTH/2),(HEIGHT/2)])
radio1 = np.array([0,-150])
radio2 = np.array([0,-150])
def rotacion (contador):
    rotation = np.array([[math.cos(contador),math.sin(contador)],[-math.sin(contador),math.cos(contador)]])
    return rotation

while True:
    
    
    for event in pygame.event.get():
        
        #print(event)
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               stepvel = -math.pi/100
            if event.key == pygame.K_UP:
                stepvel = math.pi/100
            if event.key == pygame.K_LEFT:
                spinvel = -math.pi/100
            if event.key == pygame.K_RIGHT:
               spinvel = math.pi/100
            if event.key == pygame.K_p:
                numvel = 1
            if event.key == pygame.K_o:
                numvel = -1
            if event.key == pygame.K_q:
                num = 1
                step = 1
                spin = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                stepvel = 0
            if event.key == pygame.K_UP:
                stepvel = 0
            if event.key == pygame.K_LEFT:
                spinvel = 0
            if event.key == pygame.K_RIGHT:
                spinvel = 0
            if event.key == pygame.K_p:
                numvel = 0
            if event.key == pygame.K_o:
                numvel = 0
    # dibujar una animacion
    screen.fill((0,0,0))
    contador = contador + math.pi/10
    step = step + stepvel
    spin = spin + spinvel
    num = num + numvel
    print(step)
    if num == 0:
        num = 1
    fraccion = (2*math.pi)/num
    g = np.zeros((num+1,2))
    h = np.zeros((num+1,2))
    nm = np.zeros((num+1,2))
    mx = np.zeros((num+1,2))
    for i in range(num):
        g[i,:] = np.matmul(radio1,rotacion(steps*fraccion*i))+centro1
        h[i,:] = np.matmul(radio2,rotacion(spins*fraccion*i))+g[i,:]
    g[num,:] = g[0,:]
    h[num,:] = h[0,:]
    for j in range(num):
        pygame.draw.line(screen,(100,100,0),g[j,:],g[j+1,:])
        pygame.draw.line(screen,(100,100,0),h[j,:],h[j+1,:])
    R1 = centro1 + np.matmul(radio1,rotacion(step*fraccion*contador))
    #pygame.draw.line(screen,(2,2,255),(centro1),(R1))
    R2 = R1 + np.matmul(radio2,rotacion(spin*fraccion*contador))
    for k in range(num):
        nm[k,:] = centro1 + np.matmul(radio1,rotacion(step*fraccion*k))
        mx[k,:] = R1 + np.matmul(radio2,rotacion(spin*fraccion*k))
        pygame.draw.line(screen,(10,100,0),nm[k,:],nm[k+1,:])
        pygame.draw.line(screen,(10,100,0),mx[k,:],mx[k+1,:])
    #pygame.draw.line(screen,(0,250,0),R1,(R2))
    #pygame.draw.line(screen,(255,0,255),(50,50),R2)
    #for j in range(num):
    #   pygame.draw.line(screen,(100,100,0),g[j,:],g[j+1,:])
    pygame.display.update()
    clock.tick(60)
    

    #pygame.display.flip()
    

