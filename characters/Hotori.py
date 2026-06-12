import random
from characters.Characters import Character


class Hotori(Character):

    def __init__(self):
        super().__init__("Maruzen", 40, 0, 0, 100, 30, 0, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.last_damage_taken = 0
        self.first_turn = True

        self.death_immunity_turns = 0
        self.negative_hp_turns = 0

    # ==========================
    # STATE
    # ==========================

    def is_enraged(self):
        return self.Form == "enraged"

    def check_transformation(self):
        if self.Sanity <= 30 and self.Form != "enraged":
            print("Entered ENRAGED MODE!")
            self.Form = "enraged"
            self.death_immunity_turns = 2
            self.negative_hp_turns = 2

    # ==========================
    # PASSIVE
    # ==========================

    def take_damage(self, dmg, enemy):

        if self.has_buff("Invincible"):
            print(f"{self.Name} is invincible! No damage taken!")
            return

        if self.first_turn and dmg >= self.Hp:
            print("Immune to instant kill on first turn!")
            dmg = self.Hp - 1

        if self.is_enraged():
            reflected = dmg * 0.75
            if enemy:
                enemy.Hp -= reflected
                print(f"Reflected {reflected} damage!")

            dmg *= 0.25
        else:
            self.Sanity -= 10

        self.Hp -= dmg
        self.last_damage_taken = dmg

        print(f"{self.Name} took {dmg} damage!")

        # sanity death
        if self.Sanity <= 0:
            print("Sanity depleted! Maruzen dies!")
            self.Hp = 0

    def end_turn_checks(self):

        if self.is_enraged():

            if self.Hp <= 0 < self.death_immunity_turns:
                print("Survived with death immunity!")
                self.death_immunity_turns -= 1

            elif self.Hp <= 0:
                print("Maruzen has fallen!")

            if self.Hp < 0:
                self.negative_hp_turns -= 1

                if self.negative_hp_turns <= 0:
                    print("Failed to recover from negative HP!")
                    self.Hp = 0

    # ==========================
    # NORMAL FORM
    # ==========================

    def passive(self):

        if random.random() < 0.2:
            print("Bonus turn!")
            return True

        return False

    def skill_1(self, enemy):

        print("Chrono Shift")

        self.Hp += self.last_damage_taken
        return None

    def skill_2(self, enemy):

        if self.check_hit(enemy):
            print("Godspeed!")
            dmg = enemy.Hp * 0.3
            enemy.take_damage(dmg, self)

    def skill_3(self, enemy):
        enemy.add_debuff("Frozen", 4)
        for move in self.cooldowns:
            self.cooldowns[move] = 0

        return True

    def basic_attack(self, enemy):
        print("Basic Attack!")
        if self.check_hit(enemy):
            enemy.take_damage(15, self)
        return True




    def get_skill_cd(self, move):
        if move == 2:
            return 2

        if move == 3:

            return 3

        if move == 4:
            return 5
        return 0





    def stats(self):
        return f"{self.Name} | HP:{self.Hp} | Form:{self.Form}"
