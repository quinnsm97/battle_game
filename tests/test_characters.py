from game.characters import Player

def test_take_damage():
    p = Player("Test")
    assert p.take_damage(10) == 5  # 10 - 5 defense = 5 actual damage

def test_is_alive():
    p = Player("Test")
    p.take_damage(200)  # Overkill
    assert not p.is_alive()