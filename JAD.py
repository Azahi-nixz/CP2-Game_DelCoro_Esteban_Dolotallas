import random

from Characters import Character

class JAD(Character):
    def __init__(self):
        super().__init__("Zen", 40, 60, 0, 0, 100, 100, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.ammo = 3
        self.Form = "Gun"

    def take_damage(self, dmg, enemy):

        self.Hp -= dmg

    def check_transformation(self):

        if self.ammo > 0:
            self.Form = "Gun"
        else:
            self.Form = "Hand"

    def skill_1(self, enemy):
        print("Gunho")

        enemy.buffs.clear()
        self.debuffs.clear()

        print("Cancelled all ongoing enemy buffs and self debuffs.")


    def skill_2(self, enemy):
        if self.Form == "Gun":
            print("Long shot!")
            if self.ammo < 2:
                "Insufficient ammo! Used knife skill 1 instead!"
                print("Backstab")
                dmg = self.Atk * 0.4
                enemy.take_damage(dmg, enemy)
            if self.is_headshot() and self.check_hit(enemy):
                self.ammo -= 2
                hp = enemy.Hp
                dmg = hp - 1
                enemy.take_damage(dmg, enemy)
            else: print(f"{enemy.Name} evaded your attack!")
        elif self.Form == "Hand":
            print("Backstab")
            dmg = self.Atk * 0.4
            enemy.take_damage(dmg, enemy)

    def skill_3(self, enemy):
            if self.Form == "Gun":
                print("Mist")
                if self.ammo == 3:
                    enemy.add_debuff("Blindness" , 2)
                    self.ammo -= 3
                else:
                    print("Insufficient ammo! Used knife ult instead!")
                    print("Throat cutter")
                    r = random.randint(0, 100)
                    chance = self.Accuracy * 0.15
                    if chance >= r:
                        enemy.Hp = 0
                        print("Enemy executed!")
                    else:
                        print("Failed to execute!")
            elif self.Form == "Hand":
                print("Throat cutter")
                r = random.randint(0, 100)
                chance = self.Accuracy * 0.15
                if chance >= r:
                    enemy.Hp = 0
                    print("Enemy executed!")
                else:
                    print("Failed to execute!")

    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            if self.Form == "Gun":
                dmg = self.Atk * 0.3
                self.ammo -= 1
                enemy.take_damage(dmg , enemy)
                print("J.A.D. used his gun!")
            elif self.Form == "Hand":
                dmg = self.Atk * 0.2
                enemy.take_damage(dmg, enemy)
                print("J.A.D. used his knife!")
        else: print(f"{enemy.Name} evaded your attack!")

    def is_headshot(self):
        r = random.randint(0, 100)
        chance = 10

        if chance <= r:
            return True
        else:
            return False

    def get_skill_cd(self, move):
        if move == 2:
            return 1
        if move == 3:
            return 3
        if move == 4:
            return 3
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp} | Ammunition: {self.ammo} | Form:{self.Form}"

    def end_turn_checks(self):
        self.ammo = min(self.ammo + 1, 3)
        if self.ammo < 0:
            self.ammo = 0
        if self.ammo == 0:
            self.Form = "Hand"


