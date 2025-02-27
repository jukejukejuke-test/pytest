import random

monster_names = ["Газебо", "Амазонка", "Чумная крыса"]

class Monster:
    """"Создаёт рандомного монстра"""
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        if self.hp in range(0, 30):
            self.exp = 100
        if self.hp in range(30, 90):
            self.exp = 300
        if self.hp > 90:
            self.exp = 1000

    def show_monster_info(self):
        print(
            f'Имя: {self.name}\nЗдоровье: {self.hp}\nУрон: {self.damage}'
        )


random_monster = Monster(name=random.choice(monster_names), hp=random.randint(1, 200), damage=random.randint(5, 30))