class Character:

    def __init__(self, init_pos, char_sprite):
        '''
            init_pos: character's position at the beginning of the game
            char_sprite: the sprite drawn on the character
        '''
        self.init_pos = init_pos
        self.char_sprite = char_sprite
    
    def character_display(self, screen):
        '''
            Function that makes the character appear on screen

            screen: the surface on which the character will be drawn
        '''
        screen.blit(self.char_sprite, (self.init_pos[0], self.init_pos[1]))