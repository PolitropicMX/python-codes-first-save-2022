import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
tl = 1
tr = 0
bl = 0
br = 1

clock = pygame.time.Clock()
step=20;spin = 1;num=0

while True:

    for event in pygame.event.get():
        
        #print(event)
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               step = step + 1
            if event.key == pygame.K_UP:
               step = step - 1
            if event.key == pygame.K_q:
               tl = tl - 1
            if event.key == pygame.K_w:
                tl = tl + 1
            if event.key == pygame.K_e:
                tr = tr - 1
            if event.key == pygame.K_r:
                tr = tr + 1
            if event.key == pygame.K_a:
               bl = bl - 1
            if event.key == pygame.K_s:
                bl = bl + 1
            if event.key == pygame.K_d:
                br = br - 1
            if event.key == pygame.K_f:
                br = br + 1 

    screen.fill((0,0,0))
#A partir de aqui dibujas
    divition = round(HEIGHT/step)
    firsts = np.arange((divition+1))
    firsts = firsts*step
    seconds = np.zeros((2,divition+1))
    seconds[0,:] = firsts[:]

#    print(seconds)
    thirds = np.ones((divition+1))
    fourts = np.zeros((2,divition+1))
    thirds = thirds*400
    fourts[0,:] = firsts[:]
    fourts[1,:] = thirds[:]
#    print(fourts)
    fifths = np.zeros((2,divition+1))
    fifths[1,:] = firsts[:]
    sixths = np.ones((2,divition+1))
    sixths[0,:] = thirds
    sixths[1,:] = firsts[:]
    matt = np.array([[tl, tr],[bl ,br]])
    turning = np.array([[1, 0],[0, -1]])
    matt = np.matmul(matt,turning)
    centro = np.ones((2,divition+1))
    centro[0,:] = np.zeros((divition+1))
    centro[1,:] = 400*centro[1,:]
    newseconds = np.matmul(matt,seconds) + centro
    newfourts = np.matmul(matt,fourts) + centro
    newfifths = np.matmul(matt,fifths) + centro
    newsixths= np.matmul(matt,sixths) + centro
    print(matt)
    for i in range(divition+1):
        pygame.draw.line(screen,(0,100,255),(seconds[:,i]),(fourts[:,i]))
        pygame.draw.line(screen,(0,100,255),(fifths[:,i]),(sixths[:,i]))
        pygame.draw.line(screen,(250,100,255),(newseconds[:,i]),(newfourts[:,i]))
        pygame.draw.line(screen,(250,100,255),(newfifths[:,i]),(newsixths[:,i]))
# A partir de aqui terminas
    pygame.display.update()
    clock.tick(30)
