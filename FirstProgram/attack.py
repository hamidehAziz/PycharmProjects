import random

class Enemy:

    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh




    def getAtk(self):
        print(self.atkl)


    def getHp(self):
         print(self.hp)

enemy1 = Enemy(40,49)
enemy1.getAtk()

enemy2 = Enemy(30, 60)
enemy2.getAtk()
enemy2.getHp()



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