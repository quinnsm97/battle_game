import random

def attack(attacker, defender):
    damage = attacker.attack
    #critical strike logic
    if random.randint(1, 10) == 1:
        print("Critical strike!")
        damage *= 2
    return defender.take_damage(damage)

def defend(player):
    player.defense += 5

def special_attack(attacker: Character, defender: Character) -> int:
    import random
    if random.random() < 0.5:
        return defender.take_damage(attacker.attack * 2)
    else:
        print(f"{attacker.name}'s special move missed!")
        return 0