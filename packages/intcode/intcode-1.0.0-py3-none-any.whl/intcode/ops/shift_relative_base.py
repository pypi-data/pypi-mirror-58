from intcode.interfaces.base_op import BaseOp
from intcode.interpreter.state import MachineState


class ShiftRelativeBaseOp(BaseOp):
    n_params = 1
    special_parameters = ['machine_state']

    @classmethod
    def execute(cls, a: int, machine_state: MachineState) -> None:
        machine_state.shift_relative_base(a)
