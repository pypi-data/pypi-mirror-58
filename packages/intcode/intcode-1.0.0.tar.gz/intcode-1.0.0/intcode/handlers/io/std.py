from intcode.interfaces.io_handler import BaseIOHandler


class StdIOHandler(BaseIOHandler):

    def print(self, content: str) -> None:
        print(content)

    def input(self) -> str:
        return input()
