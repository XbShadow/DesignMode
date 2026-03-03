
# https://www.runoob.com/design-pattern/mediator-pattern.html


class ChatRoom:
    @staticmethod
    def show_message(user, message):
        print(f"[{user.get_name()}] {message}")


class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def send_message(self, message: str):
        ChatRoom.show_message(self, message)


if __name__ == '__main__':
    robert = User("Robert")
    john = User("John")

    robert.send_message("Hi! John!")
    john.send_message("Hi! Robert!")
