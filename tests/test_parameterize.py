import logging

import pytest

from framework.config import settings
from utils.useless_utils import is_even


log = logging.getLogger(__name__)

# parameterize a fixture for multiple invocations
# https://docs.pytest.org/en/latest/fixture.html#parametrizing-fixtures
# can customize id's used for tests by adding "ids"
@pytest.fixture(params=[0, 1, 2])
#@pytest.fixture(params=[0, 1, 2], ids=['zero', 'one', 'two'])
def test_data(request):
    return request.param

def test_is_even1(test_data):
    log.debug(f'test_data: {test_data}')
    assert is_even(test_data)





# https://docs.pytest.org/en/latest/parametrize.html#parametrizing-fixtures-and-test-functions
@pytest.mark.parametrize("test_input, expected", [
                         (0, True),
                         (1, False),
                         (2, True),
                         ])
def test_is_even2(test_input, expected):
    assert is_even(test_input) == expected




# "To get all combinations of multiple parametrized arguments you can stack parametrize decorators"
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_combos(x, y):
    log.debug(f'x: {x} y: {y}')

