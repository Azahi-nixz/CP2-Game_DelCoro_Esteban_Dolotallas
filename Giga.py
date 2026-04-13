

from Characters import Character


class Giga(Character):

    def __init__(self):
        super().__init__("Giga", 100, 20, 0, 0, 20, 70, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

    def take_damage(self, dmg, enemy):

        if self.has_buff("Invincible"):
            print(f"{self.Name} is invincible! No damage taken!")
            return

        reflected = dmg * 0.3
        reduced = dmg - reflected
        self.Hp -= reduced
        enemy.Hp -= reflected

        print(f"{self.Name} took {dmg} damage!")
        print(f"{enemy.Name}'s attack reflected! Dealt {reflected} DMG!")



    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            print("Used Basic Attack!")
            dmg = self.Atk * 0.5

            if self.has_buff("Double Damage"):
                print(f"{self.Name} has double damage!")
                dmg *= 2

            if self.has_buff("Enhanced"):
                dmg *= 2

            enemy.take_damage(dmg, self)
        else:
            print(f"{enemy.Name} evaded your attack!")

    def end_turn_checks(self):
        if self.has_buff("Enhanced"):
            print(f"{self.Name} is Enhanced! Stats are currently doubled.")

    def skill_1(self, enemy):
        print(" Giga used Skill 1! ")
        self.add_buff("Double Damage", 1)


    def skill_2(self, enemy):
        print("Giga used Skill 2!")

        self.add_buff("Invincible", 2)

        print(f"{self.Name} is immune to damage for 2 turns!")


    def skill_3(self, enemy):
        print("Giga used Skill 3!")
        self.add_buff("Enhanced", 2)

        print(f"{self.Name}'s stats are doubled for 2 turns!")

    def get_skill_cd(self, move):
        if move == 2:
            return 3
        if move == 3:
            return 3
        if move == 4:
            return 4
        return 0

    def check_transformation(self):
        pass

    def stats(self):
        return f"{self.Name} | HP:{self.Hp} | Form:{self.Form}"