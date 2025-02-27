from base_player import Player

class Elf(Player):
    """Инициализирует конкретно эльфа"""
    def __init__(self, gender):
        super().__init__(gender)
        self.char_rase = 'Эльф'
        self.agility = 22
        self.strength = 8
        self.intelligence = 10
        self.hp = 200
        self.update_info()

class Dwarf(Player):
    """Инициализирует конкретно дварфа"""
    def __init__(self, gender):
        super().__init__(gender)
        self.char_rase = 'Дварф'
        self.agility = 6
        self.strength = 25
        self.intelligence = 8
        self.hp = 300
        self.update_info()