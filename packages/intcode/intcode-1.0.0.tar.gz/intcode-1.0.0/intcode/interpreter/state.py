from collections import defaultdict
from typing import List

from intcode.interpreter.mappings import AccessMode


class MachineState:

    def __init__(self, initial_state: List[int], machine_pointer: int = 0, relative_base: int = 0):
        self._registries = defaultdict(int)
        self._registries.update({i: state for i, state in enumerate(initial_state)})
        self.machine_pointer = machine_pointer
        self._relative_base = relative_base
        self.halted = False
        self.paused = False

    @property
    def relative_base(self) -> int:
        return self._relative_base

    @relative_base.setter
    def relative_base(self, _):
        raise ValueError("Relative base cannot be set directly")

    def shift_relative_base(self, delta: int):
        self._relative_base += delta

    def get_registry_value(self, access_mode: int, pointer: int) -> int:
        if access_mode == AccessMode.POSITION:
            return self._registries[pointer]
        elif access_mode == AccessMode.IMMEDIATE:
            return pointer
        elif access_mode == AccessMode.RELATIVE:
            return self._registries[pointer + self.relative_base]
        else:
            raise ValueError(f"Unknown access mode: '{access_mode}'")

    def set_registry_value(self, access_mode: int, registry_position: int, new_value: int) -> None:
        if access_mode == AccessMode.POSITION:
            self._registries[registry_position] = new_value
        elif access_mode == AccessMode.IMMEDIATE:
            raise Exception("WTF Access mode immediate for registry set")
        elif access_mode == AccessMode.RELATIVE:
            self._registries[registry_position + self.relative_base] = new_value
        else:
            raise ValueError(f"Unknown access mode: '{access_mode}'")

    def get_op_codes(self, n_opcodes: int = 1) -> List[int]:
        opcodes = [self._registries[self.machine_pointer + i] for i in range(n_opcodes)]
        self.machine_pointer += n_opcodes
        return opcodes

    def copy(self) -> 'MachineState':
        return MachineState([self._registries[k] for k in sorted(self._registries)], self.machine_pointer,
                            self.relative_base)

    @property
    def registries(self):
        return [self._registries[r] for r in sorted(self._registries)]
