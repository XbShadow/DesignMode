
# https://www.runoob.com/design-pattern/iterator-pattern.html
from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class Container(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self) -> Iterator:
        pass


class NameRepository(Container):
    class NameIterator(Iterator):
        def __init__(self, names: list[str]):
            self.index = 0
            self.names = names

        def has_next(self) -> bool:
            return self.index < len(self.names)

        def next(self) -> object:
            obj = self.names[self.index]
            self.index += 1
            return obj

    def get_iterator(self) -> Iterator:
        return NameRepository.NameIterator(["Robert" , "John" ,"Julie" , "Lora"])


if __name__ == '__main__':
    name_iterator = NameRepository().get_iterator()

    while name_iterator.has_next():
        name = str(name_iterator.next())
        print(f"name is {name}")
