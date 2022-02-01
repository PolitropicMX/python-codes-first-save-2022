import pygame, sys

from pygame.locals import *
pygame.init()
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
display = pygame.Surface((400,400))
pygame.display.set_caption("Pygame project")
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
grass_img = pygame.image.load('unit.png').convert()
water_img = pygame.image.load('water.png').convert()
tree_img = pygame.image.load('tree.png').convert()
wood_img = pygame.image.load('wood.png').convert()
player_texture = {'1' : pygame.image.load('player1.png').convert(),
                            '2' : pygame.image.load('player2.png').convert(),
                            '3' : pygame.image.load('player3.png').convert(),
                            '4' : pygame.image.load('player4.png').convert()}
for i in player_texture:
    player_texture[str(i)].set_colorkey((0,0,0))
grass_img.set_colorkey((0,0,0))
water_img.set_colorkey((0,0,0))
tree_img.set_colorkey((0,0,0))
wood_img.set_colorkey((0,0,0))
clock = pygame.time.Clock()
d = 'w'
#PLAYER
pos_x = 0
pos_y = 0
pos1_x = 0
pos1_y = 0

#CONTROLS
cur_vel_x1 = 0
cur_vel_y1 = 0
cur_vel_x2 = 0
cur_vel_y2 = 0
text_map = [
        '0001111112211000',
        '0000111111111000',
        '0000111112111000',
        '0000012211111000',
        '0000112181111000',
        '0000122111111000',
        '0000121111111000',
        '0012121181111000',
        '0001121121111000',
        '0001111111110000',
        '0000000000000000',
        ]

walls = ['3','3','3','3']

def player(a,b,d):
    if d == 'w':
        display.blit(player_texture['4'],( 200 + 1.2*a - 0.8*b, 200 +  1.2*a + 0.8*b))
    if d == 'a':
        display.blit(player_texture['3'],( 200 + 1.2*a - 0.8*b, 200 +  1.2*a + 0.8*b))
    if d == 's':
        display.blit(player_texture['2'],( 200 + 1.2*a - 0.8*b, 200 +  1.2*a + 0.8*b))
    if d == 'd':
        display.blit(player_texture['1'],( 200 + 1.2*a - 0.8*b, 200 +  1.2*a + 0.8*b))


def ground(map_data,a,b,c,d):
    a,b,c,d = (17,16,8,8)
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == '1':
                #pass
                #pass
                # esto es el mapa de texto
                pygame.draw.rect(display,(255,255,255),pygame.Rect(x*10, y * 10, 10, 10), 1)
            #este es el terreno
                display.blit(grass_img, ( 150 + a*x - b*y, 100 + c*x + d*y))
            if tile == '0':
                display.blit(water_img, ( 150 + a*x - b*y, 100 + c*x + d*y))
            if tile == '2':
                display.blit(grass_img, ( 150 + a*x - b*y, 100 + c*x + d*y))
                display.blit(tree_img, ( 150 + a*x - b*y, 60 + c*x + d*y))
            if tile == '8':
                display.blit(grass_img, ( 150 + a*x - b*y, 100 + c*x + d*y))
                for i, fila in enumerate(walls):
                    for j, bloque in enumerate(fila):
                        if bloque == '3':
                            display.blit(wood_img, ( 150 + a*x - b*y + a*i - b*j, 70 + c*i + d*j+ c*x + d*y))


while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cur_vel_y1 += -1
                d = 'w'
            if event.key == pygame.K_a:
                cur_vel_x1 += -1
                d = 'a'
            if event.key == pygame.K_d:
                cur_vel_x1 += 1
                d = 'd'
            if event.key == pygame.K_s:
                cur_vel_y1 += 1
                d = 's'
            if event.key == pygame.K_n:
                pass
            if event.key == pygame.K_i:
                cur_vel_y2 += -1
            if event.key == pygame.K_j:
                cur_vel_x2 += -1
            if event.key == pygame.K_l:
                cur_vel_x2 += 1
            if event.key == pygame.K_k:
                cur_vel_y2 += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                cur_vel_y1 = 0
            if event.key == pygame.K_a:
                cur_vel_x1 = 0
            if event.key == pygame.K_s:
                cur_vel_y1 = 0
            if event.key == pygame.K_d:
                cur_vel_x1 = 0
            if event.key == pygame.K_n:
                pass
            if event.key == pygame.K_i:
                cur_vel_y2 = 0
            if event.key == pygame.K_j:
                cur_vel_x2 = 0
            if event.key == pygame.K_l:
                cur_vel_x2 = 0
            if event.key == pygame.K_k:
                cur_vel_y2 = 0
    display.fill((0,0,0))

    pos_x += cur_vel_x1
    pos_y += cur_vel_y1
    pos1_x += cur_vel_x2
    pos1_y += cur_vel_y2 
    print(pos_x,pos_y,pos1_x,pos1_y)
    ground(text_map,pos_x,pos_y,pos1_x,pos1_y)
    player(pos_x,pos_y,d)
    screen.blit(pygame.transform.scale(display, screen.get_size()),(0,0))
    pygame.display.update()
