
# https://www.runoob.com/design-pattern/command-pattern.html
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class Stock:
    def __init__(self, name="ABC", quantity=10):
        self.name = name
        self.quantity = quantity

    def buy(self):
        print(f"buy stock {self.name} quantity {self.quantity}")

    def sell(self):
        print(f"sell stock {self.name} quantity {self.quantity}")


class BuyStock(Order):
    def __init__(self, stock: Stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStock(Order):
    def __init__(self, stock: Stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class Broker:
    def __init__(self):
        self.order_list = []

    def add_order(self, order: Order):
        self.order_list.append(order)

    def place_order(self):
        for order in self.order_list:
            order.execute()
        self.order_list.clear()


if __name__ == '__main__':
    stock = Stock()
    buy_stock_order = BuyStock(stock)
    sell_stock_order = SellStock(stock)

    broker = Broker()
    broker.add_order(buy_stock_order)
    broker.add_order(sell_stock_order)

    broker.place_order()
