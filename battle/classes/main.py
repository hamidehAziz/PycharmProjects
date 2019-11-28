from classes.game import person, bcolors

magic = [{"name": "Fire", "cost": 10, "damage": 60},
         {"name": "Thunder", "cost": 10, "damage": 80},
         {"name": "Blizzard", "cost": 10, "damage": 70}]


player = person(460,65,60,45,magic)
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
