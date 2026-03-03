
# https://www.runoob.com/design-pattern/bridge-pattern.html
from abc import ABCMeta, abstractmethod


class DrawApi(metaclass=ABCMeta):
    @abstractmethod
    def draw_circle(self, radius: int, x: int, y: int):
        pass


class RedCircle(DrawApi):
    def draw_circle(self, radius: int, x: int, y: int):
        print(f"draw red circle {radius} ({x}, {y})")


class GreenCircle(DrawApi):
    def draw_circle(self, radius: int, x: int, y: int):
        print(f"draw green circle {radius} ({x}, {y})")


class Shape(metaclass=ABCMeta):
    def __init__(self, draw_api: DrawApi):
        self.draw_api = draw_api

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int, x: int, y: int, draw_api: DrawApi):
        super().__init__(draw_api)
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self):
        self.draw_api.draw_circle(self.radius, self.x, self.y)


if __name__ == '__main__':
    red_circle = Circle(10, 0, 0, RedCircle())
    red_circle.draw()
    green_circle = Circle(20, 10, 10, GreenCircle())
    green_circle.draw()
