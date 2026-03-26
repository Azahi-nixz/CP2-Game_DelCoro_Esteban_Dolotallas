import random

from Characters import Character

class Maruzen(Character):

    def __init__(self):
        super().__init__("Maruzen", 30, 10, 0, 120, 30, 70, 0)

    def basic_attack(self):
        print("Maruzen used Basic Attack!")
        self.Sanity += 10

        chance = random.random()

        if chance < 0.1:
            print("Why should I fight activated! Bonus turn!")
            return True
        return False

    def skill_1(self, enemy):
        print("Maruzen used Skill 1!")
        enemy_dmg = enemy.damage(self)
        self.Hp += enemy_dmg
        self.Sanity -= 20

    def skill_2(self, enemy):
        print("Maruzen used Skill 2! Immune to damage for two turns")
        self.Eff = 2

    def skill_3(self):
        print("Maruzen used Skill 3!")

        while True:
            try:
                choice = int(input("""
Predict the enemy's move:
1. Basic Attack
2. Skill 1
3. Skill 2
4. Skill 3
> """))
                if choice in [1,2,3,4]:
                    break
                else:
                    print("Invalid prediction.")
            except ValueError:
                print("Enter a number.")

        print("Enemy is now under unreal calculation!")
        return choice

    def stats(self):
        return f"{self.Name} | HP: {self.Hp} | Sanity: {self.Sanity}"

    def skill1_cd(self):
        return 2

    def skill2_cd(self):
        return 5

    def skill3_cd(self):
        return 4
