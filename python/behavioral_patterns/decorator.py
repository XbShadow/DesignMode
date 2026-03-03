
# https://www.runoob.com/design-pattern/decorator-pattern.html
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


class ShapeDecorator(metaclass=ABCMeta):
    def __init__(self, decorated_shape):
        self.decorated_shape = decorated_shape

    @abstractmethod
    def draw(self):
        self.decorated_shape.draw()


class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decorated_shape):
        super().__init__(decorated_shape)

    def draw(self):
        self.decorated_shape.draw()
        self._set_red_border()

    def _set_red_border(self):
        print("Border Color: Red")


if __name__ == '__main__':
    circle = Circle()
    red_circle = RedShapeDecorator(Circle())
    red_rectangle = RedShapeDecorator(Rectangle())

    print("Circle with normal border")
    circle.draw()

    print("Circle of red border")
    red_circle.draw()

    print("Rectangle of red border")
    red_rectangle.draw()
