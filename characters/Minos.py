import random

from characters.Characters import Character

class Minos(Character):
    def __init__(self):
        super().__init__("Minos", 60, 0, 0, 0, 25, 0, 0)

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
            return

        if self.has_debuff("Vulnerable"):
            dmg *= 2

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
            self.add_debuff("Vulnerable", 5)

    def skill_3(self, enemy):
        print("Immortality!")
        self.add_buff("Immortality", 2)

    def basic_attack(self, enemy):
        r = random.randint(1, 10000)
        threshold = 10 * self.luck

        if r <= threshold:
            enemy.take_damage(999, self)
            print("LUCKY! DEALT 999 dmg!")
        elif r <= 400:
            enemy.take_damage(40, self)
        elif r <= 900:
            enemy.take_damage(35, self)
        elif r <= 1400:
            enemy.take_damage(35, self)
        elif r <= 1900:
            enemy.take_damage(25, self)
        elif r <= 3400:
            enemy.take_damage(20, self)
        elif r <= 5000:
            enemy.take_damage(15, self)
        elif r <= 7000:
            enemy.take_damage(10, self)
        elif r <= 8500:
            enemy.take_damage(5, self)
        elif r <= 10000:
            enemy.take_damage(1, self)

    def end_turn_checks(self):
        if self.has_buff("Health Regen"):
            heal = self.MaxHp * 0.1
            self.Hp += heal
            print(f"Health regen activated! Healed {heal} HP!")

        if self.turn_counter > 0 and self.turn_counter % 5 == 0:
            self.passive()

    def get_skill_cd(self, move):
        if move == 2:
            return 2
        if move == 3:
            return 4
        if move == 4:
            return 10
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp}"

    def passive(self):
        r = random.random()
        if r < 0.5:
            self.add_buff("S.E. Immunity", 5)
            self.add_buff("Health Regen", 5)
            print("Passive Jackpot activated!")
        elif r >= 0.5:
            self.add_debuff("Vulnerable", 5)
