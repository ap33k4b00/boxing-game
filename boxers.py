from urllib3 import Retry
from opponent import Boxer
from character import Character
import keyboard
import random


class Boxing:

    def __init__(self, name):
        self.name = name

    def character_fight(self, main_character, opponent):
        character = Character(main_character)
        opponents = Boxer(opponent)
        coin_toss = random.randint(0, 1)
        if coin_toss == 0:
            first, second = [character, opponents]
        else:
            first, second = [opponents, character]

        while True:
            if self.attack_character(first, second):
                return str(first)
            if self.attack_character(second, first):
                return str(second)

    def attack_character(self, first, second):
            damage = first.attack()
            second.take_damage(damage)
            if second.is_dead():
                return True
            return False

    def main(self):
        print(
            f"Welcome {self.name}, you are entering the boxing dimension, Get Ready!")
        opponent = random.choice(list(Boxer.LEVEL_1_OPPONENTS))
        character_win = 0
        opponent_win = 0
        for i in range(10):
            winner = self.character_fight(self.name, opponent)
            if winner == self.name:
                character_win += 1
            else:
                 opponent_win += 1
        print("Results")
        print(f"{self.name}: {character_win}")
        print(f"{opponent}: {opponent_win}")
        if character_win > opponent_win:
            print(f"Congratulations {self.name}, you won the match!")
        elif character_win >= opponent_win:
            print("Draw!")
        else:
            print("Unfortunately you lost!")


if __name__ == "__main__":
    print("The Boxer")
    name = input("Press Enter Your Fighter's Name: ")
    if name == "":
        name = "Random"
        game = Boxing(name)
        game.main()
    else:
        game = Boxing(name)
        game.main()