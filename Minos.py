import random

from Characters import Character

class Minos(Character):
    def __init__(self):
        super().__init__("Minos", 50, 0, 0, 0, 25, 0, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.Form = "normal"
        self.luck = 15

    def take_damage(self, dmg, enemy):

        if self.has_buff("Immortality"):
            print("Minos has immortality!")

        if self.has_debuff("Vulnerable"):
            dmg *= 2
            self.Hp -= dmg

        self.Hp -= dmg

    def check_transformation(self):
       pass

    def skill_1(self, enemy):
        print("Dunca Tonca!")
        self.luck += 5

    def skill_2(self, enemy):
        print("Take it all!")
        r = random.random()
        if r < 0.5:
            self.add_buff("S.E. Immunity", 5)
            self.add_buff("Health Regen", 5)
            print("Passive Jackpot activated!")
        elif r >= 0.5:
            self.add_buff("Vulnerable", 5)

    def skill_3(self, enemy):
        print("Immortality!")
        self.add_buff("Immortality", 2)

    def basic_attack(self, enemy):
        r = random.randint(1, 10000)
        if r <= 10 * self.luck:
            enemy.take_damage(999, self)
            print("LUCKY! DEALT 999 dmg!")
        if 400 >= r > 10 * self.luck:
            enemy.take_damage(40, self)
        if 900 >= r > 400:
            enemy.take_damage(35, self)
        if 1400 >= r > 900:
            enemy.take_damage(35, self)
        if 1900 >= r > 1400:
            enemy.take_damage(25, self)
        if 3400 >= r > 1900:
            enemy.take_damage(20, self)
        if 5000 >= r > 3400:
            enemy.take_damage(15, self)
        if 7000 >= r > 5000:
            enemy.take_damage(10, self)
        if 8500 >= r > 7000:
            enemy.take_damage(5, self)
        if 10000 >= r > 8500:
            enemy.take_damage(1, self)
    def get_skill_cd(self, move):
        if move == 2:
            return 2
        if move == 3:
            return 1
        if move == 4:
            return 10
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp}"

    def end_turn_checks(self):
        if self.has_buff("Health Regen"):
            heal = 5
            self.Hp += heal
            print("Health regen activated! Healed 5 HP!")

        self.turn_counter += 1
        if self.turn_counter % 5 == 0:
            self.passive()
    def passive(self):
        r = random.random()
        if r < 0.5:
            self.add_buff("S.E. Immunity" , 5)
            self.add_buff("Health Regen", 5)
            print("Passive Jackpot activated!")
        elif r >= 0.5:
            self.add_buff("Vulnerable", 5)
