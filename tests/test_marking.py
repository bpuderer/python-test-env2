import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert False

@pytest.mark.skipif(1 == 1, reason="just demoing skipif")
def test_skipif():
    assert False

@pytest.mark.xfail
def test_expected_fail_fails():
    assert False

@pytest.mark.xfail
def test_expected_fail_passes():
    assert True

@pytest.mark.xfail(strict=True)
def test_expected_fail_fails_strict():
    assert False

@pytest.mark.xfail(strict=True)
def test_expected_fail_passes_strict():
    # will report as FAILED instead of XPASS
    # can change the default value of the strict parameter using the xfail_strict ini option
    assert True

@pytest.mark.slow
def test_slow():
    pass

@pytest.mark.reallyslow
def test_really_slow():
    pass

def test_skip_during_test():
    pytest.skip(msg="skip triggered during test execution")

def test_fail_during_test():
    pytest.fail(msg="failure triggered during test execution")

def test_expected_fail_during_test():
    pytest.xfail(reason="expected failure triggered during test execution")
