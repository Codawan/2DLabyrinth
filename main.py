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
from classes import items as item

import classes.ennemy
from classes import ennemy as guardian


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

# let's create player's object, and initialize its position
macgyver = pygame.image.load(MACGYVER_SPRITE) 
player = Character(level_struct)
player_pos = [player.line_pos, player.col_pos]

# variable to keep our main loop running:
running = True

# Add our first item: Ether
ether = pygame.image.load(ETHER_SPRITE)
ether = pygame.transform.scale(ether, (TILE_SIZE, TILE_SIZE))
ether_item = item.Item(level_struct)
ether_position = ether_item.item_positioning()
ether_taken = False

# Add our second item: Syringe
syringe = pygame.image.load(SYRINGE_SPRITE)
syringe = pygame.transform.scale(syringe, (TILE_SIZE, TILE_SIZE))
syringe_item = item.Item(level_struct)
syringe_position = syringe_item.item_positioning()
syringe_taken = False

# Add our third item: Needle
needle = pygame.image.load(NEEDLE_SPRITE)
needle = pygame.transform.scale(needle, (TILE_SIZE, TILE_SIZE))
needle_item = item.Item(level_struct)
needle_position = needle_item.item_positioning()
needle_taken = False

all_items_taken = False

# Add the ennemy
murdoc_sprite = pygame.image.load(MURDOC_SPRITE)
murdoc = guardian.Ennemy()
murdoc_position = murdoc.ennemy_position(level_struct)
print(murdoc_position)

# items counter
item_count = 0

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
                player_pos = player.char_displacement('up', level_struct)
            if event.key == K_DOWN:
                player_pos = player.char_displacement('down', level_struct)
            if event.key == K_LEFT:
                player_pos = player.char_displacement('left', level_struct)
            if event.key == K_RIGHT:
                player_pos = player.char_displacement('right', level_struct)
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)

    if player_pos[0] == ether_position[1][1] and player_pos[1] == ether_position[1][0]:
        ether_taken = True
        
    if player_pos[0] == needle_position[1][1] and player_pos[1] == needle_position[1][0]:
        needle_taken = True

    if player_pos[0] == syringe_position[1][1] and player_pos[1] == syringe_position[1][0]:
        syringe_taken = True

    if ether_taken and needle_taken and syringe_taken:
        all_items_taken = True


    # Won or game over
    if player_pos[0] == murdoc_position[1] and player_pos[1] == murdoc_position[0]:
        if all_items_taken == True:
            print('You win')
        else:
            print('You lose')

    # Let's update each graphical element   
    screen.fill(BLACK)
    laby.level_display(screen, wall_file, SQUARED_OFFSET)
    
    if ether_taken == False:
        screen.blit(ether, (ether_position[1][0]*SQUARED_OFFSET, ether_position[1][1]*SQUARED_OFFSET))
    if syringe_taken == False:
        screen.blit(syringe, (syringe_position[1][0]*SQUARED_OFFSET, syringe_position[1][1]*SQUARED_OFFSET))
    if needle_taken == False:
        screen.blit(needle, (needle_position[1][0]*SQUARED_OFFSET, needle_position[1][1]*SQUARED_OFFSET))
    screen.blit(murdoc_sprite, (murdoc_position[0]*SQUARED_OFFSET, murdoc_position[1]*SQUARED_OFFSET))  
    screen.blit(macgyver, (player_pos[1]* SQUARED_OFFSET, player_pos[0]* SQUARED_OFFSET))

    pygame.display.flip()
        