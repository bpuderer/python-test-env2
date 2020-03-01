"""Demo basics of using test environment"""

import logging

import pytest

from framework.config import settings
from utils.useless_utils import add_stuffs


log = logging.getLogger(__name__)

@pytest.mark.test_id(1501)
def test_settings():
    log.debug('log message from test_something1')
    assert settings['setting1'] == 'default_setting1_value'


@pytest.mark.test_id(1502)
def test_mytest():
    assert False


@pytest.mark.test_id(1503)
def test_exceptions():
    with pytest.raises(StopIteration):
        next(iter([]))

    with pytest.raises(StopIteration) as exc:
        raise StopIteration('exception text')
    assert str(exc.value) == 'exception text'

    with pytest.raises(ValueError, match=r".* 66 .*") as exc:
        raise ValueError('Order 66 executed')


@pytest.mark.test_id(1504)
def test_file_contents():
    with open('./resources/neededfile.txt') as f:
        assert f.read() == 'text in neededfile.txt\n'


class TestClass:

    @pytest.mark.test_id(1505)
    def test_within_class(self):
        assert True

    @pytest.mark.test_id(1506)
    def test_utility(self):
        assert add_stuffs('abc', 'xyz') == 'abcxyz'
