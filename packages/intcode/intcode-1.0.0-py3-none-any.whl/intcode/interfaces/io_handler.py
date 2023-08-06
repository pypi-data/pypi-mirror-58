from abc import ABCMeta, abstractmethod


class BaseIOHandler(metaclass=ABCMeta):

    @abstractmethod
    def print(self, content: str) -> None:
        pass

    @abstractmethod
    def input(self) -> str:
        pass
