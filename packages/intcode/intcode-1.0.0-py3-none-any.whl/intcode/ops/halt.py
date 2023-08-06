from intcode.interfaces.base_op import BaseOp
from intcode.interpreter.state import MachineState


class HaltOp(BaseOp):
    special_parameters = ['machine_state']

    @classmethod
    def execute(cls, machine_state: MachineState) -> None:
        machine_state.halted = True
