import random
from Characters import Character


class Maruzen(Character):

    def __init__(self):
        super().__init__("Maruzen", 30, 0, 0, 100, 100, 0, 0)

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

    def basic_attack(self, enemy):

        if self.is_enraged():
            return self.enraged_basic(enemy)

        print("Why would I fight?")

        self.Sanity += 10

        if random.random() < 0.1:
            print("Bonus turn!")
            return True

        return False

    def skill_1(self, enemy):

        if self.is_enraged():
            return self.enraged_skill_1(enemy)

        print("Please slap me")

        self.Hp += self.last_damage_taken
        self.Sanity -= 20

    def skill_2(self, enemy):

        if self.is_enraged():
            return self.enraged_skill_2(enemy)

        print("Immune to physical damage!")
        self.add_buff("Invincible", 2)
        self.Sanity -= 30

    def skill_3(self, enemy):

        if self.is_enraged():
            return self.enraged_skill_3(enemy)

        print("Sanity implosion!")
        dmg = self.Sanity / 2
        enemy.take_damage(dmg, self)
        self.Sanity -= dmg

    # ==========================
    # ENRAGED FORM
    # ==========================

    def enraged_basic(self, enemy):

        print("Payback")

        hits = 1
        r = random.random()

        if r < 0.15:
            hits = 3
        elif r < 0.45:
            hits = 2

        for i in range(hits):
            self.Sanity += 5

        if hits == 3:
            dmg = enemy.MaxHp * 0.13
            enemy.Hp -= dmg
            print(f"Combo finisher! Dealt {dmg} damage")

    def enraged_skill_1(self, enemy):

        print("Manipulation")

        chance = 0.05 * self.turn_counter

        if random.random() < chance:
            print("Enemy surrendered!")
            enemy.Hp = 0
        else:
            print("Failed!")

    def enraged_skill_2(self, enemy):

        print("Death wish")

        dmg = 30 + ((100 - self.Sanity) / 5)
        enemy.Hp -= dmg
        self.Sanity -= 10

    def enraged_skill_3(self, enemy):

        print("System sabotage")
        enemy.add_debuff("Sabotage", 2)

    # ==========================

    def get_skill_cd(self, move):
        if move == 2:
            return 2
        if move == 3:
            return 5
        if move == 4:
            return 4
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp} | Sanity:{self.Sanity} | Form:{self.Form}"
