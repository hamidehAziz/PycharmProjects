#import random
from Classes.enemy import Enemy

enemy1 = Enemy(200,49)
enemy1.getHp()

enemy2 = Enemy(400, 60)
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