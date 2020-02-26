# https://docs.pytest.org/en/latest/xunit_setup.html

class TestXUnitStyleSetup:

    @classmethod
    def setup_class(cls):
        print("\nsetup_class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class")


    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("\nteardown_method")


    def test_something1(self):
        print('TEST test_something1')
        assert True

    def test_something2(self):
        print('TEST test_something2')
        assert True
