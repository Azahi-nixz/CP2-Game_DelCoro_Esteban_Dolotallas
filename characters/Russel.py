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
        self.guardian_angel_used = False  # Track if Guardian Angel has been used
        self.age_of_retribution_triggered = False  # Track if Age of Retribution has been triggered

    def take_damage(self, dmg, enemy):
        # Passive: "Relentless Fortitude" - Reduce damage by 20%
        final_damage = dmg * 0.8
        print(f"{self.Name}'s Relentless Fortitude reduces damage by 20%!")
        
        # Apply sleeping buff reduction (15% additional reduction)
        if self.has_buff("Sleeping"):
            final_damage *= 0.85
            print(f"{self.Name} reduces damage by an additional 15% while sleeping!")
        
        # Apply vulnerable debuff increase (Let's Dance effect)
        if self.has_debuff("Vulnerable"):
            final_damage *= 1.2
            print(f"{self.Name} is Vulnerable and takes 20% more damage!")
        
        # Apply the damage
        self.Hp -= final_damage
        print(f"{self.Name} took {final_damage:.1f} damage!")

        # Passive: "Age of Retribution" - Trigger regen when HP <= 30% (one time)
        if self.Hp <= self.MaxHp * 0.3 and not self.age_of_retribution_triggered:
            self.add_buff("Age_Regen", 3)
            self.age_of_retribution_triggered = True
            print(f"{self.Name}'s Age of Retribution activates! Health regeneration for 3 turns!")

        # Check for Guardian Angel activation
        if self.Hp <= 0 and not self.guardian_angel_used:
            self.activate_guardian_angel()
            return
        
        # Ensure HP doesn't go below 0
        if self.Hp < 0:
            self.Hp = 0
           
    def basic_attack(self, enemy):
        if self.check_hit(enemy):
            dmg = 20 + (self.Atk * 0.5)
            enemy.take_damage(dmg, self)
            print(f"{self.Name} used Basic Attack!")
        else:
            print(f"{enemy.Name} evaded your attack!")

    def skill_1(self, enemy):
        """Skill 1: "Sleep Cures All" - Sleep and recover 30% of max health. Reduce damage by 15% while sleeping."""
        print(f"{self.Name} used Sleep Cures All!")
        
        # Add sleeping buff for 1 turn (the current turn becomes a skip)
        self.add_buff("Sleeping", 1)
        
        # Heal 30% of max health
        heal_amount = self.MaxHp * 0.3
        self.Hp = min(self.Hp + heal_amount, self.MaxHp)

        print(f"{self.Name} falls asleep and heals for {heal_amount:.1f} HP!")
        print(f"{self.Name} will take 15% reduced damage while sleeping!")

    def skill_2(self, enemy):
        """Skill 2: "Let's Dance!" (Taunt) - Make opponent use only basic attack. Both take 20% more damage."""
        print(f"{self.Name} used Let's Dance!")

        # Force enemy to only use basic attack next turn
        enemy.add_debuff("Taunted", 3)
        
        # Both take 20% more damage for the next turn
        self.add_debuff("Vulnerable", 3)
        enemy.add_debuff("Vulnerable", 3)
        
        print(f"{enemy.Name} is taunted and can only use basic attack next turn!")
        print(f"Both {self.Name} and {enemy.Name} take 20% more damage!")
    
    def skill_3(self, enemy):
        """Skill 3: "Guardian Angel" (Passive) - Auto-activates when dying. This is just a placeholder."""
        print(f"Guardian Angel is a passive ability - it activates automatically when {self.Name} would die!")
        print(f"Guardian Angel status: {'Already used' if self.guardian_angel_used else 'Available'}")
    
    def activate_guardian_angel(self):
        """Auto-activate Guardian Angel when HP reaches 0"""
        print(f"\n💫 Guardian Angel activates! 💫")
        
        # Revive with 35% HP
        self.Hp = self.MaxHp * 0.35
        self.guardian_angel_used = True
        
        # Become immune to negative status effects for next turn
        self.add_buff("Guardian_Immunity", 1)
        
        # Clear all current debuffs
        self.debuffs.clear()
        
        print(f"{self.Name} rejects death and returns with {self.Hp:.1f} HP!")
        print(f"{self.Name} is immune to negative status effects for 1 turn!")
        print(f"HP is capped at 35% of max health until next turn!")     


    def get_skill_cd(self, move):
        if move == 2:
            return 5
        if move == 3:
            return 3
        if move == 4:
            return 999
        return 0
    
    def check_transformation(self):
        pass

    def stats(self):
        return f"{self.Name} | HP:{self.Hp}"
    
    def end_turn_checks(self):
        """Handle end of turn effects"""
        if self.is_alive():
            # Age of Retribution regeneration (5% per turn for 3 turns)
            if self.has_buff("Age_Regen"):
                heal = self.MaxHp * 0.05
                
                # Cap HP at 35% if Guardian Angel was just used
                if self.has_buff("Guardian_Immunity"):
                    max_allowed_hp = self.MaxHp * 0.35
                    self.Hp = min(self.Hp + heal, max_allowed_hp)
                    print(f"{self.Name}'s Age of Retribution heals {heal:.1f} HP! (Capped at 35% due to Guardian Angel)")
                else:
                    self.Hp = min(self.Hp + heal, self.MaxHp)
                    print(f"{self.Name}'s Age of Retribution heals {heal:.1f} HP!")
    
    def add_debuff(self, debuff_name, duration):
        """Override to prevent debuffs when Guardian Immunity is active"""
        if self.has_buff("Guardian_Immunity"):
            print(f"{self.Name} is immune to {debuff_name} due to Guardian Angel!")
            return
        super().add_debuff(debuff_name, duration)
