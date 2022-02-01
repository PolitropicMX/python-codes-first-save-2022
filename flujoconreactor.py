import pygame, sys
import numpy as np
import math
pygame.init()
def diferencialde(A,chunks):
    dx = (A[1,0]-A[0,0])/chunks
    dy = (A[1,1]-A[0,1])/chunks
    return dx,dy

def text(a):
    WHITE = (255,255,255)
    fuente = pygame.font.Font(None,30)
    b = fuente.render(a,0,WHITE)
    return b
HEIGHT, WIDTH = 900,400

screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
#variables importantes
segundero = 0
chunks = 20
flxa = np.ones((chunks+1,2))
flxb = np.ones((chunks+1,2))
flxc = np.ones((chunks+1,2))
cuantascorrientes  = 3
#materias primas y corrientes de flujo
fa0 = 30
fb0 = 30
fc = 30
# Tanques de Almacenamiento
#para la especie reactiva A
tanqueA = np.array([[30,0],[30,50]])
anchoA = 50
centroA = np.array([tanqueA[0,0],(tanqueA[1,1]+tanqueA[0,1])/2])
print(centroA)
#para la especie reactiva B
tanqueB = np.array([[30,100],[30,150]])
anchoB = 50
centroB = np.array([tanqueB[0,0],(tanqueB[1,1]+tanqueB[0,1])/2])
#reactor y efluente
reactorposition = np.array([[300,20],[300,200]])
reactorancho = 50
centroreactor = np.array([reactorposition[0,0],(tanqueB[1,1]+tanqueB[0,1])/2])
tanqueprod = np.array([[800,150],[800,250]])
tanqueancho = 60
centroprod = np.array([tanqueprod[0,0],(tanqueprod[1,1]+tanqueprod[0,1])/2])


flujos = ["A" ,"B", "C"]
#variables para crear flujos
#listas de puntos inicial y final de los flujos
flujoA = np.array([centroA,centroA])
flujoB = np.array([centroB,centroB])
flujoC = np.array([centroreactor,centroreactor])
#sus pendientes/diferenciales
ax,ay = diferencialde(flujoA,chunks)
bx,by = diferencialde(flujoB,chunks)
cx,cy = diferencialde(flujoC,chunks)


print(ax,ay,bx,by,cx,cy)
for i in range(chunks+1):
    flxa[i,0] = int(flujoA[0,0] + i*ax)
    flxa[i,1] = int(flujoA[0,1] + i*ay)
    flxb[i,0] = int(flujoB[0,0] + i*bx)
    flxb[i,1] = int(flujoB[0,1] + i*by)
    flxc[i,0] = int(flujoC[0,0] + i*cx)
    flxc[i,1] = int(flujoC[0,1] + i*cy)
direction = 0
select = 0
flxA = 0
flyA = 0
flxB = 0
flyB = 0
flxC = 0
flyC = 0
vx = 0
vy = 0
vefx = 0
vefy = 0
ainr = 0
binr = 0

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vy = 5
            if event.key == pygame.K_UP:
                vy = -5
            if event.key == pygame.K_RIGHT:
                vx = 5
            if event.key == pygame.K_LEFT:
                vx = -5
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
            if event.key == pygame.K_o:
                if select > 1:
                    select = 2
                else:
                    select = select +1
            if event.key == pygame.K_p:
                if select < 1:
                    select = 0
                else:
                    select = select -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                vy = 0
            if event.key == pygame.K_UP:
                vy = 0
            if event.key == pygame.K_RIGHT:
                vx = 0
            if event.key == pygame.K_LEFT:
                vx = 0
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
    #velocidades de control
    
    #variables para crear flujos
    #listas de puntos inicial y final de los flujos
    if select == 0:
        flxA = flxA + vx
        flyA = flyA + vy
        flujoA = np.array([centroA,[centroA[0]+flxA,centroA[1]+flyA]])
    elif select == 1:
        flxB = flxB + vx
        flyB = flyB + vy
        flujoB = np.array([centroB,[centroB[0]+flxB,centroB[1]+flyB]])

    if flujoA[1,0] >= 275 and flujoA[1,0] <= 325 and flujoA[1,1] >= 20 and flujoA[1,1] <= 200:
        ainr = 1
    else:
        ainr = 0
    if flujoB[1,0] >= 275 and flujoB[1,0] <= 325 and flujoB[1,1] >= 20 and flujoB[1,1] <= 200:
        binr = 1
    else:
        binr = 0
    if ainr == 1 and binr == 1:
        print('yes')
        if vefx*cx > centroprod[0]:
            vefx = 0
            print('yes1')
        else:
            vefx = 5
        if vefy*cy > centroprod[1]:
            vefy = 0
        else:
            vefy = 5
        flujoC = np.array([centroreactor,[centroreactor[0]+vefx*cx,centroreactor[1]+vefy*cy]])
        print(cx,cy,vefx,vefy)
        print(flujoC)
    else:
        print('no')

    #sus pendientes/diferenciales
    ax,ay = diferencialde(flujoA,chunks)
    bx,by = diferencialde(flujoB,chunks)
 


    for i in range(chunks+1):
        flxa[i,0] = int(flujoA[0,0] + i*ax)
        flxa[i,1] = int(flujoA[0,1] + i*ay)
        flxb[i,0] = int(flujoB[0,0] + i*bx)
        flxb[i,1] = int(flujoB[0,1] + i*by)
        flxc[i,0] = int(flujoC[0,0] + i*cx)
        flxc[i,1] = int(flujoC[0,1] + i*cy)
    #flujos
    for i in range(chunks):
        f = int((255*math.sin(0.4*i-segundero)**2))
        pygame.draw.line(screen,(0,f,f),(flxa[i,:]),(flxa[i+1,:]),fa0)
        pygame.draw.line(screen,(f,0,f),(flxb[i,:]),(flxb[i+1,:]),fb0)
        pygame.draw.line(screen,(f,f,0),(flxc[i,:]),(flxc[i+1,:]),fc)
    #reactor
    pygame.draw.line(screen,(192,192,192),(reactorposition[0,:]),(reactorposition[1,:]),reactorancho)
    #tanques
    pygame.draw.line(screen,(195,195,195),(tanqueA[0,:]),(tanqueA[1,:]),anchoA)
    pygame.draw.line(screen,(195,195,195),(tanqueB[0,:]),(tanqueB[1,:]),anchoB)
    
    titulo = "En el reactor              =>"
    reaction = "A   +   B   ==> C"
    column = "F0"
    screen.blit(text(flujos[select]),(300,270))
    screen.blit(text(titulo),(50,270))
    screen.blit(text(reaction),(50,300))
    screen.blit(text(column),(0,330))
    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
