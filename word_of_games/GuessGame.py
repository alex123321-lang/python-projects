import random


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = 0

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        number = input(f"Please, guess the number from 1 to {self.difficulty}\n")
        if not number.isdigit():
            return -1
        else:
            return int(number)

    def compare_results(self):
        return self.secret_number == self.get_guess_from_user()

    def play(self):
        self.generate_number()
        return self.compare_results()


if __name__ == '__main__':
    game = GuessGame(difficulty=2)
    print(game.play())