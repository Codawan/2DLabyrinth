import sys

import pygame
from pygame.locals import RESIZABLE, QUIT, \
     KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, \
     K_ESCAPE

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, \
    WINDOW_TITLE, BLACK, WALL_SPRITE, LEVEL_FILE, \
    SQUARED_OFFSET, MACGYVER_SPRITE, GAME_FONT, WIN_TEXT, \
    WHITE, SCREEN_CENTER, LOSE_TEXT, RED, ETHER_SPRITE, \
    TILE_SIZE, SYRINGE_SPRITE, NEEDLE_SPRITE, MURDOC_SPRITE, \
    FPS

from classes import labyrinth as lab
from classes import character as char
from classes import items as item
from classes import ennemy as guardian


def main():
    '''
        Main function of the game
    '''

    pygame.init()

    fpsClock = pygame.time.Clock()

    # Let's initialize our window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
    pygame.display.set_caption(WINDOW_TITLE)
    screen.fill(BLACK)  # our background is set to black

    # Let's draw the labyrinth once here
    wall_file = pygame.image.load(WALL_SPRITE).convert()
    laby = lab.Labyrinth(LEVEL_FILE)
    laby.level_display(screen, wall_file, SQUARED_OFFSET)
    pygame.display.flip()

    # We will use 'extracted' level data to move our character
    level_struct = laby.level_load()

    # let's create player's object, and initialize its position
    macgyver = pygame.image.load(MACGYVER_SPRITE)
    macgyver = pygame.transform.scale(macgyver, (24, 30))
    player = char.Character(level_struct)
    player_pos = [player.col_pos, player.line_pos]

    # variable to keep our main game loop running:
    main_game = True

    # variables that define the end of the game:
    win = False
    lose = False
    # pygame font object to draw end game text:
    game_font = pygame.font.Font(GAME_FONT, 30)
    text_win_surface = game_font.render(WIN_TEXT, True, WHITE)
    text_win_rect = text_win_surface.get_rect()
    text_win_rect.center = SCREEN_CENTER
    text_lose_surface = game_font.render(LOSE_TEXT, True, RED)
    text_lose_rect = text_win_surface.get_rect()
    text_lose_rect.center = SCREEN_CENTER

    # Add our first item: Ether
    ether = pygame.image.load(ETHER_SPRITE).convert()
    ether = pygame.transform.scale(ether, (TILE_SIZE, TILE_SIZE))
    ether_item = item.Item(level_struct, ether)

    # Add our second item: Syringe
    syringe = pygame.image.load(SYRINGE_SPRITE).convert_alpha()
    syringe = pygame.transform.scale(syringe, (TILE_SIZE, TILE_SIZE))
    syringe_item = item.Item(level_struct, syringe)

    # Add our third item: Needle
    needle = pygame.image.load(NEEDLE_SPRITE).convert()
    needle = pygame.transform.scale(needle, (TILE_SIZE, TILE_SIZE))
    needle_item = item.Item(level_struct, needle)

    item_list = [ether_item, syringe_item, needle_item]
    item_needed = len(item_list)
    item_count = 0
    all_items_taken = False

    # Item counter display
    counter_font = pygame.font.Font(GAME_FONT, 12)
    text_counter_surface = counter_font.render('Items taken: ' +
                                               str(item_count),
                                               True, WHITE)
    text_counter_rect = text_counter_surface.get_rect()
    text_counter_rect.center = (SCREEN_WIDTH - 100, 15)

    # Add the ennemy
    murdoc_sprite = pygame.image.load(MURDOC_SPRITE)
    murdoc_sprite = pygame.transform.scale(murdoc_sprite, (27, 30))
    murdoc = guardian.Ennemy(level_struct)

    # Our main loop:
    while main_game:

        # let's fill the background with black color
        screen.fill(BLACK)

        if win:
            screen.blit(text_win_surface, text_win_rect)
        elif lose:
            screen.blit(text_lose_surface, text_lose_rect)
        else:

            for event in pygame.event.get():

                # Quit the game and close the window
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

                # Check for player's input during the game
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        player_pos = player.char_displacement('up',
                                                              level_struct)
                    if event.key == K_DOWN:
                        player_pos = player.char_displacement('down',
                                                              level_struct)
                    if event.key == K_LEFT:
                        player_pos = player.char_displacement('left',
                                                              level_struct)
                    if event.key == K_RIGHT:
                        player_pos = player.char_displacement('right',
                                                              level_struct)
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)

            for i in item_list:
                if i.check_if_taken(player_pos):
                    item_count += 1
                    item_list.remove(i)
                else:
                    screen.blit(i.sprite, (i.item_position[0]*SQUARED_OFFSET,
                                           i.item_position[1]*SQUARED_OFFSET))

            if item_count == item_needed:
                all_items_taken = True

            # Won or game over when being next to the ennemy
            if player_pos == [murdoc.position[0]-1, murdoc.position[1]]:
                if all_items_taken:
                    win = True
                else:
                    lose = True

            laby.level_display(screen, wall_file, SQUARED_OFFSET)
            screen.blit(murdoc_sprite, (murdoc.position[0] * SQUARED_OFFSET,
                                        murdoc.position[1] * SQUARED_OFFSET))
            screen.blit(macgyver, (player_pos[0] * SQUARED_OFFSET,
                                   player_pos[1] * SQUARED_OFFSET))

            text_counter_surface = counter_font.render('Items taken: ' +
                                                       str(item_count),
                                                       True, WHITE)
            screen.blit(text_counter_surface, text_counter_rect)

        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__ == "__main__":

    main()
