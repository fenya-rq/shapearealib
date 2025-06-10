# Shape Area Library

A Python library for calculating areas of geometric shapes with a clean, extensible interface.

## Features

- Calculate areas of circles and triangles
- Validate input parameters (positive numbers only)
- Extensible interface for custom shapes
- Type hints and comprehensive documentation
- Support for right triangle detection

## Installation

```bash
pip install shapearea
```

## Quick Start

```python
from shapearea import Circle, Triangle, get_area

# Calculate circle area
circle = Circle(2)
circle_area = get_area(circle)  # Returns 12.57

# Calculate triangle area
triangle = Triangle(3, 4, 5)
triangle_area = get_area(triangle)  # Returns 6.0

# Check if triangle is right-angled
is_right = triangle.is_rectangular_triangle()  # Returns True
```

## API Reference

### Circle

```python
circle = Circle(radius: float)
```

Creates a circle with the specified radius.

- **Parameters:**
  - `radius` (float): The radius of the circle (must be positive)
- **Returns:** Circle instance
- **Raises:**
  - `ValueError`: If radius is not positive
  - `TypeError`: If radius is not a number

### Triangle

```python
triangle = Triangle(a: float, b: float, c: float)
```

Creates a triangle with three sides.

- **Parameters:**
  - `a` (float): First side length (must be positive)
  - `b` (float): Second side length (must be positive)
  - `c` (float): Third side length (must be positive)
- **Returns:** Triangle instance
- **Raises:**
  - `ValueError`: If any side is not positive
  - `TypeError`: If any side is not a number

#### Methods

- `calculate_area()`: Returns the area of the triangle using Heron's formula
- `is_rectangular_triangle()`: Returns `True` if the triangle is right-angled

### Creating Custom Shapes

You can create your own shapes by implementing the `BaseShape` protocol:

```python
from shapearea import BaseShape

class Square:
    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        return self.side * self.side

# Usage
square = Square(3)
area = get_area(square)  # Returns 9.0
```

## Examples

### Basic Usage

```python
from shapearea import Circle, Triangle, get_area

# Circle examples
circle1 = Circle(2)
print(get_area(circle1))  # 12.57

# Triangle examples
triangle1 = Triangle(3, 4, 5)
print(get_area(triangle1))  # 6.0
print(triangle1.is_rectangular_triangle())  # True

triangle2 = Triangle(2, 3, 4)
print(get_area(triangle2))  # 2.9
print(triangle2.is_rectangular_triangle())  # False
```

### Error Handling

```python
from shapearea import Circle

try:
    circle = Circle(-1)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    circle = Circle("invalid")  # Raises TypeError
except TypeError as e:
    print(f"Error: {e}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
