import random

class Boxer:
    _health = 0
    _attack = 0
    _dodge = 0

    JOE = {"health": 5, "attack": 1, "dodge": 1}
    LEVEL_1_OPPONENTS = {"Paul Smith": JOE, "John May": JOE, "Henry Live": JOE}

    def __init__(self, character):
        self._character = character 
        self._assign_attributes()

    def __str__(self):
        return self._character

    def _assign_attributes(self):
        char_attr_dict = self.LEVEL_1_OPPONENTS[self._character]
        self._health = char_attr_dict["health"]
        self._attack = char_attr_dict["attack"]
        self._dodge = char_attr_dict["dodge"]
    
    def attack(self):
        return self._attack

    def take_damage(self, damage):
        if self._dodge_success():
            return "Missed!"
        self._health -= damage
        return f"{self._character} took {damage} damage."

    def _dodge_success(self):
        # Every point in dodge is 20% chance to dodge
        dodge_chance = self._dodge * 20
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_chance:
            return True
        return False

    def is_dead(self):
        return self._health <= 0