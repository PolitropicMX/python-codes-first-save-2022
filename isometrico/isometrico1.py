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
player_img = pygame.image.load('player.png').convert()
grass_img.set_colorkey((0,0,0))
water_img.set_colorkey((0,0,0))
player_img.set_colorkey((0,0,0))
clock = pygame.time.Clock()
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
        '000111110011000',
        '000111111111000',
        '000000110000000',
        '000001111100000',
        '000011111111000',
        '000111111111000',
        '000111112111000',
        '000111111111000',
        '000111111111000',
        '000111111110000',
        '000000000000000',
        ]

def player(a,b,c,d):
    pass


def draw(map_data,a,b,c,d):
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
                display.blit(player_img, ( 150 + a*x - b*y, 100 + c*x + d*y))

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cur_vel_y1 += -1
            if event.key == pygame.K_a:
                cur_vel_x1 += -1
            if event.key == pygame.K_d:
                cur_vel_x1 += 1
            if event.key == pygame.K_s:
                cur_vel_y1 += 1
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
    draw(text_map,pos_x,pos_y,pos1_x,pos1_y)
    screen.blit(pygame.transform.scale(display, screen.get_size()),(0,0))
    pygame.display.update()
