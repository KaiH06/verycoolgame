import pygame as pg

pg.init()

#defining colors for objects in scene using RGB parameters
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 89, 0)
YELLOW = (255, 204, 0)

TITLE = "Very Cool Game"
# Set the screen size [width, height]
WIDTH = 600
HEIGHT = 500

# character sizes
P_SIZE = 30
E_SIZE = 20
M_HEIGHT = 10
M_WIDTH = 5

ENEMY_COUNT = 13
LIVES = 3
#frame rate
FPS = 60   #frames per second

# display and timing
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
CLOCK = pg.time.Clock()

# fonts
pg.font.init()
LRG_FONT = pg.font.SysFont("Impact", 60, False, False)
MED_FONT = pg.font.SysFont("Impact", 40, False, False)
SML_FONT = pg.font.SysFont("Impact", 20, False, False)