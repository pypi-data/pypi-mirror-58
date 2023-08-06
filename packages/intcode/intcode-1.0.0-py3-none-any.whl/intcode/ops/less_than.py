from intcode.interfaces.base_op import BaseOp


class LessThanOp(BaseOp):
    n_params = 2
    returns_value = True

    @classmethod
    def execute(cls, a: int, b: int) -> int:
        return int(a < b)
