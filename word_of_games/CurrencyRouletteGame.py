import random
import requests
import re

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.currency = CurrencyRouletteGame.get_currency()
        self.ils = 0

    def get_money_interval(self):
        return self.ils - 5 + self.difficulty, self.ils + 5 - self.difficulty

    def get_guess_from_user(self):
        random_amount = random.randint(1, 100)
        self.ils = random_amount * self.currency
        user_guess = input(f"Guess how many ils are {random_amount} dollars\n")
        if not user_guess.isdigit() or int(user_guess) <= 0:
            return -100
        return int(user_guess)

    def play(self):
        user_guess = self.get_guess_from_user()
        lower_bound = self.get_money_interval()[0]
        upper_bound = self.get_money_interval()[1]
        lower_bound = lower_bound if lower_bound > 0 else 0
        upper_bound = upper_bound if upper_bound > 0 else 0
        return lower_bound <= user_guess <= upper_bound

    @staticmethod
    def get_currency():
        content = requests.get("https://www.x-rates.com/table/?from=USD&amount=1").content
        return float(re.search('\d+.\d+', re.search('Israeli Shekel.{200}', str(content)).group()).group())

if __name__ == '__main__':
    game = CurrencyRouletteGame(difficulty=2)
    print(game.play())
    