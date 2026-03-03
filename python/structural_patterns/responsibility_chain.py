
# https://www.runoob.com/design-pattern/chain-of-responsibility-pattern.html
from abc import ABCMeta, abstractmethod

INFO = 1
DEBUG = 2
ERROR = 3


class AbstractLogger(metaclass=ABCMeta):
    _level = INFO
    _next_logger = None

    def set_level(self, level: int):
        self._level = level

    def set_next_logger(self, next_logger):
        self._next_logger = next_logger

    def log_massage(self, level: int, message: str):
        if self._level <= level: self.write(message)
        if self._next_logger:
            self._next_logger.log_massage(level, message)

    @abstractmethod
    def write(self, message: str):
        pass


class ConsoleLogger(AbstractLogger):
    def __init__(self, level: int):
        self._level = level

    def write(self, message: str):
        print(f"Standard Console::Logger: {message}")


class ErrorLogger(AbstractLogger):
    def __init__(self, level: int):
        self._level = level

    def write(self, message: str):
        print(f"Error Console::Logger: {message}")


class FileLogger(AbstractLogger):
    def __init__(self, level: int):
        self._level = level

    def write(self, message: str):
        print(f"File::Logger: {message}")


if __name__ == '__main__':
    def get_logger_chain():
        error_logger = ErrorLogger(ERROR)
        file_logger = FileLogger(DEBUG)
        console_logger = ConsoleLogger(INFO)
        error_logger.set_next_logger(file_logger)
        file_logger.set_next_logger(console_logger)
        return error_logger

    logger = get_logger_chain()
    logger.log_massage(INFO, "This is an information.")
    logger.log_massage(DEBUG, "This is a debug level information.")
    logger.log_massage(ERROR, "This is an error level information.")
