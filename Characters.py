import random

# =====================================
# CHARACTER BASE CLASS
# =====================================

class Character:
    def __init__(self, Name, Hp, Atk, Mana, Sanity, Spd, Acc, Eff):
        self.Hp = Hp
        self.Sanity = Sanity
        self.Spd = Spd
        self.Accuracy = Acc
        self.Atk = Atk
        self.Mana = Mana
        self.Name = Name
        self.Eff = Eff

    def is_alive(self):
        return self.Hp > 0

    def has_mana(self):
        return self.Mana > 0

    def has_sanity(self):
        return self.Sanity > 0

    def is_cooldown(self, max_cd):
        if max_cd != 0:
            return f"Cooldown: {max_cd} turn(s)"
        return "Ready!"

    def damage(self, enemy):
        return enemy.Atk
