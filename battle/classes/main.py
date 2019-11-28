from classes.game import person, bcolors

magic = [{"name": "Fire", "cost": "10", "damage": "60"},
         {"name": "Thunder", "cost": "10", "damage": "60"},
         {"name": "Blizzard", "cost": "10", "damage": "60"}]


player = person(460,65,60,45,magic)
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
