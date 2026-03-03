
# https://www.runoob.com/design-pattern/state-pattern.html
from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state


class State(metaclass=ABCMeta):
    @abstractmethod
    def do(self, context: Context):
        pass


class StartState(State):
    def do(self, context: Context):
        print("Player is in start state")
        context.set_state(self)

    def __repr__(self):
        return "Start State"


class StopState(State):
    def do(self, context: Context):
        print("Player is in stop state")
        context.set_state(self)

    def __repr__(self):
        return "Stop State"


if __name__ == '__main__':
    context = Context()
    start_state = StartState()
    start_state.do(context)

    stop_state = StopState()
    stop_state.do(context)

    print(context.get_state())
