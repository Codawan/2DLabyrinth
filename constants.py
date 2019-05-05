# Game attributes
FPS = 30

# Screen attributes
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
TILE_NUMBER = 15
SQUARED_OFFSET = SCREEN_WIDTH / TILE_NUMBER
TILE_SIZE = int(SCREEN_WIDTH / TILE_NUMBER)
WINDOW_TITLE = 'MacGyver and the mighty 2D Labyrinth'
SCREEN_CENTER = (SCREEN_WIDTH * .5 , SCREEN_HEIGHT * .5)

# Level structure
LEVEL_FILE = 'assets/level.txt'
WALL_SPRITE = 'assets/wall.png'

# Player character attributes
SPAWN = [2,1]
MACGYVER_SPRITE = 'assets/macgyver.png'

# Ennemy attributes
MURDOC_SPRITE = 'assets/murdoc.png'

# Colors   R    G    B
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# Item sprites
ETHER_SPRITE = 'assets/ether.png'
SYRINGE_SPRITE = 'assets/syringe.png'
NEEDLE_SPRITE = 'assets/needle.png'

# Fonts
GAME_FONT = 'assets/PressStart2P-Regular.ttf'

# Text
WIN_TEXT = 'You win!'
LOSE_TEXT = 'You lose!'