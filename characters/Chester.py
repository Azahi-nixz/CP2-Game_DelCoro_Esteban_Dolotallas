# Sol Emberlord
import characters.Characters 
import Characters

class Chester(Characters.Characters):
    def __init__(self):
        super().__init__("Chester", 105, 10, 5, 0, 0, 65, 75, 0 )

    self.skills = {
        1:self.basic_attack,
        2:self.skill_1,
        3:self.skill_2,
        4:self.skill_3,
    }        

    def take_damage(self, dmg):
        self.Hp -= dmg
        if self.Hp < 0:
            self.Hp = 0
        print(f"{self.name} takes {dmg} damage. Remaining HP: {self.Hp}")

    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            dmg = self.Atk 
            print(f"{self.Name} used Basic Attack!")
            enemy.take_damage(dmg)
            enemy.add_debuff("Burned", 2)
        else:
            print(f"{self.Name}'s attack missed!")

    def end_turn_checks(self):
        self.Hp -= 5 

    def skill_1(self, enemy):
        # Skill 1 - Sol Kick
        if self.check_hit(enemy):
            dmg = self.Atk + 25
            print(f"{self.Name} used Skill 1!")
            enemy.take_damage(dmg)
        else:
            print(f"{self.Name}'s attack missed!")
    
    def skill_2(self, enemy):
        enemy.Acc -= 30
        self.Hp += 15
        print(f"{self.Name} used Skill 2! Enemy's accuracy reduced by 30 for 2 turns.")
        print(f"{self.Name} heals for 15 HP. Current HP: {self.Hp}")

    def skill_3(self, enemy):
        if self.check_hit(enemy):    