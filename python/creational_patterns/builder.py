
# https://www.runoob.com/design-pattern/builder-pattern.html
from abc import ABCMeta, abstractmethod


class House(object):
    def __init__(self, door=None, windows=None, rooms=None):
        self.door = door
        self.windows = windows
        self.rooms = rooms


class BaseBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_door(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_rooms(self):
        pass


class BaseHouseBuilder(BaseBuilder):
    def __init__(self):
        self.house = House()

    def build_door(self):
        self.house.door = 1

    def build_rooms(self):
        self.house.rooms = 1

    def build_windows(self):
        self.house.windows = 1


class BigHouseBuilder(BaseBuilder):
    def __init__(self):
        self.house = House()

    def build_door(self):
        self.house.door = 3

    def build_rooms(self):
        self.house.rooms = 3

    def build_windows(self):
        self.house.windows = 3


class HouseBuildDirector:
    def build_house(self, builder):
        builder.build_door()
        builder.build_windows()
        builder.build_rooms()
        return builder.house


if __name__ == '__main__':
    base_builder = BaseHouseBuilder()
    big_house_builder = BigHouseBuilder()
    director = HouseBuildDirector()

    base_house = director.build_house(base_builder)
    print(base_house.rooms)
    big_house = director.build_house(big_house_builder)
    print(big_house.rooms)
