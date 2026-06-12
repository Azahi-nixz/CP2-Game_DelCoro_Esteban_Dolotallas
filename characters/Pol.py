from characters.Characters import Character

class Pol(Character):
    def __init__(self):
        super().__init__("Pol", 60, 30, 0, 0, 50, 70, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.Form = "normal"

    def take_damage(self, dmg, enemy):

        # Reflect mechanic
        if self.has_buff("High counter"):

            reduced = dmg * 0.7
            reflected = dmg * 0.3

            print("High Counter activated!")

            if enemy:
                enemy.take_damage(reflected, self)

            if self.debuffs:
                debuff_name = next(iter(self.debuffs))
                duration = self.debuffs[debuff_name]

                print(f"Reflected debuff: {debuff_name}!")
                enemy.add_debuff(debuff_name, duration)

            self.Hp -= reduced
            return

        self.Hp -= dmg

    def check_transformation(self):
       pass

    def skill_1(self, enemy):
        print("Stance: Unyielding")
        self.add_buff("High Counter", 3)

    def skill_2(self, enemy):
        if self.check_hit(enemy):
            print("Drive: Windcharge")
            dmg = (self.Atk * 0.2) + (self.Spd * 0.3)
            enemy.take_damage(dmg, self)

        else: print("Enemy evaded your attack!")

    def skill_3(self, enemy):
        print("Summon: Wind Maiden Hael")
        self.add_buff("Covenant of the wind", 3)

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
           if self.has_buff("Covenant of the wind"):
            self.Spd = 120
            self.Atk = 50
