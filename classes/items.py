import random
from random import randint

class Item:
    '''
        Class that defines an item the player will have to find
        to escape the labyrinth

        level_structure: a level structure given
        sprite: picture of the item
    '''
    def __init__(self, level_structure):
        self.level_structure = level_structure

    def item_positioning(self):
        '''
            Method that put the item in the structure in on an empty
            place, and draw it
        '''
        # Let's count the number of places available
        empty_places = 0
        for line in self.level_structure:
            for tile in line:
                if tile == ' ':
                    empty_places += 1
        # Let's assign a position to our item
        # Our item will be assigned a random number between 0 and the total number of empty places:
        item_random_spot = randint(0, empty_places)     
        # Let's stock our item coordinates in a list:  
        item_position = []
        x = 0
        for i in range(0, len(self.level_structure)):
            for j in range(0, len(self.level_structure[0])):
                if self.level_structure[i][j] == ' ':
                    if x != item_random_spot:
                        x+=1
                    else: # Let's replace - in our level structure - an empty place with the item
                        self.level_structure[i] = self.level_structure[i][0:j] + 'I' + self.level_structure[i][j+1:]
                        # Let's get our item position
                        item_position.append(j)
                        item_position.append(i)
                                            
                        x+=1
        return [self.level_structure, item_position]




