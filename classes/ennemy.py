class Ennemy:
    '''
        We define the ennemy position

        level_structure: the level as an array
    '''
    def ennemy_position(self, level_structure):
        for line in level_structure:
            for character in line:
                if character == 'E':
                    row_position = line.index(character)
                    line_position = level_structure.index(line)
        return [row_position, line_position]