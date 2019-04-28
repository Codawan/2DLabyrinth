import sys

import pygame
from pygame.locals import *

import constants
from constants import *

import classes.labyrinth
from classes import labyrinth as lab

import classes.character
from classes.character import *

import classes.items
from classes.items import Item as item


pygame.init()

# Let's initialize our window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
pygame.display.set_caption(WINDOW_TITLE)
screen.fill(BLACK) # our background is set to black

# Let's draw the labyrinth once here
wall_file = pygame.image.load(WALL_SPRITE)
laby = lab.Labyrinth(LEVEL_FILE)
laby.level_display(screen, wall_file, SQUARED_OFFSET)
pygame.display.flip()

# We will use 'extracted' level data to move our character
level_struct = laby.level_load()

macgyver = pygame.image.load(MACGYVER_SPRITE) 
player = Character()

# initialize player's position
player_pos = player.character_spawn(level_struct)
print(player_pos)
# variable to keep our main loop running:
running = True

# Add our first item: Ether
ether = pygame.image.load(ETHER_SPRITE)
ether = pygame.transform.scale(ether, (TILE_SIZE, TILE_SIZE))
ether_item = item(level_struct)
ether_position = ether_item.item_positioning()
print("ether:",ether_position[1])

# Add our second item: Syringe
syringe = pygame.image.load(SYRINGE_SPRITE)
syringe = pygame.transform.scale(syringe, (TILE_SIZE, TILE_SIZE))
syringe_item = item(level_struct)
syringe_position = syringe_item.item_positioning()
print("syringe:",syringe_position[1])

# Add our third item: Needle
needle = pygame.image.load(NEEDLE_SPRITE)
needle = pygame.transform.scale(needle, (TILE_SIZE, TILE_SIZE))
needle_item = item(level_struct)
needle_position = needle_item.item_positioning()
print("needle:",needle_position[1])

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
    screen.blit(ether, (ether_position[1][0]*SQUARED_OFFSET, ether_position[1][1]*SQUARED_OFFSET))
    screen.blit(syringe, (syringe_position[1][0]*SQUARED_OFFSET, syringe_position[1][1]*SQUARED_OFFSET))
    screen.blit(needle, (needle_position[1][0]*SQUARED_OFFSET, needle_position[1][1]*SQUARED_OFFSET))  
    screen.blit(macgyver, (player_pos[1]* SQUARED_OFFSET, player_pos[0]* SQUARED_OFFSET))

    pygame.display.flip()
        