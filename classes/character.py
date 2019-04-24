class Character:

    def __init__(self, char_sprite):
        '''
            player_position: character's position at the beginning of the game
            char_sprite: the sprite drawn on the character
        '''
        self.char_sprite = char_sprite

    def char_check_displacement(self, level_structure, line_position, col_position):
        '''
            A level structure given, this function checks
            if the player can move, or not, in any direction.
        
            level_structure: an array containing the level
        '''
        for line in level_structure:
            for tile in line:
                if tile == ' ':
                    return line_position, col_position
        