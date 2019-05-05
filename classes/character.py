class Character:

    def __init__(self, level_structure):

        # Let's get player coordinates at the begining of the game
        spawn_coordinates = []
        for line in level_structure:
            for tile in line:
                if tile == 'S':
                    spawn_coordinates = [level_structure.index(line), line.index(tile)]        
        self.line_pos = spawn_coordinates[0]
        self.col_pos = spawn_coordinates[1]
        # Let's set the amount of items the player get
        self.items_count = 0
        


    def char_displacement(self, displacement, level_structure):
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
       
        if displacement == 'up' and level_structure[self.line_pos - 1][self.col_pos] != 'W':
            self.line_pos -= 1
        elif displacement == 'down' and level_structure[self.line_pos + 1][self.col_pos] != 'W':
            self.line_pos += 1
        elif displacement == 'left' and level_structure[self.line_pos][self.col_pos - 1] != 'W':
            self.col_pos -= 1
        elif displacement == 'right' and level_structure[self.line_pos][self.col_pos +1] != 'W':
            self.col_pos += 1
        
        return [self.line_pos, self.col_pos]