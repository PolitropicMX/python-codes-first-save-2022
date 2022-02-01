import pygame
import math

class Drawing:
    def __init__(self,sc,sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial',36,bold=True)
        self.texture = pygame.image.load('wall_image.jpg').convert()

    def background(self):
        pygame.draw.rect(self.sc,BLUE,(0,0,WIDTH,HALF_HEIGHT))
        pygame.draw.rect(self.sc,DARKGRAY,(0,HALF_HEIGHT,WIDTH,HALF_HEIGHT))

    def world(self,player_pos,player_angle):
        ray_casting(self.sc,player_pos,player_angle)

    def fps(self,clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps,0,RED)
        self.sc.blit(render,(WIDTH-65,5))

    def mini_map(self,player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE,player.y // MAP_SCALE
        pygame.draw.circle(self.sc_map,RED,(int(map_x),int(map_y)),5)
        
        for x,y in mini_map:
            pygame.draw.rect(self.sc_map,DARKGRAY,(x,y,MAP_TILE,MAP_TILE))
        pygame.draw.line(self.sc_map,YELLOW,(map_x,map_y),(int(map_x+WIDTH*math.cos(player.angle)),int(map_y+WIDTH*math.sin(player.angle))))
        self.sc.blit(self.sc_map,(MAP_POS))
###########################################################################

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

#MINI MAP SETTINGS
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT//MAP_SCALE)

#RAY CASTING SETTINGS
FOV = math.pi/3
HALF_FOV = FOV/2
NUM_RAYS = 80
MAX_DEPTH = 300
DELTA_ANGLE = FOV/NUM_RAYS
DIST = NUM_RAYS / (2*math.tan(HALF_FOV))
PROJ_COEFF = DIST*TILE
SCALE = WIDTH // NUM_RAYS

#PLAYER SETTINGS
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

#COLORS
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
DARKGRAY = (110,110,110)
BLUE = (0,0,150)
GREEN = (0,200,2)
YELLOW = (220,220,0)

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            
##def ray_casting(sc,player_pos,player_angle):
##    cur_angle = player_angle - HALF_FOV
##    xo, yo = player_pos
##    for ray in range(NUM_RAYS):
##        sin_a = math.sin(cur_angle)
##        cos_a = math.cos(cur_angle)
##        for depth in range(MAX_DEPTH):
##            x = xo + depth*cos_a
##            y = yo + depth*sin_a
##            if (x//TILE*TILE,y//TILE*TILE) in world_map:
##                depth *= math.cos(player.angle-cur_angle)
##                proj_height = PROJ_COEFF/depth
##                c = (255/(1+depth**2*0.0001))
##                pygame.draw.rect(sc,(c,c//2,c//3),(ray*SCALE, HALF_HEIGHT - proj_height//2, SCALE,proj_height)) 
##                break
##        cur_angle += DELTA_ANGLE

def mapping(a,b):
    return (a//TILE)*TILE, (b//TILE)*TILE

def ray_casting(sc,player_pos,player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
    
        #verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0,WIDTH,TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v *sin_a
            if mapping(x+dx, yv) in world_map:
                break
            x += dx*TILE

        # horizontals
        y, dy = (ym + TILE,1) if sin_a >= 0 else(ym,-1)
        for i in range(0,HEIGHT,TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h*cos_a
            if mapping(xh, y+dy) in world_map:
                break
            y += dy*TILE

        #projection
        depth = (depth_v) if depth_v < depth_h else (depth_h)
        depth *= math.cos(player_angle - cur_angle)
        proj_height = (PROJ_COEFF / depth)
        c = 255/(1+depth*depth*0.00002)
        pygame.draw.rect(sc,(c,c,c),(ray*SCALE,HALF_HEIGHT-proj_height//2,SCALE,proj_height))
        cur_angle += DELTA_ANGLE
            
pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
sc_map = pygame.Surface((WIDTH//MAP_SCALE,HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc,sc_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos,player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()
