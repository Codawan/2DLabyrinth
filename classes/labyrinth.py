class Labyrinth:
    
    def __init__(self, level_file):
        self.level_file = level_file

    def level_display(self, screen, wall_sprite, offset):
        '''
            Loads a level from a .txt file,
            extract each line and remove space at
            their end.
        '''

        line_pos = []
        col_pos = []
        with open(self.level_file, 'r') as file:
            labyrinth = file.readlines()
            n_line = 0 # line number
            for n_line in range(0, len(labyrinth)):
                # allows to remove space between every lines
                labyrinth[n_line] = labyrinth[n_line].strip()
                line_pos.append(labyrinth[n_line])
            print(line_pos)
              
                
                
                
                '''for tile in labyrinth[n_line]:
                    if tile == 'W':
                        screen.blit(wall_sprite, (sprite_x, sprite_y))
                        sprite_x += offset
                    else:
                        sprite_x += offset
                sprite_y += offset
                sprite_x = 0'''

                
                
                # if labyrinth[i], print a given sprite, with a given offset
