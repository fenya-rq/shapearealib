import pytest
from math import pi

from shapearea import Circle, Triangle, get_area


# === Circle tests ===
@pytest.mark.parametrize(
    'radius, expected_area',
    [
        (1, pi),
        (0.5, pi * 0.25),
        (3, pi * 9),
    ],
)
def test_circle_area(radius, expected_area):
    circle = Circle(radius)
    assert circle.calculate_area() == pytest.approx(expected_area, rel=0.1)


@pytest.mark.parametrize('radius', [0, -1, -3.5])
def test_circle_invalid_radius_raises(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize('invalid_type', ['string', None, [], {}])
def test_circle_invalid_type_raises(invalid_type):
    with pytest.raises(TypeError):
        Circle(invalid_type)


# === Triangle tests ===
@pytest.mark.parametrize(
    'sides, expected_area',
    [
        ((3, 4, 5), 6.0),
        ((5, 5, 6), 12.0),
    ],
)
def test_triangle_area(sides, expected_area):
    triangle = Triangle(*sides)
    assert triangle.calculate_area() == pytest.approx(expected_area, rel=0.1)


@pytest.mark.parametrize(
    'sides',
    [
        (0, 1, 1),
        (-1, 2, 2),
        (3, -2, 4),
        (1, 1, 0),
    ],
)
def test_triangle_invalid_sides_raises(sides):
    with pytest.raises(ValueError):
        Triangle(*sides)


@pytest.mark.parametrize(
    'invalid_type',
    [
        ('a', 1, 2),
        (None, 3, 4),
        ([1], 2, 3),
    ],
)
def test_triangle_invalid_type_raises(invalid_type):
    with pytest.raises(TypeError):
        Triangle(*invalid_type)


@pytest.mark.parametrize(
    'sides, expected_check_result',
    [
        ((3, 4, 5), True),
        ((5, 5, 6), False),
    ],
)
def test_is_rectangular_triangle(sides, expected_check_result):
    triangle = Triangle(*sides)
    assert triangle.is_rectangular_triangle() is expected_check_result
    assert triangle.is_rectangular_triangle() is expected_check_result


# === get_area tests ===
def test_get_area_with_circle_and_triangle():
    circle = Circle(2)
    triangle = Triangle(3, 4, 5)
    assert get_area(circle) == pytest.approx(pi * 4, rel=0.1)
    assert get_area(triangle) == pytest.approx(6.0, rel=0.1)


def test_get_area_with_mock_shape():
    class DummyShape:
        @staticmethod
        def calculate_area():
            return 42

    shape = DummyShape()
    assert get_area(shape) == 42
