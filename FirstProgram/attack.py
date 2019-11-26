import random

class Enemy:
    atkl = 30
    atkh = 90

    def getAtk(self):
        print(self.atkl)


enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()

'''
    playerhp = 250
    enemyatkl = 50
    emenyatkh = 90

while playerhp > 0:
    damage = random.randrange(enemyatkl, emenyatkh)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strike for", damage, "points of damage. Current HP is", playerhp)

    if playerhp > 30:
        continue

    print("Go to the nearest hospital")
    break
'''