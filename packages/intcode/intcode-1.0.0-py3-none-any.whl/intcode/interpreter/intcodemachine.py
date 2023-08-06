from typing import Union, List, Tuple, Optional

from intcode.handlers.io.std import StdIOHandler
from intcode.interfaces.base_op import BaseOp
from intcode.interfaces.io_handler import BaseIOHandler
from intcode.interpreter.opcode_dispatcher import OpFactory
from intcode.interpreter.state import MachineState


class IntCodeMachine:
    def __init__(self,
                 program: Union[str, List[int]],
                 machine_state: Optional[MachineState] = None,
                 io_handler: Optional[BaseIOHandler] = None
                 ):
        self.machine_state = machine_state or MachineState(self._read_input_program(program))
        self._original_machine_state = self.machine_state.copy()
        self.io_handler = io_handler or StdIOHandler()

    def run(self, enable_pauses: bool = False, reset_machine_state: bool = False):
        if reset_machine_state:
            self.machine_state = self._original_machine_state.copy()
        self.machine_state.paused = False
        while not self.machine_state.halted or (enable_pauses and self.machine_state.paused):
            op, unresolved_params = self._next_op()
            self._execute_op(op, unresolved_params)

    def _next_op(self) -> Tuple[BaseOp, List[Tuple[int, int]]]:
        raw_op_code = self.machine_state.get_op_codes().pop()
        fixed_op_code = self._fix_op_code(raw_op_code)
        op = self._get_op(fixed_op_code)
        raw_params = self.machine_state.get_op_codes(op.n_params + int(op.returns_value))
        unresolved_params = list(zip([int(access_method)
                                      for access_method in fixed_op_code[:-2][::-1]],
                                     raw_params))
        return op, unresolved_params

    def _fix_op_code(self, raw_op_code: int) -> str:
        fixed_op_code = str(raw_op_code).rjust(2, '0')
        op = self._get_op(fixed_op_code)
        padded_op_code = fixed_op_code.rjust(2 + op.n_params + int(op.returns_value), '0')
        return padded_op_code

    def _get_op(self, op_code: str) -> BaseOp:
        return OpFactory.get_op(op_code[-2:])

    def _resolve_op_params(self, unresolved_op_params: List[Tuple[int, int]]) -> List[int]:
        return [self.machine_state.get_registry_value(access_mode, pointer)
                for access_mode, pointer in unresolved_op_params]

    def _execute_op(self, op: BaseOp, unresolved_params: List[Tuple[int, int]]):
        resolved_params = self._resolve_op_params(unresolved_params)
        resolved_params.pop() if op.returns_value else None
        unresolved_destination = unresolved_params.pop() if op.returns_value else None

        result = op.execute(*resolved_params, **{k: getattr(self, k) for k in op.special_parameters})

        if op.returns_value:
            self.machine_state.set_registry_value(unresolved_destination[0], unresolved_destination[1], result)
        if op.pauses_execution:
            self.machine_state.paused = True

    @staticmethod
    def _read_input_program(program: Union[str, List[int]]) -> List[int]:
        if isinstance(program, str):
            program = [int(c.strip()) for c in program.split(',') if c.strip()]
        return program
