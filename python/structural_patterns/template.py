
# https://www.runoob.com/design-pattern/template-pattern.html
from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    def play(self):
        self.initialize()
        self.start()
        self.end()


class Cricket(Game):
    def end(self):
        print("Cricket Game Finished!")

    def start(self):
        print("Cricket Game Started. Enjoy the game!")

    def initialize(self):
        print("Cricket Game Initialized! Start playing.")


class Football(Game):
    def end(self):
        print("Football Game Finished!")

    def start(self):
        print("Football Game Started. Enjoy the game!")

    def initialize(self):
        print("Football Game Initialized! Start playing.")


if __name__ == '__main__':
    Cricket().play()
    Football().play()
