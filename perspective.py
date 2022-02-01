import math
import numpy as np
import pygame

WHITE = (255,255,255)

WIDTH, HEIGHT = 800,600
pygame.display.set_caption("3D projection in pygame")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

points = []

points.append(np.matrix([[-1],[-1],[1]]))
points.append(np.matrix([[1],[-1], [1]]))
points.append(np.matrix([[1],[1], [1]]))
points.append(np.matrix([[-1],[1], [1]]))
points.append(np.matrix([[-1],[-1], [-1]]))
points.append(np.matrix([[1],[-1], [-1]]))
points.append(np.matrix([[1],[1], [-1]]))
points.append(np.matrix([[-1],[1], [-1]]))

projection_matrix = np.matrix([
        [1,0,0],
        [0,1,0]
    ])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    #Update stuff

    screen.fill(WHITE)
    #drawing stuff
    for point in points:
        projected2d = np.dot(projection_matrix,point.reshape((3, 1)))
        #pygame.draw.circle(screen, black, (x,y) , 5)

    pygame.display.update()
        
