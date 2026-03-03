
# https://www.runoob.com/design-pattern/facade-pattern.html
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")


class Circle(Shape):
    def draw(self):
        print("Shape: Circle")


class ShapeMaker:
    def __init__(self):
        self.circle_worker = Circle()
        self.rectangle_worker = Rectangle()

    def draw_circle(self):
        self.circle_worker.draw()

    def draw_rectangle(self):
        self.rectangle_worker.draw()


if __name__ == '__main__':
    shape_worker = ShapeMaker()
    shape_worker.draw_circle()
    shape_worker.draw_rectangle()
