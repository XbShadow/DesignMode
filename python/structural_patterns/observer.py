
# https://www.runoob.com/design-pattern/observer-pattern.html
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class Subject:
    def __init__(self):
        self.state = 0
        self.observers = []

    def get_state(self) -> int:
        return self.state

    def set_state(self, state: int):
        self.state = state
        self.notify()

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class BinaryObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"Binary String: {self.subject.get_state()}")


class OctalObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"OctalObserver String: {self.subject.get_state()}")


class HexaObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"HexaObserver String: {self.subject.get_state()}")


if __name__ == '__main__':
    subject = Subject()

    HexaObserver(subject)
    OctalObserver(subject)
    BinaryObserver(subject)

    print("First state change: 15")
    subject.set_state(15)

    print("Second state change: 20")
    subject.set_state(20)
