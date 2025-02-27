from weapons import *

class Archer:
    def __init__(self, char_rase):
        self.rase = char_rase
        if self.rase == 'Эльф':
            self.weapons = [bow, bag]
        if self.rase == 'Дварф':
            self.weapons = [ballist, bolt]


class Warrior:
    def __init__(self, char_rase):
        self.rase = char_rase
        if self.rase == 'Эльф':
            self.weapons = [sword, dagger]
        if self.rase == 'Дварф':
            self.weapons = [axe, shield]