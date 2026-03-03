
# https://www.runoob.com/design-pattern/visitor-pattern.html
from abc import ABCMeta, abstractmethod


class ComputerPart(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class Keyboard(ComputerPart):
    def accept(self, visitor):
        visitor.visit(self)

    def __repr__(self):
        return "Keyboard"


class Monitor(ComputerPart):
    def accept(self, visitor):
        visitor.visit(self)

    def __repr__(self):
        return "Monitor"


class Mouse(ComputerPart):
    def accept(self, visitor):
        visitor.visit(self)

    def __repr__(self):
        return "Mouse"


class Computer(ComputerPart):
    def __init__(self):
        self.parts = []
        self.parts.append(Mouse())
        self.parts.append(Monitor())
        self.parts.append(Keyboard())

    def accept(self, visitor):
        for part in self.parts:
            part.accept(visitor)
        visitor.visit(self)

    def __repr__(self):
        return "Computer"


class ComputerPartVisitor:
    def __init__(self):
        pass

    def visit(self, part):
        print(f"visit {part}")


if __name__ == '__main__':
    Computer().accept(ComputerPartVisitor())
