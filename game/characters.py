class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        reduced = max(0, damage - self.defense)
        self.health -= reduced
        return reduced

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: HP={self.health}, ATK={self.attack}, DEF={self.defense}"

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15, 5)