import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
    
    @property
    def pos(self):
        return (int(self.x),int( self.y))
    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

#TEXT MAP
TILE =  60

text_map = [
        'WWWWWWWWWW',
        'W........W',
        'W.W.....WW',
        'W.W......W',
        'W.....WW.W',
        'W........W',
        'W.W......W',
        'WWWWWWWWWW'
        ]

#Game Settings
HEIGHT = 480
WIDTH = 600
HALF_HEIGHT = int(HEIGHT / 2)
HALF_WIDTH = int(WIDTH / 2)

#RAY CASTING SETTINGS
FOV = math.pi/3
HALF_FOV = FOV/2
NUM_RAYS = 90
MAX_DEPTH = 300
DELTA_ANGLE = FOV/NUM_RAYS
DIST = NUM_RAYS / (2*math.tan(HALF_FOV))
PROJ_COEFF = 3*DIST*TILE
SCALE = (WIDTH / NUM_RAYS)

#PLAYER SETTINGS
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2
n = 2

#COLORS
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
DARKGRAY = (110,110,110)
BLUE = (0,0,150)
GREEN = (0,200,2)
YELLOW = (220,220,0)

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            
def ray_casting(sc,player_pos,player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth*cos_a
            y = yo + depth*sin_a
            #pygame.draw.line(sc,DARKGRAY,player_pos,(x,y), 2)
            #pygame.draw.line(sc,DARKGRAY,player_pos,(x,y), 2)
            if (x//TILE*TILE,y//TILE*TILE) in world_map:
                depth *= math.cos(player.angle-cur_angle)
                proj_height = PROJ_COEFF//depth
                c = (255//(1+depth**2*0.0001))
                pygame.draw.rect(sc,(c,c,c),(ray*SCALE, HALF_HEIGHT - proj_height//2 ,SCALE,proj_height)) 
                break
        cur_angle += DELTA_ANGLE

pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)
    
    ray_casting(sc,player.pos,player.angle)
##    pygame.draw.circle(sc,GREEN,player.pos,10)
##    pygame.draw.line(sc,GREEN,player.pos,(player.x + WIDTH * math.cos(player.angle),
##                                                                      player.y + WIDTH * math.sin(player.angle)))

##    for x,y in world_map:
##        pygame.draw.rect(sc,DARKGRAY,(x,y,TILE,TILE),1)

    pygame.display.flip()
    clock.tick()
