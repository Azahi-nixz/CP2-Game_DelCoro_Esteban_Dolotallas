class Character:

    def __init__(self, Name, Hp, Atk, Mana, Sanity, Spd, Acc, Eff):

        self.Name = Name
        self.Hp = Hp
        self.Atk = Atk
        self.Mana = Mana
        self.Sanity = Sanity
        self.Spd = Spd
        self.Accuracy = Acc
        self.Eff = Eff

        self.Form = "normal"

        # status effects
        self.buffs = {}
        self.debuffs = {}

    def is_alive(self):
        return self.Hp > 0

    def has_mana(self):
        return self.Mana > 0

    def has_sanity(self):
        return self.Sanity > 0


    # ==========================
    # BUFF / DEBUFF MANAGEMENT
    # ==========================

    def add_buff(self, name, duration):
        self.buffs[name] = duration
        print(f"{self.Name} gained buff: {name} ({duration} turns)")

    def add_debuff(self, name, duration):
        self.debuffs[name] = duration
        print(f"{self.Name} received debuff: {name} ({duration} turns)")


    def reduce_effects(self):

        expired = []

        for buff in self.buffs:
            self.buffs[buff] -= 1
            if self.buffs[buff] <= 0:
                expired.append(buff)

        for buff in expired:
            del self.buffs[buff]
            print(f"{self.Name}'s {buff} buff expired")

        expired = []

        for debuff in self.debuffs:
            self.debuffs[debuff] -= 1
            if self.debuffs[debuff] <= 0:
                expired.append(debuff)

        for debuff in expired:
            del self.debuffs[debuff]
            print(f"{self.Name}'s {debuff} debuff expired")


    def has_debuff(self, name):
        return name in self.debuffs

    def has_buff(self, name):
        return name in self.buffs


    def status(self):
        return f"Buffs: {list(self.buffs.keys())} | Debuffs: {list(self.debuffs.keys())}"


    def is_cooldown(self, cd):
        if cd != 0:
            return f"Cooldown: {cd}"
        return "Ready!"