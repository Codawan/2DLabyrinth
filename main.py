import sys

import pygame
from pygame.locals import *

import constants
from constants import *

import classes.labyrinth
from classes.labyrinth import *

import classes.character
from classes.character import *


pygame.init()

# Let's initialize our window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
pygame.display.set_caption(WINDOW_TITLE)
screen.fill(BLACK) # our background is set to black

# Let's draw the labyrinth once here
wall_file = pygame.image.load(WALL_SPRITE)
laby = Labyrinth(LEVEL_FILE)
laby.level_display(screen, wall_file, SQUARED_OFFSET)
pygame.display.flip()

# We will use 'extracted' level data to move our character
level_struct = laby.level_load()

macgyver = pygame.image.load(MACGYVER_SPRITE) 
player = Character(macgyver)

# initialize player's position
player_pos = SPAWN
print(player_pos)
# variable to keep our main loop running:
running = True

# Our main loop:
while running:

    for event in pygame.event.get():

        # Quit the game and close the window
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        # Check for player's input during the game
        if event.type == KEYDOWN:
            if event.key == K_UP:
                player_pos = player.char_displacement('up', player_pos, level_struct)
            if event.key == K_DOWN:
                player_pos = player.char_displacement('down', player_pos, level_struct)
            if event.key == K_LEFT:
                player_pos = player.char_displacement('left', player_pos, level_struct)
            if event.key == K_RIGHT:
                player_pos = player.char_displacement('right', player_pos, level_struct)
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            print(player_pos)

    # Let's update each graphical element   
    screen.fill(BLACK)
    laby.level_display(screen, wall_file, SQUARED_OFFSET)
    screen.blit(macgyver, (player_pos[1]* SQUARED_OFFSET, player_pos[0]* SQUARED_OFFSET))

    pygame.display.flip()
        