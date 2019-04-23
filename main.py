import sys

import pygame
from pygame.locals import *

import constants
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
pygame.display.set_caption(WINDOW_TITLE)

# draw the labyrinth once here

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
                pass
            if event.key == K_DOWN:
                pass
            if event.key == K_LEFT:
                pass
            if event.key == K_RIGHT:
                pass
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)