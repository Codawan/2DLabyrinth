class Character:

    def __init__(self, char_sprite):
        '''
            player_position: character's position at the beginning of the game
            char_sprite: the sprite drawn on the character
        '''
        self.char_sprite = char_sprite

    def char_displacement(self, displacement, init_pos, level_structure):
        '''
            We check player input and detect if a movement is allowed or not
            (is there a Wall 'W' on the way?)

            For example, if the player presses K_UP, the main scripts returns
            'up' as an argument to this function. If the character on the same column
            but on the line on top is not a wall (written 'W'), the movement is allowed.
            Then the new position is return.

            displacement: the input returned by a Keydown event in the main script
            init_pos: player's initial position in the labyrinth
            level_structure: an array that represents the level structure
        '''

        line_pos = init_pos[0]
        col_pos = init_pos[1]
        
        if displacement == 'up' and level_structure[line_pos - 1][col_pos] != 'W':
            line_pos -= 1
        elif displacement == 'down' and level_structure[line_pos + 1][col_pos] != 'W':
            line_pos += 1
        elif displacement == 'left' and level_structure[line_pos][col_pos - 1] != 'W':
            col_pos -= 1
        elif displacement == 'right' and level_structure[line_pos][col_pos +1] != 'W':
            col_pos += 1
        
        return [line_pos, col_pos]