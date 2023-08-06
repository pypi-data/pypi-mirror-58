from fractions import Fraction
from typing import Tuple, List, Iterable
from math import gcd
from sympy.ntheory.factor_ import divisors
from functools import reduce


def lcm(number1: int, number2: int) -> int:
    return (number1 * number2) // gcd(number1, number2)


def lcd2(fraction1: Fraction, fraction2: Fraction) -> Fraction:
    return Fraction(1, lcm(fraction1.denominator, fraction2.denominator))


def lcd(fractions: Iterable):
    return reduce(lcd2, fractions)


def get_divisors(number: int):
    return divisors(number, generator=True)


class Vector:
    value: tuple
    length: int

    def __init__(self, *values):
        self.value = tuple(values)
        self.length = len(self.value)

    def __len__(self) -> int:
        return self.length

    def __add__(self, other: "Vector"):
        if len(self) != len(other):
            raise TypeError('Vectors have incompatible lengths')
        return Vector(
            *tuple([self.value[i] + other.value[i] for i in range(len(self))])
        )

    def __str__(self):
        return f'Vector({self.value})'

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other: "Vector"):
        return self.value == other.value

    def __iter__(self):
        return (x for x in self.value)

    def __mul__(self, other):
        return Vector(self.value[i] * other for i in range(len(self)))


class Vector2Int(Vector):
    value: Tuple[int, int]
    _angle: Fraction = None

    @property
    def x(self) -> int:
        return self.value[0]

    @property
    def y(self) -> int:
        return self.value[1]

    @property
    def angle(self) -> Fraction:
        if not self._angle:
            if self.x == 0:
                self._angle = Fraction(0, 1)
            else:
                self._angle = Fraction(self.y, self.x)
        return self._angle

    def __add__(self, other: "Vector2Int"):
        return Vector2Int(
            self.x + other.x,
            self.y + other.y
        )

    def __mul__(self, other):
        return Vector2Int(
            self.x * other,
            self.y * other
        )


class GridCrawler:
    directions: List[tuple] = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    def __init__(self, location: Vector2Int, direction: Vector2Int):
        self.location = location
        self.direction = direction

    def turn_right(self):
        index = self.directions.index(self.direction)
        index = (index + 1) % 4
        self.direction = self.directions[index]

    def turn_left(self):
        index = self.directions.index(self.direction)
        index = (index + 3) % 4
        self.direction = self.directions[index]

    def turn_back(self):
        index = self.directions.index(self.direction)
        index = (index + 2) % 4
        self.direction = self.directions[index]
