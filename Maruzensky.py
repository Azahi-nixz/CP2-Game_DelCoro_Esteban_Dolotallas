import random

from Characters import Character


class Maruzen(Character):

    def __init__(self):
        super().__init__("Maruzen", 30, 5, 0, 100, 30, 70, 0)


    def basic_attack(self, enemy):

        print("Maruzen used Basic Attack!")

        if enemy.has_buff("Invincible"):
            print("Enemy is immune!")
            return False

        enemy.Hp -= self.Atk
        self.Sanity += 10

        chance = random.random()

        if chance < 0.1:
            print("Why should I fight activated! Bonus turn!")
            return True

        return False


    def skill_1(self, enemy):

        print("Maruzen used Skill 1!")

        if not self.enraged():

            enemy_dmg = enemy.Atk
            self.Hp += enemy_dmg
            self.Sanity -= 20

        else:

            chance = random.random()

            if chance <= 0.05:
                print("Enemy surrendered!")
                enemy.Hp = 0
            else:
                print("Manipulation failed!")


    def skill_2(self, enemy):

        if not self.enraged():

            print("Maruzen became immune for 2 turns!")

            self.add_buff("Invincible", 2)

        else:

            dmg = 30 + ((120 - self.Sanity) / 10)
            enemy.Hp -= dmg

            print(f"Maruzen dealt {dmg} damage!")


    def skill_3(self):

        print("Maruzen used Skill 3!")

        while True:

            try:

                choice = int(input("""
Predict enemy move
1 Basic
2 Skill1
3 Skill2
4 Skill3
> """))

                if choice in [1,2,3,4]:
                    break

            except:
                pass

        return choice


    def enraged(self):

        if self.Sanity <= 50:

            if self.Form != "enraged":
                print("Maruzen entered ENRAGED mode!")

            self.Form = "enraged"
            return True

        self.Form = "normal"
        return False

    def skill1_cd(self):
         return 2

    def skill2_cd(self):
         return 5

    def skill3_cd(self):
        return 4

    def stats(self):

        return f"{self.Name} | HP:{self.Hp} | Sanity:{self.Sanity}"