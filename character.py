import random

class Character:
    _health: 0
    _attack: 0
    _dodge: 0

    def __init__(self, name):
        self.name = name
        self._set_attributes()

    def __str__(self):
        return self.name

    def _set_attributes(self):
        self._health = random.randint(1, 5)
        self._attack = random.randint(1, 5)
        self._dodge = random.randint(1, 5)

    def attack(self):
        return self._attack

    def take_damage(self, damage):
        if self._dodge_success():
            return "Missed!"
        self._health -= damage
        return f"{self.name} took {damage} damage."

    def _dodge_success(self):
        # Every point in dodge is 20% chance to dodge
        dodge_chance = self._dodge * 20
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_chance:
            return True
        return False

    def is_dead(self):
        return self._health <= 0