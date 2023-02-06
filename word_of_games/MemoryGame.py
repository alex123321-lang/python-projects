import random
import time
import re


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.seq = ""

    def generate_sequence(self):
        self.seq = " ".join(str(x) for x in [random.randint(1, 101) for x in range(1, self.difficulty + 1)])
        print(self.seq, end="")
        time.sleep(0.7)
        print("\r", end="")
        print(" " * len(self.seq), end="")
        print("\r", end="")

    def get_list_from_user(self):
        user_list = input(f"Please, insert {self.difficulty} numbers separated by one space\n")
        return re.sub(' +', ' ', user_list)

    def is_list_equal(self):
        return self.seq == self.get_list_from_user()

    def play(self):
        self.generate_sequence()
        return self.is_list_equal()


if __name__ == '__main__':
    game = MemoryGame(difficulty=2)
    print(game.play())

