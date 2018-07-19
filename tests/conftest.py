import pytest

from pages.calculator import Calculator


@pytest.fixture(scope='session')
def calc_page(request):
    calc = Calculator()
    yield calc

    def fin():
        calc.driver.close()

    request.addfinalizer(fin)
