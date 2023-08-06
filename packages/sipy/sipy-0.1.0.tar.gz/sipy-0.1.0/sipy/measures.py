from collections import Counter
from copy import copy
import operator
from inspect import getmro
import typing
from numbers import Number

# todo generic scaling function for sharing e.g. meters?
# todo 3 add Inches
# todo 4 constants
# todo 1 tests
# todo 2 functions on complex types (prevent?)
# todo git
# todo pypi (poetry)
# todo tidy & document
# todo support for powers (meters ^ 4, meters ^ (1/2))
# todo mypy support for invalid operations?
MeasureType = typing.Union[
    typing.Type["Measure"], typing.Type["Scalar"], typing.Type["ComplexMeasure"]
]


class Measure:
    UNITS: typing.Counter[str] = Counter({})

    def __init__(self):
        self.si_value: float = 0

    def __add__(self, other: "Measure") -> "Measure":
        if not self._isinstance(other):
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )
        val = self.__class__()
        val.si_value = self.si_value + other.si_value
        return val

    def __sub__(self, other: "Measure") -> "Measure":
        if not self._isinstance(other):
            raise TypeError(
                f"unsupported operand type(s) for -: "
                f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )
        val = self.__class__()
        val.si_value = self.si_value - other.si_value
        return val

    def __mul__(self, other: typing.Union["Measure", float]) -> "Measure":
        if not isinstance(other, Measure):
            if not isinstance(other, Number):
                raise TypeError(
                    f"unsupported operand type(s) for *: "
                    f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
                )
            return self._number_mul(other)

        val = self._new_measure(other, add_counters(self.UNITS, other.UNITS))
        val.si_value = self.si_value * other.si_value
        return val

    def __rmul__(self, other: float) -> "Measure":
        if not isinstance(other, Number):
            raise TypeError(
                f"unsupported operand type(s) for *: "
                f"'{other.__class__.__name__}' and '{self.__class__.__name__}'"
            )

        return self._number_mul(other)

    def __truediv__(self, other: typing.Union["Measure", float]) -> "Measure":
        if not isinstance(other, Measure):
            if not isinstance(other, Number):
                raise TypeError(
                    f"unsupported operand type(s) for /: "
                    f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
                )
            return self._number_truediv(other)

        val = self._new_measure(other, subtract_counter(self.UNITS, other.UNITS))
        val.si_value = self.si_value / other.si_value
        return val

    def __rtruediv__(self, other: float) -> "Measure":
        if not isinstance(other, Number):
            raise TypeError(
                f"unsupported operand type(s) for /: "
                f"'{other.__class__.__name__}' and '{self.__class__.__name__}'"
            )

        inverted_units = Counter({unit: -power for unit, power in self.UNITS.items()})
        CustomMeasure = type(
            self._custom_class_name(Measure(), inverted_units),
            self.__class__.__bases__,
            {},
        )
        CustomMeasure.UNITS = inverted_units
        custom_measure = CustomMeasure()
        custom_measure.si_value = other / self.si_value
        return custom_measure

    def __str__(self) -> str:
        return f"{self.si_value:.2E}{self.unit_string}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.si_value:.2E}{self.unit_string}>"

    def __eq__(self, other: object) -> bool:
        if not self._isinstance(other):
            return False
        return self.si_value == other.si_value  # type: ignore

    def __lt__(self, other: object) -> bool:
        if not self._isinstance(other):
            raise TypeError(
                f"'<' not supported between instances of "
                f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )
        return self.si_value < other.si_value  # type: ignore

    def _isinstance(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    @property
    def unit_string(self) -> str:
        return string_from_units(self.UNITS)

    @property
    def int(self):
        return int(self.si_value)

    @property
    def float(self):
        return float(self.si_value)

    def _number_mul(self, number: float) -> "Measure":
        val = self.__class__()
        val.si_value = self.si_value * number
        return val

    def _number_truediv(self, number: float) -> "Measure":
        val = self.__class__()
        val.si_value = self.si_value / number
        return val

    def _custom_class_name(
        self, other: "Measure", combined_units: typing.Counter[str]
    ) -> str:
        """Determine the name of a class when another class is combined with this one

        :param other: The class to combine with
        :param combined_units: The units of the new class
        :return: The name of the new class
        """
        name = ""
        for unit, count in sorted(combined_units.items()):
            if count != 0:
                unit_class = find_ancestor([self, other], unit)
                if count == 1:
                    name += f"{unit_class.__name__}"
                else:
                    name += f"{unit_class.__name__}{count}"

        if not name:
            name = "Scalar"

        return name

    def _custom_class_parents(
        self, other: "Measure", combined_units: typing.Counter[str]
    ) -> typing.Tuple[MeasureType, ...]:
        parents: typing.List[MeasureType] = [ComplexMeasure]
        for unit, count in combined_units.items():
            if count != 0:
                parents.append(find_ancestor([self, other], unit))

        return tuple(parents)

    def _new_measure(
        self, other: "Measure", combined_units: typing.Counter[str]
    ) -> "Measure":
        try:
            unit = fundamental_unit(combined_units)
        except ValueError:
            class_name = self._custom_class_name(other, combined_units)
            if class_name == "Scalar":
                CustomMeasure: MeasureType = Scalar
            else:
                CustomMeasure = type(
                    self._custom_class_name(other, combined_units),
                    self._custom_class_parents(other, combined_units),
                    {},
                )
            CustomMeasure.UNITS = combined_units
            return CustomMeasure()

        fundamental_measure = find_ancestor([self, other], unit)
        return fundamental_measure()

    @property
    def ancestors(self) -> typing.Dict[str, typing.Type["Measure"]]:
        ancestors = {}
        ancestor: MeasureType
        for ancestor in getmro(self.__class__):
            if Measure in getmro(ancestor):
                try:
                    ancestor_unit: str = fundamental_unit(ancestor.UNITS)
                except ValueError:
                    continue

                ancestors[ancestor_unit] = ancestor

        return ancestors


class ComplexMeasure(Measure):
    pass


class Scalar(Measure):
    pass


def fundamental_unit(units: typing.Counter[str]) -> str:
    """Find the fundamental unit from a counter of units

    >>> fundamental_unit(Counter({"a": 1, "b": 0, "c": 0}))
    'a'
    >>> fundamental_unit(Counter({"a": 0, "b": 1, "c": 0}))
    'b'
    >>> fundamental_unit(Counter({"a": 0, "b": 0, "c": 1}))
    'c'
    >>> fundamental_unit(Counter({"a": 1, "b": 0, "c": 1}))
    Traceback (most recent call last):
     ...
    ValueError: Units are not fundamental
    >>> fundamental_unit(Counter({"a": 2, "b": 0, "c": 0}))
    Traceback (most recent call last):
     ...
    ValueError: Units are not fundamental
    >>> fundamental_unit(Counter({"a": -1, "b": 0, "c": 0}))
    Traceback (most recent call last):
     ...
    ValueError: Units are not fundamental
    >>> fundamental_unit(Counter({"a": 0, "b": 0, "c": 0}))
    Traceback (most recent call last):
     ...
    ValueError: Units are not fundamental
    """
    f_unit = None
    for unit, count in units.items():
        if count not in [0, 1]:
            raise ValueError("Units are not fundamental")
        if count == 1 and f_unit:
            raise ValueError("Units are not fundamental")
        if count == 1:
            f_unit = unit

    if f_unit is None:
        raise ValueError("Units are not fundamental")
    return f_unit


def string_from_units(units: typing.Counter[str]) -> str:
    """Construct a string from a units counter

    >>> string_from_units(Counter({"a": 1, "b": 0, "c": 0}))
    'a'
    >>> string_from_units(Counter({"a": 0, "b": 1, "c": 0}))
    'b'
    >>> string_from_units(Counter({"a": 2, "b": 0, "c": 0}))
    'a^2'
    >>> string_from_units(Counter({"a": -1, "b": 0, "c": 0}))
    'a^-1'
    >>> string_from_units(Counter({"a": 1, "b": 2, "c": 0}))
    'ab^2'
    """
    string = ""
    for unit, power in sorted(units.items()):
        if power == 1:
            string += unit
        elif power != 0:
            string += f"{unit}^{power}"
    return string


def find_ancestor(measures: typing.List[Measure], unit: str) -> typing.Type[Measure]:
    for measure in measures:
        try:
            return measure.ancestors[unit]
        except KeyError:
            pass
    else:
        raise KeyError("Ancestor not found")


def add_counters(a: typing.Counter[str], b: typing.Counter[str]) -> typing.Counter[str]:
    return _combine_counter(a, b, operator.add)


def subtract_counter(
    a: typing.Counter[str], b: typing.Counter[str]
) -> typing.Counter[str]:
    return _combine_counter(a, b, operator.sub)


def _combine_counter(
    a: typing.Counter[str], b: typing.Counter[str], operator
) -> typing.Counter[str]:
    tmp = copy(a)
    for item, value in b.items():
        tmp[item] = operator(tmp[item], value)

    return tmp
