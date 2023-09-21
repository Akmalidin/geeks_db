import random

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage
    # @property - getter() декаратор достает защищенный атрибут
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value
    
    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value
    
    def __str__(self):
        return f"Персонаж: {self.__name}, Здоровье: {self.__health}, Урон: {self.__damage}"

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None
        
        @property
        def defence(self):
            return self.__defence
        
        def choose_defence(self, heroes):
            random_hero = random.choice(heroes)
        
        def hit(self, heroes):
            for hero in heroes:
                if hero.health > 0 and self.health > 0:
                    hero.health = hero.health - self.damage
        
        def __str__(self):
            return "BOSS" + super().__str__() + f"Босс выбрал: {self.__defence}"

class Heroes(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Heroes, self).__init__(name, health, damage)
        self.__super_ability = super_ability
        @property
        def super_ability(self):
            return self.__super_ability
        
        def hit(self, boss):
            if boss.health > 0 and self.health > 0:
                boss.health -= self.damage
        
        def apply_super_power(self, boss, heroes):
            pass

class Warrior(Heroes):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, 'CRITICAL DAMAGE')
    def apply_super_power(self, boss, heroes):
        critical = random.randint(1, 7)
        boss.health -= self.damage * critical
        print(f'Удар увеличился в {critical} раз')

class Medic(Heroes):
    def __init__(self, name, health, damage):
        super(Medic, self).__init__(name, health, damage, 'Healling')
    def apply_super_power(self, boss, heroes):
        heal_point = random.randint(1,7)
        print(f'Healling {heal_point}')
        for hero in heroes:
            if hero in heroes:
                if hero != self and hero.health > 0:
                    hero.health += heal_point
round_counter = 0

def print_statictic(boss, heroes):
    print(f'________ROUND {round_counter}________')
    print(boss)
    for hero in heroes:
        print(hero)

def play_round(boss, heroes):
        # global -- чтобы одна переменная работала в других
        global round_counter
        round_counter += 1
        boss.choose_defence(heroes)
        boss.hit(heroes)
        
        for hero in heroes:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
        
def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes win!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
        
        if all_heroes_dead:
            print("Boss Win!")
        return all_heroes_dead

def start_game():
    boss = Boss("Syimyk", 200, 20)
    warrior = Warrior('Warrior1', 100, 20)
    medic = Medic('medic', 65, 0)
    
    heroes = [warrior, medic]
    
    print_statictic(boss, heroes)
    
    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)

start_game()