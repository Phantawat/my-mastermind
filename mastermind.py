import random


class Mastermind:
    def __init__(self, x, y):
        self.__colors = x
        self.__positions = y
        self.sample = self.generate_sample()

    @property
    def colors(self):
        return self.__colors

    @colors.setter
    def colors(self, x):
        self.__colors = x

    @property
    def positions(self):
        return self.__positions

    @positions.setter
    def positions(self, y):
        self.__positions = y

    def generate_sample(self):
        sample = ''
        for i in range(1, 5):
            sample += str(random.randint(1, 8))
        return sample

    def play(self):
        print(f'Playing Mastermind with {self.__colors} colors and {self.__positions} positions')
        self.guess = input('What is your guess?: ')
        while True:
            hint = self.check_ans()
            print(f'Your guess is {self.guess}')
            print(hint)
            print(self.sample)
            if hint == '*' * self.__positions:
                break
            self.guess = input('What is your guess?: ')

    def check_ans(self):
        hint = ''
        for j, i in enumerate(self.sample):
            if self.guess[j] == self.sample[j]:
                hint += '*'
            elif self.guess[j] in self.sample:
                hint += 'o'
        return hint


if __name__ == '__main__':
    mastermind = Mastermind(6, 4)
    mastermind.play()

