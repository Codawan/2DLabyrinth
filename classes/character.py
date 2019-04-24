class Character:

    def __init__(self, char_sprite):
        '''
            player_position: character's position at the beginning of the game
            char_sprite: the sprite drawn on the character
        '''
        self.char_sprite = char_sprite
    
    def character_display(self, screen, line_position, col_position):
        '''
            Function that makes the character appear on screen

            screen: the surface on which the character will be drawn
        '''
        screen.blit(self.char_sprite, (line_position, col_position))

    def char_check_displacement(self, level_structure, line_position, col_position):
        '''
            A level structure given, this function checks
            if the player can move, or not, in any direction.
        
            level_structure: an array containing the level
        '''
        for line in level_structure:
            for tile in line:
                # Check if the player is outside the level boundaries.
                # if line_position < 0 or col_position < 0 or line_position > (len(level_structure) -1) \
                #     or col_position > (len(level_structure[0])-1):
                #     print('Outside the boundaries')
                #     print(line_position, col_position)
                #     return None
                # Check if the player encounters a wall or not
                if tile != ' ':
                    print('Obstacle encountered')
                    return None
                # else:
                #     print('Player can move')
                #     print(line_position, col_position)
                #     return [line_position, col_position]
        