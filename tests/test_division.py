import random as r

import pytest


@pytest.mark.parametrize('a, b', [
    (r.randint(0, 9), r.randint(1, 9)),
    (r.randint(0, 9), r.randint(-9, -1)),
    (r.randint(0, 9), round(r.uniform(0.001, 9.999), 3)),
    (r.randint(0, 9), round(r.uniform(-9.999, -0.001), 3))
])
def test_divide_int_positive(calc_page, a, b):
    actual = calc_page.divide(a, b)
    assert actual == round(a / b, 3), (
        'Quotient of {0} and {1} is expected to be {2} but got {3}'.format(
            a, b, round(a / b, 3), actual
        )
    )


@pytest.mark.parametrize('a, b', [
    (r.randint(-9, -1), r.randint(-9, -1)),
    (r.randint(-9, -1), round(r.uniform(0.001, 9.999), 3)),
    (r.randint(-9, -1), round(r.uniform(-9.999, -0.001), 3))
])
def test_divide_int_negative(calc_page, a, b):
    actual = calc_page.divide(a, b)
    assert actual == round(a / b, 3), (
        'Quotient of {0} and {1} is expected to be {2} but got {3}'.format(
            a, b, round(a / b, 3), actual
        )
    )


@pytest.mark.parametrize('a, b', [
    (round(r.uniform(0.001, 9.999), 3), round(r.uniform(0.001, 9.999), 3)),
    (round(r.uniform(0.001, 9.999), 3), round(r.uniform(-9.999, -0.001), 3))
])
def test_divide_float_positive(calc_page, a, b):
    actual = calc_page.divide(a, b)
    assert actual == round(a / b, 3), (
        'Quotient of {0} and {1} is expected to be {2} but got {3}'.format(
            a, b, round(a / b, 3), actual
        )
    )


@pytest.mark.parametrize('a, b', [
    (round(r.uniform(-9.999, -0.001), 3), round(r.uniform(0.001, 9.999), 3))
])
def test_divide_float_negative(calc_page, a, b):
    actual = calc_page.divide(a, b)
    assert actual == round(a / b, 3), (
        'Quotient of {0} and {1} is expected to be {2} but got {3}'.format(
            a, b, round(a / b, 3), actual
        )
    )


@pytest.mark.parametrize('a, b', [
    (r.randint(0, 9), 0),
    (r.randint(-9, -1), 0),
    (round(r.uniform(0.001, 9.999), 3), 0),
    (round(r.uniform(-9.999, -0.001), 3), 0)
])
def test_division_by_zero(calc_page, a, b):
    actual = calc_page.divide(a, b)
    assert actual == 'Infinity', (
        'Result is expected to be "Infinity" but got {}'.format(actual)
    )
