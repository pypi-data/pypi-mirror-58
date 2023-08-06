from intcode.interfaces.base_op import BaseOp
from intcode.interfaces.io_handler import BaseIOHandler


class PrintValueOp(BaseOp):
    n_params = 1
    special_parameters = ['io_handler']
    pauses_execution = True

    @classmethod
    def execute(cls, a: int, io_handler: BaseIOHandler) -> None:
        io_handler.print(str(a))
