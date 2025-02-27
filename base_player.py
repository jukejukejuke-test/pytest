class Player:
    """Инициализируем базового игрока"""
    def __init__(self, gender):
        self.info = None
        self.lvl = 1
        self.exp = 0
        self.exp_to_next_lvl = 500
        self.gender = gender
        self.hp = None
        self.agility = None
        self.strength = None
        self.intelligence = None
        self.char_rase = None
        self.weapons = []
        self.damage = 0
        self.weapon_names = None

    """Обновляет объект с информацией о персонаже"""
    def update_info(self):
        self.info = {
            "Уровень": self.lvl,
            "Пол": self.gender,
            "Раса": self.char_rase,
            "Здоровье": self.hp,
            "Сила": self.strength,
            "Ловкость": self.agility,
            "Интеллект": self.intelligence,
            "Оружие": self.weapon_names,
            "Урон": self.damage
        }

    """Возвращает объект с инфо о персонаже"""
    def description(self):
        return self.info

    """Поднимает уровень персонажа"""
    def level_up(self):
        self.lvl += 1
        self.exp = 0
        self.exp_to_next_lvl *= 1.2

        if self.char_rase == 'Эльф':
            self.agility += 3
            self.intelligence += 2
            self.strength += 1
            self.damage += 6
            self.max_hp += 20
        if self.char_rase == 'Дварф':
            self.agility += 2
            self.intelligence += 1
            self.strength += 3
            self.damage += 5
            self.max_hp += 40
#
        self.hp = self.max_hp