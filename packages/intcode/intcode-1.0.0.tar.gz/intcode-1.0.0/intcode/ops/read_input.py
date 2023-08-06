from intcode.interfaces.base_op import BaseOp
from intcode.interfaces.io_handler import BaseIOHandler


class ReadInputOp(BaseOp):
    n_params = 0
    special_parameters = ['io_handler']
    returns_value = True

    @classmethod
    def execute(cls, io_handler: BaseIOHandler) -> int:
        return int(io_handler.input().strip())
