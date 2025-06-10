"""
Geometry library for computing areas of geometric shapes.

Supports circles and triangles by default. Easily extensible
to other shapes via the BaseShape protocol interface.

Shapes must implement a `calculate_area()` method.

Example:
    >>> from geometry import Circle, Triangle, get_area
    >>> circle = Circle(2)
    >>> triangle = Triangle(3, 4, 5)
    >>> get_area(circle)
    12.56
    >>> get_area(triangle)
    6.0

Each shape validates that all dimensions are positive numbers.

Custom shapes can be added by implementing `calculate_area()`:

Example:
    >>> class Square:
    ...     def __init__(self, side):
    ...         self.side = side
    ...
    ...     def calculate_area(self):
    ...         return self.side * self.side
    >>> square = Square(3)
    >>> get_area(square)
    9
"""

from math import pi, sqrt
from typing import Protocol

from shapearea.validators import PositiveNumber


class BaseShape(Protocol):
    """
    Interface for geometric shapes that can calculate area.
    """

    def calculate_area(self) -> float:
        """
        Compute the area of a geometric shape.

        :returns: The area as a float.
        """
        ...


class Circle:
    __slots__ = ('radius', '__pi')

    def __init__(self, radius: float) -> None:
        """
        Initialize a circle with a given radius.

        :param radius: Radius of the circle.
        :raises ValueError: If radius is not positive.
        """
        self.radius = PositiveNumber.validate(radius)
        self.__pi = pi

    def __setattr__(self, name, value) -> None:
        if name == 'radius':
            value = PositiveNumber.validate(value)
        super().__setattr__(name, value)

    def calculate_area(self) -> float:
        """
        Compute the area of the circle.

        :returns: Area as a float.
        """
        return round(self.__pi * (self.radius**2), 2)


class Triangle:
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initialize a triangle with three sides.

        :param a: First side.
        :param b: Second side.
        :param c: Third side.
        :raises ValueError: If any side is not positive.
        """
        self.a = PositiveNumber.validate(a)
        self.b = PositiveNumber.validate(b)
        self.c = PositiveNumber.validate(c)

    def __setattr__(self, name, value) -> None:
        if name in ('a', 'b', 'c'):
            value = PositiveNumber.validate(value)
        super().__setattr__(name, value)

    def calculate_area(self) -> float:
        """
        Compute the area using Heron's formula.

        :returns: Area as a float, rounded to 2 decimals.
        """
        p = (self.a + self.b + self.c) / 2
        square = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return round(square, 2)


def get_area(shape: BaseShape) -> float:
    """
    Compute the area of any shape implementing BaseShape.

    :param shape: An instance implementing BaseShape.
    :returns: Area of the shape as a float.
    """
    return shape.calculate_area()
