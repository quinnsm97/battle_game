def attack(attacker, defender):
    damage = attacker.attack
    return defender.take_damage(damage)