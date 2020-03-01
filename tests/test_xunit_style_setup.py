# https://docs.pytest.org/en/latest/xunit_setup.html
import logging

from framework.config import settings


log = logging.getLogger(__name__)

def setup_module():
    log.debug('setup module')

def teardown_module():
    log.debug('teardown module')

def setup_function():
    log.debug('setup function')

def teardown_function():
    log.debug('teardown function')

def test_xunit_function():
    log.debug('xunit function test')


class TestXUnitStyleSetup:

    @classmethod
    def setup_class(cls):
        log.debug('setup class')

    @classmethod
    def teardown_class(cls):
        log.debug('teardown class')

    def setup_method(self):
        log.debug('setup method')

    def teardown_method(self):
        log.debug('teardown method')

    def test_xunit_method(self):
        log.debug('xunit method test')
