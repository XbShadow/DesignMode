
# https://www.runoob.com/design-pattern/memento-pattern.html


class Memento:
    def __init__(self, state: str):
        self.state = state

    def get_state(self) -> str:
        return self.state


class Originator:
    def __init__(self):
        self.state = ""

    def get_state(self) -> str:
        return self.state

    def set_state(self, state: str):
        self.state = state

    def save_state_to_memento(self):
        return Memento(self.state)

    def get_state_from_memento(self, memento: Memento):
        self.state = memento.get_state()


class CareTaker:
    def __init__(self):
        self.memento_list = []

    def add(self, memento: Memento):
        self.memento_list.append(memento)

    def get(self, index: int) -> Memento:
        return self.memento_list[index]


if __name__ == '__main__':
    originator = Originator()
    care_taker = CareTaker()
    originator.set_state("State #1")
    originator.set_state("State #2")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #3")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #4")

    print(f"current state is {originator.get_state()}")
    originator.get_state_from_memento(care_taker.get(0))
    print(f"first saved state is {originator.get_state()}")
    originator.get_state_from_memento(care_taker.get(1))
    print(f"second saved state is {originator.get_state()}")
