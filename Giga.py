import random


from Characters import Character

class Giga (Character):

    def __init__(self):
        super().__init__("Giga", 180, 20, 0, 0, 70, 70, 0)

        self.skills = {
            1: self.basic_attack,
            2: self.skill_1,
            3: self.skill_2,
            4: self.skill_3
        }

def basic_attack(self, enemy):
    print("Used Basic Attack!")
    dmg = self.Atk
    
    # If skill 1 is activated
    if self.has_buff("Double Damage"):
        print(f"{self.Name} has double damage!")
        dmg *= 2  # apply the effect
    
    else:
        print("Normal damage.")
    
    # Apply damage to enemy (optional, if you have HP system)
    enemy.hp -= dmg
    print(f"{enemy.name} took {dmg} damage!")

    return True

def skill_1 (self, enemy):

    print (" Giga used Skill 1! ")
    # GIGA SMASH
    # Everytime GigaSmash skill activates, doubling the next basic attack and reducing the cooldown of the other skill
        
def skill_2(self, enemy):
    print("Giga used Skill 2!")
    
    # GIGA TURN
    # Negates damage for 2 turns
    self.add_buff("Damage Immunity", 2)
    
    print(f"{self.Name} is immune to damage for 2 turns!")
    
    return True

def skill_3(self):
    print("Giga used Skill 3!")
    
    # Save original stats only if not already buffed
    if not hasattr(self, "original_stats"):
        self.original_stats = {
            "MaxHp": self.MaxHp,
            "Hp": self.Hp,
            "Atk": self.Atk,
            "Spd": self.Spd,
            "Accuracy": self.Accuracy
        }

    # Apply buff
    self.MaxHp *= 2
    self.Hp *= 2
    self.Atk *= 2
    self.Spd *= 2
    self.Accuracy *= 2

    # Set duration
    self.skill3_turns = 3

    print(f"{self.Name}'s stats are doubled for 4 turns!")

    return True

# Skill 3 buffs for calculating stats

def update_buffs(self):
    if hasattr(self, "skill3_turns") and self.skill3_turns > 0:
        self.skill3_turns -= 1

        if self.skill3_turns == 0:
            # Revert stats
            self.MaxHp = self.original_stats["MaxHp"]
            self.Hp = min(self.Hp, self.MaxHp)  # avoid overflow
            self.Atk = self.original_stats["Atk"]
            self.Spd = self.original_stats["Spd"]
            self.Accuracy = self.original_stats["Accuracy"]

            del self.original_stats
            print(f"{self.Name}'s stats returned to normal!")

def skill_cd (self, move):
    if move == 2:
        return 2
    if move == 3:
        return 2
    if move == 4:
        return 9
