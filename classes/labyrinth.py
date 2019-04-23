class Labyrinth:
    

    def level_loading(file_name):
        '''
            Loads a level from a .txt file,
            extract each line and remove space at
            their end.
        '''
        with open(file_name, 'r') as file:
            labyrinth = file.readlines()
            i = 0
            for i in range(0, len(labyrinth)):
                # allows to remove space between every lines
                labyrinth[i] = labyrinth[i].strip()

