from characters.Characters import Character

class Sed(Character):
    def __init__(self):
        super().__init__("Sed", 100, 30, 0, 0, 40, 80, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.Form = "normal"

    def take_damage(self, dmg, enemy):

        self.Hp -= dmg

    def check_transformation(self):
       pass

    def skill_1(self, enemy):
        print("Serene posture")
        self.add_buff("BA boost", 3)

    def skill_2(self, enemy):
        if self.check_hit(enemy):
            print("Warhammer Onslaught")
            dmg = (self.Atk * 0.6)
            enemy.take_damage(dmg, self)

        else: print("Enemy evaded your attack!")

    def skill_3(self, enemy):
        print("Summon: War Maiden Ei-ram")
        self.add_buff("Excalibur", 3)

        self.debuffs.clear()

    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            dmg = 20 + (self.Spd * 0.1)
            enemy.take_damage(dmg, self)
            print("Gale slash")
        else: print(f"{enemy.Name} evaded your attack!")

    def get_skill_cd(self, move):
        if move == 2:
            return 5
        if move == 3:
            return 2
        if move == 4:
            return 5
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp}"

    def end_turn_checks(self):
        if self.is_alive():
            if self.has_buff("Excalibur"):
                self.Atk = 70
            else:
                self.Atk = 30
