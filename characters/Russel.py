from characters.Characters import Character

class Russel(Character):

    def __init__(self):
        super().__init__("Russel", 200, 15, 0, 0, 5, 65, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

        self.Form = "normal"

    def take_damage(self, dmg, enemy):
        # Start with base damage
        final_damage = dmg * 0.8
        
        # Apply sleeping buff reduction
        if self.has_buff("Sleeping"):
            final_damage *= 0.85
            print(f"{self.Name} reduces damage while sleeping!")
        
        # Apply vulnerable debuff increase
        if self.has_debuff("Vulnerable"):
            final_damage *= 1.2
            print(f"{self.Name} is Vulnerable and takes 20% more damage!")
        
        # Apply the damage
        self.Hp -= final_damage
        print(f"{self.Name} took {final_damage:.1f} damage!")

        # Check if HP is low and trigger regen
        if self.Hp <= self.MaxHp * 0.3:
            if not self.has_buff("Regen"):
                self.add_buff("Regen", 3)
                print(f"{self.Name} is below 30% HP and gains regen!")

            heal = self.MaxHp * 0.05
            self.Hp = min(self.Hp + heal, self.MaxHp)
            print(f"{self.Name} heals {heal:.1f} HP!")
           
    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            dmg = 20 + (self.Atk * 0.5)
            enemy.take_damage(dmg, self)
            print(f"{self.Name} used Basic Attack!")
        else:
            print(f"{enemy.Name} evaded your attack!")

    def skill_1(self, enemy):
        print(f"{self.Name} used Deep Sleep!")
        
        self.add_buff("Sleeping", 1)
        heal_amount = self.MaxHp * 0.3
        self.Hp = min(self.Hp + heal_amount, self.MaxHp)

        print(f"{self.Name} is now sleeping and healed for {heal_amount:.1f} HP!")

    def skill_2(self, enemy):
        print(f"{self.Name} used Mutual Vulnerability!")

        enemy.add_debuff("Basic Only", 2)
        self.add_debuff("Vulnerable", 2)
        enemy.add_debuff("Vulnerable", 2)
        
        print(f"Both fighters are now vulnerable!")
    
    def skill_3(self, enemy):
        print(f"{self.Name} used Last Stand!")

        if self.Hp <= 0:
            self.Hp = self.MaxHp
            print(f"{self.Name} revives with {self.Hp} HP!")
        else:
            print("Skill can only be used when defeated!")     


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

    def stats(self):
        return f"{self.Name} | HP:{self.Hp}"
    
    def end_turn_checks(self):
        if self.is_alive():
            if self.has_buff("Regen"):
                heal = self.MaxHp * 0.05
                self.Hp = min(self.Hp + heal, self.MaxHp)
                print(f"{self.Name}'s Regen activated! Healed {heal:.1f} HP!")
