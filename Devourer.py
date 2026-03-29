from Characters import Character

class Devourer(Character):
    def __init__(self):
        super().__init__("Devourer", 40, 60, 0, 0, 45, 75, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.Form = "normal"

    def take_damage(self, dmg, enemy):

        if self.has_buff("Immortality"):
            print("Devourer has immortality!")

        self.Hp -= dmg

    def check_transformation(self):
       pass

    def skill_1(self, enemy):
        print("Lemme suck 'em")
        heal = enemy.Hp * 0.2
        self.Hp += heal
        print(f"Devourer recovered {heal} health!")

    def skill_2(self, enemy):
        if self.check_hit(enemy):
            print("Lethal claw!")
            enemy.take_damage(20, enemy)
            enemy.add_debuff("Poison" , 2)
        else: print(f"{enemy.Name} evaded your attack!")

    def skill_3(self, enemy):
        print("Immortality!")
        self.add_buff("Immortality", 2)

    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            dmg = 20 + (self.Atk * 0.1)
            enemy.take_damage(dmg, enemy)
            print("Slash!")
        else: print(f"{enemy.Name} evaded your attack!")

    def get_skill_cd(self, move):
        if move == 2:
            return 4
        if move == 3:
            return 3
        if move == 4:
            return 5
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp}"

    def end_turn_checks(self):
        if self.is_alive():
            self.Hp += 5
            print("Devourer's iron will activated! 5 HP added!")



