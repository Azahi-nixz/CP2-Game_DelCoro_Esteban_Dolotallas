from Characters import Character

class Zen(Character):
    def __init__(self):
        super().__init__("Zen", 80, 30, 100, 0, 90, 80, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.blood_rage = 0
        self.total_damage = 0
        self.incoming_debuff = ""
        self.form = "normal"

    def take_damage(self, dmg, enemy):

        # Reflect mechanic
        if self.has_buff("High counter"):

            reduced = dmg * 0.7
            reflected = dmg * 0.3

            print("High Counter activated!")

            if enemy:
                enemy.take_damage(reflected, self)

            if self.debuffs:
                debuff_name = next(iter(self.debuffs))  # get any debuff
                duration = self.debuffs[debuff_name]

                print(f"Reflected debuff: {debuff_name}!")
                enemy.add_debuff(debuff_name, duration)

            self.Hp -= reduced
            return

        self.Hp -= dmg

    def check_transformation(self):
        if self.blood_rage > 100:
            self.form = "Blood rage"


    def skill_1(self, enemy):
        print("A lost cause....")
        dmg = self.Atk * 0.2
        enemy.take_damage(dmg, enemy)
        self.blood_rage += 40

    def skill_2(self, enemy):
        print("A silent plead....")
        self.add_buff("High counter" , 3)

    def skill_3(self, enemy):
        print("Death slash!")
        dmg = self.Atk
        enemy.take_damage(dmg, enemy)
        self.blood_rage /= 2

    def basic_attack(self, enemy):
        if self.form == "normal":
            enemy.take_damage(5 , enemy)
            print("Zen used basic attack!")
            self.blood_rage += 5
        elif self.form == "Blood rage":
            dmg = self.Atk
            enemy.take_damage(dmg, enemy)
            self.blood_rage += dmg
            print("Zen used Blood rage!")

    def get_skill_cd(self, move):
        if move == 2:
            return 1
        if move == 3:
            return 3
        if move == 4:
            return 3
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp} | Sanity:{self.Sanity} | Form:{self.Form}"

    def end_turn_checks(self):
        pass

