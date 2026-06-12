from characters.Characters import Character


class SolEmberload(Character):

    def __init__(self):
        super().__init__("Sol Emberload", 105, 35, 0, 0, 55, 65, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3,
        }

        self.Form = "normal"

    def take_damage(self, dmg, enemy):
        self.Hp -= dmg
        if self.Hp < 0:
            self.Hp = 0
        print(f"{self.Name} took {dmg:.1f} damage!")

    def basic_attack(self, enemy):
        """Ember Strike — deals ATK damage and applies Burned debuff."""
        if self.check_hit(enemy):
            dmg = self.Atk
            print(f"{self.Name} used Ember Strike!")
            enemy.take_damage(dmg, self)
            enemy.add_debuff("Burned", 2)
        else:
            print(f"{enemy.Name} evaded your attack!")

    def skill_1(self, enemy):
        """Sol Kick — deals ATK + 25 damage."""
        if self.check_hit(enemy):
            dmg = self.Atk + 25
            print(f"{self.Name} used Sol Kick!")
            enemy.take_damage(dmg, self)
        else:
            print(f"{enemy.Name} evaded your attack!")

    def skill_2(self, enemy):
        """Smoke Veil — reduces enemy accuracy by 30 and heals self 15 HP."""
        print(f"{self.Name} used Smoke Veil!")
        enemy.add_debuff("Blinded", 2)
        self.Hp = min(self.Hp + 15, self.MaxHp)
        print(f"{self.Name} heals 15 HP! Current HP: {int(self.Hp)}")

    def skill_3(self, enemy):
        """Inferno Burst — massive fire attack, deals 2x ATK and burns for 3 turns."""
        if self.check_hit(enemy):
            print(f"{self.Name} used Inferno Burst!")
            dmg = self.Atk * 2
            enemy.take_damage(dmg, self)
            enemy.add_debuff("Burned", 3)
            print("The enemy is engulfed in flames!")
        else:
            print(f"{enemy.Name} evaded your attack!")

    def end_turn_checks(self):
        # Passive: Sol Emberload burns 5 HP per turn — the flame consumes him too
        if self.is_alive():
            self.Hp -= 5
            if self.Hp < 1:
                self.Hp = 1  # Won't die from own flame passive
            print(f"{self.Name}'s flame flickers... -5 HP passively!")

    def check_transformation(self):
        pass

    def get_skill_cd(self, move):
        if move == 2:
            return 3
        if move == 3:
            return 2
        if move == 4:
            return 5
        return 0

    def stats(self):
        return f"{self.Name} | HP:{self.Hp}"
