class Ennemy:
    '''
        Class that defines the ennemy, and his
        position in the labyrinth.

        level_structure: the level as an array
    '''

    def __init__(self, level_structure):
        for line in level_structure:
            for character in line:
                if character == 'E':
                    row_position = line.index(character)
                    line_position = level_structure.index(line)
        self.position = [row_position, line_position]
