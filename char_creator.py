from rases import Elf, Dwarf
from profs import Archer, Warrior

class CharCreate(Elf, Dwarf, Archer, Warrior):
    """Создаёт игрового персонажа"""
    def __init__(self, gender, char_rase, prof):
        super().__init__(gender)
        self.char_rase = char_rase
        self.prof = prof

        if self.char_rase == 'Дварф':
            Dwarf.__init__(self, gender)
        if self.char_rase == 'Эльф':
            Elf.__init__(self, gender)

        if self.prof == 'Лучник':
            Archer.__init__(self, char_rase)
        if self.prof == 'Воин':
            Warrior.__init__(self, char_rase)
        self.damage = self.weapons[0]["damage"] + self.weapons[1]["damage"]
        self.weapon_names = self.weapons[0]["name"], self.weapons[1]["name"],
        self.update_info()
        self.max_hp = self.hp

character = CharCreate(input('Введите пол - "Мужчина"/"Женщина": '), input('Введите расу - "Эльф"/"Дварф": '), input('Введите класс - "Лучник"/"Воин": '))

print(character.info)