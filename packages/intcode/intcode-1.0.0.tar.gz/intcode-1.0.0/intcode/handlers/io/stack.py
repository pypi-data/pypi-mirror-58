from typing import Optional, List

from intcode.interfaces.io_handler import BaseIOHandler


class StackIOHandler(BaseIOHandler):
    def __init__(self, io_stack: Optional[List[str]] = None):
        self.io_stack = io_stack or []

    def print(self, content: str) -> None:
        self.io_stack.append(content)

    def input(self) -> str:
        return self.io_stack.pop()
