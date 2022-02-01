import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
# quiero hacer la animacion de un flujo asi que primero intentare lograr hacer que un
#de circunferencia gira en torno de los vectores de cierta matriz
centro = np.array([HEIGHT/2,WIDTH/2])

# aqui hare la primera malla con 2 for-looops
#yendo de mayor a menor
factor_de_escala = 200
start = 1
stop = 30
delta = int(math.fabs(stop/start))

datos = np.linspace(start,stop, num= delta)
datos = datos
print(datos)
el_sumador = 0
la_malla = np.zeros((len(datos)**2,2))
for k  in range(len(datos)):
    
    for j  in range(len(datos)):
        #print(str(k) + '   '  + str(j) + '    ' +str(el_sumador))

        la_malla[el_sumador,0] = datos[k]
        la_malla[el_sumador,1] = datos[j]
        el_sumador = el_sumador + 1
print(la_malla)
centrom = np.ones((len(datos)**2,2))
centrom[:,0] = centrom[:,0] *(HEIGHT/2)
centrom[:,1] = centrom[:,1] *(WIDTH/2)

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
            
    screen.fill((0,0,0))
    # A partir de aqui dibujas


    for h in range(len(datos)**2):
        pygame.draw.line(screen,(255,00,100),centro,(la_malla[h,:]-centrom[h,:]))

    #Aqui termina el loop
    pygame.display.update()
    clock.tick(30)
