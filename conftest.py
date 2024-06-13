import pytest
from selenium import webdriver
from pages.home_page import HomePage
# https://docs.pytest.org/en/latest/usage.html

def pytest_collection_modifyitems(session, config, items):
    for item in items:
        for marker in item.iter_markers(name="test_id"):
            test_id = marker.args[0]
            item.user_properties.append(("test_id", test_id))


@pytest.fixture
def home_page():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    driver.implicitly_wait(10)
    yield HomePage(driver)
    driver.quit()
