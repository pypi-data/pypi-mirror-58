from collections import Counter
import typing

from sipy.measures import Measure
from sipy.units import SIUnit, Micro, Milli, Kilo


SECONDS = "s"
METERS = "m"
KILOGRAMS = "kg"
AMPERES = "A"
KELVIN = "K"
MOLES = "mol"
CANDELAS = "cd"
SI_UNITS = [SECONDS, METERS, KILOGRAMS, AMPERES, KELVIN, MOLES, CANDELAS]


def _unit_count(
    seconds: int = 0,
    meters: int = 0,
    kilograms: int = 0,
    amperes: int = 0,
    kelvin: int = 0,
    moles: int = 0,
    candelas: int = 0,
) -> typing.Counter[str]:
    return Counter(
        {
            SECONDS: seconds,
            METERS: meters,
            KILOGRAMS: kilograms,
            AMPERES: amperes,
            KELVIN: kelvin,
            MOLES: moles,
            CANDELAS: candelas,
        }
    )


class Length(Measure):
    UNITS: typing.Counter[str] = _unit_count(meters=1)
    meters = SIUnit()
    micrometers = Micro()
    millimeters = Milli()
    kilometers = Kilo()


class Time(Measure):
    UNITS: typing.Counter[str] = _unit_count(seconds=1)
    seconds = SIUnit()
    milli1seconds = Milli()


meter = Length()
meter.meters = 1

second = Time()
second.seconds = 1
