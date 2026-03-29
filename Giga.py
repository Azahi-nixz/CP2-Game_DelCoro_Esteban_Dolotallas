

from Characters import Character


class Giga(Character):

    def __init__(self):
        super().__init__("Giga", 100, 30, 0, 0, 20, 80, 0)

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

        self.Hp -= dmg
        print(f"{self.Name} took {dmg} damage!")


    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            print("Used Basic Attack!")
            dmg = self.Atk * 0.5
            enemy.take_damage(dmg , enemy)

            # If skill 1 is activated
            if self.has_buff("Double Damage"):
                print(f"{self.Name} has double damage!")
                dmg += dmg  # apply the effect
                enemy.take_damage(dmg , enemy)

            else:
                print("Normal damage.")
        else:
             print(f"{enemy.Name} evaded your attack!")


    def skill_1(self, enemy):
        print(" Giga used Skill 1! ")
        self.add_buff("Double Damage", 1)


    def skill_2(self, enemy):
        print("Giga used Skill 2!")

        # GIGA TURN
        # Negates damage for 2 turns
        self.add_buff("Invincible", 2)

        print(f"{self.Name} is immune to damage for 2 turns!")


    def skill_3(self, enemy):
        print("Giga used Skill 3!")
        self.add_buff("Enhanced", 2)

        print(f"{self.Name}'s stats are doubled for 2 turns!")

    def end_turn_checks(self):
        if "Enhanced" in self.buffs:
            self.Atk *= 2
            self.Hp *= 2

    def get_skill_cd(self, move):
        if move == 2:
            return 1
        if move == 3:
            return 3
        if move == 4:
            return 3
        return 0

    def check_transformation(self):
        pass

    def stats(self):
        return f"{self.Name} | HP:{self.Hp} | Form:{self.Form}"