
# https://www.runoob.com/design-pattern/prototype-pattern.html

from abc import ABCMeta, abstractmethod
import copy


class PrototypeShape(metaclass=ABCMeta):
    def __init__(self, shape_id="", shape_type=""):
        self.shape_id = shape_id
        self.shape_tyoe = shape_type

    def get_shape_id(self):
        return self.shape_id

    def get_shape_type(self):
        return self.shape_tyoe

    def set_shape_id(self, shape_id):
        self.shape_id = shape_id

    @abstractmethod
    def draw(self):
        pass


class Circle(PrototypeShape):
    def __init__(self):
        super().__init__(shape_type="circle")

    def draw(self):
        print("draw circle")


class Angle(PrototypeShape):
    def __init__(self):
        super().__init__(shape_type="angle")

    def draw(self):
        print("draw angle")


class ShapeCache:
    def __init__(self):
        self.shape_map = dict()

    def load_cache(self):
        circle = Circle()
        circle.set_shape_id("1")
        self.shape_map[circle.get_shape_id()] = circle
        angle = Angle()
        angle.set_shape_id("2")
        self.shape_map[angle.get_shape_id()] = angle

    def get_shape(self, shape_id):
        return copy.deepcopy(self.shape_map[shape_id])


if __name__ == '__main__':
    cache = ShapeCache()
    cache.load_cache()
    circle = cache.get_shape("1")
    angle = cache.get_shape("2")
    print(circle.get_shape_id())
    print(angle.get_shape_id())
