import random

playerhp = 250
enemyatkl = 50
emenyatkh = 90

while playerhp > 0:
    damage = random.randrange(enemyatkl, emenyatkh)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strike for", damage, "points of damage. Current HP is", playerhp)

    if playerhp == 30:
        print("Go to the nearest hospital")
        break
