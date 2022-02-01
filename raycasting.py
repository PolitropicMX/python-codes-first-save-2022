import pygame
import math
###########################################################################
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
        ray_casting(self.sc,player_pos,player_angle,self.texture)

    def fps(self,clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps,0,RED)
        self.sc.blit(render,(WIDTH-65,5))

    def mini_map(self,player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE,player.y // MAP_SCALE
        pygame.draw.circle(self.sc_map,RED,(int(map_x),int(map_y)),5)
        pygame.draw.line(self.sc_map,YELLOW,(map_x,map_y),(int(map_x+WIDTH*math.cos(player.angle)),int(map_y+WIDTH*math.sin(player.angle))))
        for x,y in mini_map:
            pygame.draw.rect(self.sc_map,DARKGRAY,(x,y,MAP_TILE,MAP_TILE))
        self.sc.blit(self.sc_map,(MAP_POS))
#############################################################################    
class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    
    @property
    def pos(self):
        return (self.x, self.y)
    
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
############################################################################
        

#TEXT MAP
TILE =  60

text_map = [
        'WWWWWWWWWW',
        'W........W',
        'W.W.....WW',
        'W.W.......W',
        'W....WW..W',
        'W........W',
        'WWWWWWWWWW'
        ]

#Game Settings
HEIGHT = 400
WIDTH = 600
HALF_HEIGHT = int(HEIGHT / 2)
HALF_WIDTH = int(WIDTH / 2)
FPS = 60

#TEXTURE SETTINGS
TEXTURE_WIDTH = 600
TEXTURE_HEIGHT = 600
TEXTURE_SCALE = TEXTURE_HEIGHT // TILE

#MINI MAP SETTINGS
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT//MAP_SCALE)

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))

#PLAYER SETTINGS
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2
 
#RAY CASTING SETTINGS
FOV = math.pi/3
HALF_FOV = FOV/2
NUM_RAYS = 70
MAX_DEPTH = 300
DELTA_ANGLE = FOV/NUM_RAYS
DIST = NUM_RAYS / (2*math.tan(HALF_FOV))
PROJ_COEFF = 3*DIST*TILE
SCALE = 2*WIDTH // NUM_RAYS

#COLORS
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
DARKGRAY = (110,110,110)
BLUE = (0,0,150)
GREEN = (0,200,2)
YELLOW = (220,220,0)

pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
sc_map = pygame.Surface((WIDTH//MAP_SCALE,HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc,sc_map)

def mapping(a,b):
    return (a//TILE)*TILE, (b//TILE)*TILE

##def ray_casting(sc,player_pos,player_angle):
##    cur_angle = player_angle - HALF_FOV
##    xo, yo = player_pos
##    for ray in range(NUM_RAYS):
##        sin_a = math.sin(cur_angle)
##        cos_a = math.cos(cur_angle)
##        for depth in range(MAX_DEPTH):
##            x = xo + depth*cos_a
##            y = yo + depth*sin_a
##            #pygame.draw.line(sc,DARKGRAY,player_pos,(x,y), 2)
##            if (x//TILE*TILE,y//TILE*TILE) in world_map:
##                

def ray_casting(sc,player_pos,player_angle, texture):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        #verticals
        x, dx = (xm + TILE,1) if cos_a >= 0 else (xm, -1)
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
        depth, offset = (depth_v,yv) if depth_v < depth_h else (depth_h, xh)
        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth,0.00001)
        proj_height = min(int(PROJ_COEFF / depth),2*HEIGHT)
##        c = 255/(1+depth*depth*0.00002)
##        color = (c,c//2,c)
##        pygame.draw.rect(sc,color,(ray*SCALE,HALF_HEIGHT-proj_height//2,SCALE,proj_height))
        wall_column = texture.subsurface(offset * TEXTURE_SCALE,0,TEXTURE_SCALE, TEXTURE_HEIGHT )
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column,(ray*SCALE, HALF_HEIGHT - proj_height//2,SCALE,proj_height))
        cur_angle += DELTA_ANGLE

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
    #ray_casting(sc,player.pos,player.angle)
    

        
    pygame.display.flip()
    clock.tick()
