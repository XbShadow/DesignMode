
# https://www.runoob.com/design-pattern/factory-pattern.html
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class ShapeFactory:
    def create_shape(self, shape_name=""):
        if shape_name == "circle":
            return Circle()
        if shape_name == "rectangle":
            return Rectangle()
        raise NotImplementedError(f"{shape_name} not implemented")


if __name__ == '__main__':
    factory = ShapeFactory()
    circle = factory.create_shape("circle")
    circle.draw()
    rectangle = factory.create_shape("rectangle")
    rectangle.draw()
