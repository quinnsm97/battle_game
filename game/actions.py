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