from mmo_constants import *
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
        self.info["Класс"] = self.prof
gender = None
rase = None
prof = None

while True:
    x = input('Введите пол - "Мужчина"/"Женщина": ')
    if x in VALID_GENDERS:
        gender = x
        break
    else:
        print('Введите существующий пол - "Мужчина"/"Женщина": ')

while True:
    x = input('Введите расу - "Эльф"/"Дварф": ')
    if x in VALID_RASES:
        rase = x
        break
    else:
        print('Введите существующую расу - "Эльф"/"Дварф": ')

while True:
    x = input('Введите класс - "Лучник"/"Воин": ')
    if x in VALID_PROFS:
        prof = x
        break
    else:
        print('Введите существующий класс - "Воин"/"Лучник": ')

character = CharCreate(gender, rase, prof)

print(character.info)