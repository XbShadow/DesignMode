
# https://www.runoob.com/design-pattern/null-object-pattern.html
from abc import ABCMeta, abstractmethod


class AbstractCustomer(metaclass=ABCMeta):
    _name = ""

    @abstractmethod
    def is_null(self) -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class RealCustomer(AbstractCustomer):
    def __init__(self, name):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def is_null(self) -> bool:
        return False


class NullCustomer(AbstractCustomer):
    def get_name(self) -> str:
        return "Not Available in Customer Database"

    def is_null(self) -> bool:
        return True


class CustomerFactory:
    _NAMES = ["Rob", "Joe", "Julie"]

    @staticmethod
    def get_customer(name: str):
        for _name in CustomerFactory._NAMES:
            if _name == name:
                return RealCustomer(name)
        return NullCustomer()


if __name__ == '__main__':
    customer1 = CustomerFactory.get_customer("Rob")
    customer2 = CustomerFactory.get_customer("Bob")
    customer3 = CustomerFactory.get_customer("Julie")
    customer4 = CustomerFactory.get_customer("Laura")

    print("Customers")
    print(customer1.get_name())
    print(customer2.get_name())
    print(customer3.get_name())
    print(customer4.get_name())
