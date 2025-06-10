# Library Development Task Description

---

This document outlines the scope and key requirements for a recent development task: creating a **C# or Python library** intended for distribution to external clients.

## Description

The core functionality of the library was to perform geometric area calculations. Specifically, it needed to **calculate the area of a circle given its radius** and the **area of a triangle given its three sides**.

## Key Requirements

Beyond basic operational correctness, the evaluation of the solution focused on several critical software engineering principles:

* **Unit Tests:** Comprehensive **unit tests** were a fundamental requirement to ensure the accuracy, robustness, and reliability of all calculation methods.
* **Extensibility:** The library's architecture had to demonstrate **easy extensibility**, allowing for the straightforward addition of new geometric shapes and their area calculation methods in the future.
* **Compile-time Type Agnosticism:** A pivotal aspect was the ability to **compute a shape's area without prior knowledge of its specific type at compile-time**. This emphasized the application of polymorphism and flexible design patterns.
* **Right Triangle Check:** An additional feature involved implementing a dedicated method to **verify if a given triangle is a right-angled triangle**.

This task served as a comprehensive assessment of problem-solving abilities, adherence to best practices such as test-driven development, architectural design for scalability, and advanced type handling.

___

# Shape Area Library

A Python library for calculating areas of geometric shapes with a clean, extensible interface.

## Features

- Calculate areas of circles and triangles
- Validate input parameters (positive numbers only)
- Extensible interface for custom shapes
- Type hints and comprehensive documentation
- Support for right triangle detection

## Installation

This project serves as a small, straightforward library developed for an employer evaluation task and is not intended for general distribution on PyPI. Therefore, the installation process differs from a typical public package.

### 1. Clone the Repository

First, you'll need to clone the project's source code from GitHub to your local machine:

```bash
git clone https://github.com/fenya-rq/shapearealib.git
cd shapearealib
```

### 2. Install Poetry and Build the Package

This project uses [Poetry](https://python-poetry.org/) for dependency management and building. If you don't already have it, you can find installation instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Once Poetry is set up, navigate to the root directory of the cloned project (the one containing `pyproject.toml`) and run the build command:

```bash
poetry build
```

### 3. Install the Library

This command will create the distributable files (`.whl` and `.tar.gz`) inside a new `dist/` directory within your project folder.

After building, you can install the library into your Python environment. It's always a good practice to work within a virtual environment for your projects.

#### For Development (Editable Install)

If you plan to actively develop the library or make changes that you want to instantly see reflected in another project using it, an editable install is best. This creates a link to the source code, so updates are immediate.

From the root of your consuming project's virtual environment:

```bash
pip install -e /path/to/shapearealib/
```

#### For General Use (from `.whl` file)

If you prefer to install a stable, pre-built version of the library (without direct source linking), you can install the wheel file.

From the root of your consuming project's virtual environment:

```bash
pip install /path/to/shapearealib/dist/shape_area_lib-0.1.0-py3-none-any.whl
```

### Using Poetry in your Consuming Project

If the project where you want to use this library is also managed by Poetry, you can add it as a local dependency using `poetry add`:

#### For an editable install (recommended for development):

```bash
poetry add --editable /path/to/shapearealib/
```

#### OR for a non-editable install from the wheel file:

```bash
poetry add /path/to/shapearealib/dist/shape_area_lib-0.1.0-py3-none-any.whl
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
