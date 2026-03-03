
# https://www.runoob.com/design-pattern/proxy-pattern.html
from abc import ABCMeta, abstractmethod


class Image(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename

    def display(self):
        print(f"display {self.filename}")


class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        if not self.real_image:
            self.real_image = RealImage(filename=self.filename)
        self.real_image.display()


if __name__ == '__main__':
    image = ProxyImage("image.img")
    image.display()
