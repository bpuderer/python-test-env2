# https://docs.pytest.org/en/latest/fixture.html

import logging

import pytest

# typically all tests will use settings.  importing since that's where logger is initialized
from framework.config import settings

log = logging.getLogger(__name__)


# can move fixtures to conftest.py. automatically discovered by pytest
# fixtures can use other fixtures
# can pass autouse=True to fixture decorator to invoke automatically


# scope values: function, class, module, package or session
# function = default, package is experimental
@pytest.fixture(scope="module")
def module_fixture():
    log.debug("module fixture")
    # use yield instead of return for teardown code
    # https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code
    yield "object from module fixture"
    log.debug("module fixture teardown")


@pytest.fixture
def function_fixture(request):
    log.debug("function fixture")

    # another way of writing teardown code
    def fin():
        print('function fixture teardown')
    request.addfinalizer(fin)

    return "object from function fixture"



def test_fixture1(function_fixture, module_fixture):
    log.debug("test_fixture1")
    assert function_fixture == "object from function fixture"
    assert module_fixture == "object from module fixture"

def test_fixture2(function_fixture, module_fixture):
    log.debug("test_fixture2")
