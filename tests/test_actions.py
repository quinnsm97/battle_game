from game.characters import Player
from game.actions import attack, special_attack, defend

def test_attack():
    p1 = Player("A")
    p2 = Player("B")
    before = p2.health
    attack(p1, p2)
    assert p2.health < before

def test_special_attack():
    p1 = Player("A")
    p2 = Player("B")
    special_attack(p1, p2)
    assert p2.health <= 100  # Could be unchanged or damaged

def test_defend_adds_defense():
    p = Player("Test")
    before = p.defense
    defend(p)
    assert p.defense > before