
# https://www.runoob.com/design-pattern/abstract-factory-pattern.html
from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_shape(self, shape_name=""):
        pass

    @abstractmethod
    def get_color(self, color_name):
        pass


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


class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_name=""):
        if shape_name == "circle":
            return Circle()
        if shape_name == "rectangle":
            return Rectangle()
        raise NotImplementedError(f"{shape_name} not implemented")

    def get_color(self, color_name):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def fill(self):
        pass


class Red(Color):
    def fill(self):
        print("fill red color")


class Green(Color):
    def fill(self):
        print("fill green color")


class ColorFactory(AbstractFactory):
    def get_color(self, color_name):
        if color_name == "red": return Red()
        if color_name == "green": return Green()
        raise NotImplementedError(f"{color_name} color not implemented")

    def get_shape(self, shape_name=""):
        pass

class FactoryProducer:
    def create_factory(self, factory_name):
        if factory_name == "shape": return ShapeFactory()
        if factory_name == "color": return ColorFactory()
        raise NotImplementedError(f"{factory_name} factory not implemented")


if __name__ == '__main__':
    shape_factory = FactoryProducer().create_factory("shape")
    shape = shape_factory.get_shape("circle")
    shape.draw()

    color_factory = FactoryProducer().create_factory("color")
    color = color_factory.get_color("red")
    color.fill()
