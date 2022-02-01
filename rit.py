import pygame, sys
import numpy as np
import math
# Initialize the pygame
pygame.init()

#Create the screen
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Pygame project")
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#Create the clock
clock = pygame.time.Clock()

#Codeline for the image background
#background = pygame.image.load('')

# variables
segundero = 0


# programare visualmente el diagrama de





# otras cosas
def dot(xi,yi,r):
    pygame.draw.circle(screen,(255,255,0),(xi,yi),r)
def line(xi,yi,xf,yf):
    pygame.draw.line(screen,(255,255,255),(xi,yi),(xf,yf),1)
def rect(xi,yi,w,h):
    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
def text(string,xi,yi):
    textsurface = font.render(string,False,(10,100,100))
    screen.blit(textsurface,(xi,yi))
def panel(xi,yi,string):
    w,h = 250,40
    pygame.draw.rect(screen,(25,25,255),(xi,yi,w,h))
    textsurface = font.render(string,False,(255,255,255))
    screen.blit(textsurface,(xi,yi))

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
                cur_x = cur_x
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                cur_x = cur_x
            if event.key == pygame.K_s:
                cur_y = y
            if event.key == pygame.K_d:
                cur_x = cur_x
            if event.key == pygame.K_f:
                pass
    screen.fill((0,0,0))
    # A partir de aqui dibujas
    #print(segundero)
    # panel
    #diferencia entre opciones es de 50 siempre
    panel(100,100,'Menu')
    panel(100,150,'crear corriente')
    panel(100,200,'creat calculacion')
    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
