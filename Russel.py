from Characters import Character

class Russel (Character):

    def __init__(self):
        super().__init__ ("Russel", 200, 15, 0, 0, 5, 65, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

    def take_damage (self, dmg, enemy):
        final_damage = dmg * 0.8
        self.Hp -= final_damage 

        print(f"{self.Name} took {final_damage} damage!!")

        if self.has_buff("Sleeping"):
           reduce_damage *= 0.85
           print(f"{self.Name} reduce the damage while sleeping!")
        self.Hp -= reduce_damage

        print (f"{self.Name} took {reduce_damage} damage!!")

        if self.has_buff("Vulnerable"):
            reduce_damage *= 1.2
            print (f"{self.Name} is Vulnerable and takes 20% more damage!")
            self.Hp -= reduce_damage

            print(f"{self.Name} took {reduce_damage} damage!!")

        if self.Hp <= self.MaxHp * 0.3:
            if not self.has_buff("Regen"):

                self.add_buff("Regen", 3)
            print(f"{self.Name} is below 30% HP and gains regen!")

            heal = self.MaxHp * 0.05
            self.Hp = min(self.Hp + heal, self.MaxHp)

            print(f"{self.Name} heals {heal} HP!")
           
    def basic_attack(self, enemy):
        print(f"{self.Name} used Basic Attack!")
        enemy.take_damage (self.Atk, self)

    def skill_1 (self, enemy):
        print("Russel used Skill 1!")
        
        self.add_buff("Sleeping", 1)
        Max = self.MaxHp * 0.3
        self.Hp += Max

        if self.Hp > self.MaxHp:
            self.Hp = self.MaxHp 

        print(f"{self.Name} is now sleeping and healed for {Max} HP!")    

    def skill_2 (self, enemy):
        print ("Russel used Skill 2!")

        enemy.add_buff ("Basic Only",2)

        self.add_buff ("Vulnerable", 2)
        enemy.add_buff ("Vulnerable", 2)
    
    def skill_3 (self, enemy):
        print ("Russel used Skill 3!!")

        if self.Hp <= 0:
            self.Hp = self.MaxHp * 1
            print(f"{self.Name} revives with {self.Hp} HP!!")
        else:
            print ("Skill can be only used when defeated")     


    def get_skill_cd(self, move):
        if move == 2:
            return 5
        if move == 3:
            return 2
        if move == 4:
            return 999
        return 0
    
    def check_transformation(self):
        pass

    def stats (self):
        return f"{self.Name}  |  HP: {self.Hp}  | Form: {self.Form}"
