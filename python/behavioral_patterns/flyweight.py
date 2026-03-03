import random
# https://www.runoob.com/design-pattern/flyweight-pattern.html
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, color: str):
        self.color = color
        self.x = 0
        self.y = 0
        self.radius = 0

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_radius(self, radius: int):
        self.radius = radius

    def draw(self):
        print(f"draw circle: ({self.x}, {self.y}, radius {self.radius}, color: {self.color})")


class ShapeFactory:
    def __init__(self):
        self.circle_map = {}

    def get_circle(self, color: str) -> Circle:
        circle = self.circle_map.get(color)
        if not circle:
            circle = Circle(color)
            self.circle_map.update({color: circle})
            print(f"Creating circle of color: {color}")
        return circle


if __name__ == '__main__':
    def random_value(limit: int):
        return int(random.random() * limit)

    def random_color():
        colors = ["Red", "Green", "Blue", "White", "Black"]
        index = random_value(len(colors))
        return colors[index]

    factory = ShapeFactory()
    for i in range(20):
        circle = factory.get_circle(random_color())
        circle.set_x(random_value(100))
        circle.set_y(random_value(100))
        circle.set_radius(100)
        circle.draw()
