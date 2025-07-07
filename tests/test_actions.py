from game.characters import Player
from game.actions import attack

def test_attack():
    p1 = Player("Attacker")
    p2 = Player("Defender")
    before = p2.health
    attack(p1, p2)
    assert p2.health < before  # Health must decrease after attack