from abc import ABCMeta
from typing import List, Optional


class BaseOp(metaclass=ABCMeta):
    n_params = 0
    special_parameters = []
    returns_value = False
    pauses_execution = False

    @classmethod
    def execute(cls, *parameters: List[int]) -> Optional[int]:
        pass
