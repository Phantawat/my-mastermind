import random


class Mastermind:
    def __init__(self, x, y):
        self.__colors = x
        self.__positions = y
        self.sample = self.generate_sample()
        self.attempt = 1

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
        for i in range(1, self.__positions + 1):
            sample += str(random.randint(1, self.__colors))
        return sample

    def play(self):
        print(f'Playing Mastermind with {self.__colors} colors and {self.__positions} positions')
        self.guess = input('What is your guess?: ')
        while True:
            hint = self.check_ans()
            print(f'Your guess is {self.guess}')
            print(hint)
            if hint == '*' * self.__positions:
                break
            self.attempt += 1
            self.guess = input('What is your guess?: ')
        print(f'You solve it after {self.attempt} rounds')
        print('Congrats, you are clever as Conan!')

    def check_ans(self):
        hint1 = ''
        hint2 = ''
        temp_sample = self.sample

        for j, i in enumerate(self.sample):
            if self.guess[j] == i:
                hint1 += '*'
                temp_sample = temp_sample[:j] + '.' + temp_sample[j + 1:]
            elif self.guess[j] in temp_sample:
                hint2 += 'o'
                temp_sample = temp_sample.replace(self.guess[j], '.', 1)

        return hint1 + hint2


if __name__ == '__main__':
    while True:
        mastermind = Mastermind(6, 4)
        mastermind.play()
        con_or_pause = int(input('Press 1 if you wanna play again 0 to quit: '))
        if con_or_pause == 0:
            break
