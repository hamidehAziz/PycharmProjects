import random

class bcolors:
    HEADER = '\300[95n'
    OKBLUE = '\300[94n'
    OKGREEN = '\300[92n'
    WARNING = '\300[93n'
    FAIL ='\300[91n'
    ENDC = '\300[0n'
    BOLD = '\300[1n'
    UNDRLINE = '\300[4n'


class person:
    # constructor function with variables
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df= df
        self.magic = magic
        self.action = ["Attack", "magic"]

    # utility functions:
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)


    def generate_spell_damage(self, index):
        mgl = self.magic[index]["damage"] - 5
        mgh = self.magic[index]["damage"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self,damage):
       self.hp = self.hp - damage
       if self.hp < 0:
            self.hp = 0
       return self.hp

