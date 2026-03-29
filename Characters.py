import random


class Character:

    def __init__(self, Name, Hp, Atk, Mana, Sanity, Spd, Acc, Eff):
        self.Name = Name
        self.Hp = Hp
        self.MaxHp = Hp
        self.Atk = Atk
        self.Mana = Mana
        self.Sanity = Sanity
        self.Spd = Spd
        self.Accuracy = Acc
        self.Eff = Eff

        self.Form = "normal"
        self.turn_counter = 0

        self.buffs = {}
        self.debuffs = {}

        self.skills = {}
        self.cooldowns = {}

    def is_alive(self):
        return self.Hp > 0

    def use_skill(self, move, enemy):

        if self.cooldowns.get(move, 0) > 0:
            print("Skill is on cooldown!")
            return True

        result = self.skills[move](enemy)

        self.cooldowns[move] = self.get_skill_cd(move)

        return result

    def reduce_cooldowns(self):
        for k in self.cooldowns:
            self.cooldowns[k] = max(self.cooldowns[k] - 1, 0)

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

    def get_skill_cd(self, move):
        return 0

    def debuff_checker(self, move, enemy):
        if self.has_debuff("Sabotage") and move != 1:
            print("You are sabotaged! Only Basic Attack allowed!")
            return 1
        if self.has_debuff("Poison"):
            enemy.take_damage(5 , enemy)
        return move




    def check_hit(self, enemy):
        r = random.random()
        chance = self.Accuracy / (enemy.Spd + self.Accuracy)
        if chance >= r:
            return True
        else:
            return False