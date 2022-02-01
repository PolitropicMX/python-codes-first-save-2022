import pygame, sys
import numpy as np
import math
pygame.init()
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
# variables
segundero = 0
class Flows:
    def __init__(self,xa,ya,xb,yb):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.ch = 50
        self.flujo = np.array([[xa,ya],[xb,yb]])
        #las pendientes
        self.dx = (self.flujo[1,0]-self.flujo[0,0])/self.ch
        self.dy = (self.flujo[1,1]-self.flujo[0,1])/self.ch
        #matriz de ch + 1 filas y 2 columnas
        self.listofpositions = np.ones((self.ch+1,2))
        
        for it in range(self.ch+1):
            self.listofpositions[it,0] = self.flujo[0,0] + it*self.dx
            self.listofpositions[it,1] = self.flujo[0,1] + it*self.dy


    def draw(self,segundero):
        #aqui se debe escribir lo que se va a dibujar en la pantalla de juego
        for i in range(self.ch):
            f = int((255*math.sin(0.4*i-segundero)**2))
            pygame.draw.line(screen,(f,f,f),(self.listofpositions[i,:]),(self.listofpositions[i+1,:]),50)

        


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
    print(segundero)
    f1 = Flows(100,100,100,200)
    f1.draw(segundero)
    f2 = Flows(100,200,200,200)
    f2.draw(segundero)
    f3 = Flows(200,200,200,100)
    f3.draw(segundero)
    f4 = Flows(200,100,100,100)
    f4.draw(segundero)
    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
