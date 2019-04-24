class Character:

    def __init__(self, char_sprite):
        '''
            player_position: character's position at the beginning of the game
            char_sprite: the sprite drawn on the character
        '''
        self.char_sprite = char_sprite

    def char_check_displacement(self, level_structure, displacement, line_pos, col_pos):
        '''
            A level structure given, this function checks
            if the player can move, or not, in any direction.
        
            level_structure: an array containing the level
        '''
        for line in level_structure:
            for tile in line:
                if displacement == 'up' and level_structure[line_pos-1][col_pos] != 'W':
                    print('good')

                elif displacement == 'down':
                    print('down')
                elif displacement == 'left':
                    print('left')
                elif displacement == 'right':
                    print('right')

    def char_displacement(self, displacement, init_pos):
        
        line_pos = init_pos[0]
        col_pos = init_pos[1]
        
        if displacement == 'up':
            line_pos -= 1
        elif displacement == 'down':
            line_pos += 1
        elif displacement == 'left':
            col_pos -= 1
        elif displacement == 'right':
            col_pos += 1
        
        return [line_pos, col_pos]