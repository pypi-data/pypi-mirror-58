from typing import Dict, Union

from intcode.interfaces.base_op import BaseOp
from intcode.ops.addition import AdditionOp
from intcode.ops.equals import EqualsOp
from intcode.ops.halt import HaltOp
from intcode.ops.jump_if_false import JumpIfFalseOp
from intcode.ops.jump_if_true import JumpIfTrueOp
from intcode.ops.less_than import LessThanOp
from intcode.ops.multiplication import MultiplicationOp
from intcode.ops.print_value import PrintValueOp
from intcode.ops.read_input import ReadInputOp
from intcode.ops.shift_relative_base import ShiftRelativeBaseOp


class OpFactory:
    __OPCODES: Dict[int, BaseOp] = {
        1: AdditionOp,
        2: MultiplicationOp,
        3: ReadInputOp,
        4: PrintValueOp,
        5: JumpIfTrueOp,
        6: JumpIfFalseOp,
        7: LessThanOp,
        8: EqualsOp,
        9: ShiftRelativeBaseOp,
        99: HaltOp
    }

    @classmethod
    def get_op(cls, op_code: Union[int, str]) -> BaseOp:
        op_code = int(op_code)
        if op_code not in cls.__OPCODES:
            raise KeyError(f"Opcode '{op_code}' could't be found")
        return cls.__OPCODES[op_code]
