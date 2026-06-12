import random
from characters.Characters import Character


class Hotori(Character):

    def __init__(self):
        super().__init__("Hotori", 80, 25, 0, 0, 60, 75, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.last_damage_taken = 0
        self.Form = "normal"

    # ==========================
    # PASSIVE — 20% bonus turn on basic attack
    # ==========================

    def basic_attack(self, enemy):
        print("Basic Attack!")
        if self.check_hit(enemy):
            enemy.take_damage(15, self)
            if random.random() < 0.2:
                print("Bonus turn!")
                return True
        else:
            print(f"{enemy.Name} evaded your attack!")
        return None

    # ==========================
    # SKILLS
    # ==========================

    def skill_1(self, enemy):
        """Chrono Shift — recover last damage taken as HP."""
        print("Chrono Shift!")
        if self.last_damage_taken > 0:
            self.Hp = min(self.Hp + self.last_damage_taken, self.MaxHp)
            print(f"{self.Name} recovered {self.last_damage_taken:.1f} HP!")
        else:
            print("No damage to recover.")

    def skill_2(self, enemy):
        """Godspeed — deal 30% of enemy current HP as damage."""
        if self.check_hit(enemy):
            print("Godspeed!")
            dmg = enemy.Hp * 0.3
            enemy.take_damage(dmg, self)
        else:
            print(f"{enemy.Name} evaded your attack!")

    def skill_3(self, enemy):
        """Time Stop — freeze enemy for 4 turns. Resets skills 1-3 only.
        The ult CD (move 4) is locked at 10 and cannot be reset by any means."""
        print("Time Stop!")
        enemy.add_debuff("Frozen", 4)
        # Save the ult's current cooldown before touching anything
        ult_cd = self.cooldowns.get(4, 0)
        # Reset only skills 1-3
        for move in (1, 2, 3):
            self.cooldowns[move] = 0
        # Always restore ult CD — this ensures it can never be zeroed by this skill
        self.cooldowns[4] = ult_cd
        print(f"{self.Name} reset skill cooldowns (1-3)!")
        return True

    # ==========================
    # DAMAGE
    # ==========================

    def take_damage(self, dmg, enemy):
        if self.has_buff("Invincible"):
            print(f"{self.Name} is invincible! No damage taken!")
            return

        self.Hp -= dmg
        self.last_damage_taken = dmg
        print(f"{self.Name} took {dmg:.1f} damage!")

    def check_transformation(self):
        pass

    def get_skill_cd(self, move):
        if move == 2:
            return 2
        if move == 3:
            return 3
        if move == 4:
            return 10
        return 0

    def end_turn_checks(self):
        pass

    def stats(self):
        return f"{self.Name} | HP:{self.Hp} | Form:{self.Form}"
