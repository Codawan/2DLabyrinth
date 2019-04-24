class Labyrinth:
    
    def __init__(self, level_file):
        self.level_file = level_file

    def level_load(self):
        '''
            Loads a level from a .txt file,
            remove space between lines and create
            a new list
        '''
        level_structure = []
        with open(self.level_file, 'r') as file:
            labyrinth = file.readlines()
            for n_line in range(0, len(labyrinth)):
                # let's remove spaces at the end of each line
                labyrinth[n_line] = labyrinth[n_line].strip()
            for line in labyrinth:
                level_structure.append(line)
        return level_structure

    def level_display(self, screen, wall_sprite, offset):
        '''
            Uses pygame to display the level as graphics

            screen = the display screen
            wall_sprite = pygame surface made of image file
            offset = offset defined by the size of each tile on screen
        '''
        # init sprite coordinates, on top left of the screen
        sprite_x = 0
        sprite_y = 0
        for line in self.level_load():
            for tile in line:
                if tile == 'W':
                    screen.blit(wall_sprite, (sprite_x, sprite_y))
                    sprite_x += offset
                else:
                    sprite_x += offset
            sprite_y += offset
            sprite_x = 0