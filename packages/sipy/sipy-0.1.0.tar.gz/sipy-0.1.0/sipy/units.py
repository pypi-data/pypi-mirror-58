from typing import Type
from numbers import Number

from sipy.measures import Measure


class SIUnit:
    def __get__(self, instance: Measure, _: Type[Measure]) -> float:
        if instance.si_value is None:
            raise ValueError("Value Undefined")
        return self._from(instance.si_value)

    def __set__(self, instance: Measure, value: float):
        instance.si_value = self._to(value)

    def _to(self, value: float) -> float:
        return value

    def _from(self, value: float) -> float:
        return value


class Prefix(SIUnit):
    MULTIPLIER: float = 0

    def _to(self, value: float) -> float:
        return value * self.MULTIPLIER

    def _from(self, value: float) -> float:
        return value / self.MULTIPLIER


class Micro(Prefix):
    MULTIPLIER = 1e-6


class Milli(Prefix):
    MULTIPLIER = 1e-3


class Kilo(Prefix):
    MULTIPLIER = 1e3
