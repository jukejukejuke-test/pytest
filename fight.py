from char_creator import character
from monsters import *


def monster_fight(character, monster):
    print(f'##########Вы встретили монстра:##########')
    monster.show_monster_info()
    print(f'#########################################')
    while character.hp > 0 or monster.hp > 0:
        action = input('Введите ваше действие ["1 - атака", "2 - бегство"]: ')
        print(f'#########################################')
        if action == '1':
            monster.hp -= character.damage
            character.hp -= monster.damage
            if monster.hp > 0:
                print(f'Ваше здоровье: {character.hp}, здоровье монстра: {monster.hp}')
                print(f'#########################################')
            else:
                print(f'Ваше здоровье: {character.hp}')
        if action == '2':
            luck = random.randint(1, 7)
            if luck > 4:
                print('Вы успешно сбежали!')
                return
            else:
                if character.exp - monster.exp > 0:
                    character.exp -= monster.exp
                else:
                    character.exp = 0
                character.hp = character.max_hp
                print(f'Вы повержены и потеряли {monster.exp} опыта.')
                return
        if monster.hp <= 0:
            character.exp += monster.exp
            character.hp = character.max_hp
            if character.exp >= character.exp_to_next_lvl:
                character.level_up()
                print(f'Персонаж повышен до {character.lvl} уровня!')
            if character.exp > 0:
                print(f'Вы победили! Получено {monster.exp} опыта.\nТекущий опыт: {character.exp}.')
            else:
                print(f'Вы победили! Получено {monster.exp} опыта.')
            return
while True:
    monster_fight(character, Monster(name=random.choice(monster_names), hp=random.randint(1, 200), damage=random.randint(5, 30)))