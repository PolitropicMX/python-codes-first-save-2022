import pygame, sys
import numpy as np
pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption( ' Linear Transformation 1: rotation square' )
screen.fill( BG_COLOR )

points = np.array([50,100])
mesh = np.zeros((len(points),len(points)))
contador = 1
for pointx in range(len(points)):
    for pointy in range(len(points)):
        mesh[contador][1] = mesh[pointx]
        mesh[contador][2] = mesh[pointy]
        contador = contador + 1
print(mesh)        

#POLYCOOR = np.array([[50,50],[50,100],[100,100],[100,50]])

pygame.draw.polygon(screen,LINE_COLOR,POLYCOOR)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
