
# https://www.runoob.com/design-pattern/interpreter-pattern.html
from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, context: str) -> bool:
        pass


class TerminalExpression(Expression):
    def __init__(self, data: str):
        self.data = data

    def interpret(self, context: str) -> bool:
        return self.data in context


class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: str) -> bool:
        return self.expr1.interpret(context) or self.expr2.interpret(context)


if __name__ == '__main__':
    def get_male_expression():
        robert = TerminalExpression("Robert")
        john = TerminalExpression("John")
        return OrExpression(robert, john)

    def get_married_woman_expression():
        julie = TerminalExpression("Julie")
        married = TerminalExpression("Married")
        return OrExpression(julie, married)

    is_male = get_male_expression()
    is_married_woman = get_married_woman_expression()

    print(f"John is male? {is_male.interpret('John')}")
    print(f"Julie is a married woman? {is_married_woman.interpret('Married Julie')}")
