
# https://www.runoob.com/design-pattern/strategy-pattern.html
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def do(self, num1: int, num2: int) -> int:
        pass


class OperationAdd(Strategy):
    def do(self, num1: int, num2: int):
        return num1 + num2


class OperationSubtract(Strategy):
    def do(self, num1: int, num2: int):
        return num1 - num2


class OperationMultiply(Strategy):
    def do(self, num1: int, num2: int):
        return num1 * num2


class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def execute(self, num1: int, num2: int) -> int:
        return self.strategy.do(num1, num2)


if __name__ == '__main__':
    context = Context(OperationAdd())
    print(f"10 + 5 = {context.execute(10, 5)}")

    context = Context(OperationSubtract())
    print(f"10 - 5 = {context.execute(10, 5)}")

    context = Context(OperationMultiply())
    print(f"10 * 5 = {context.execute(10, 5)}")
