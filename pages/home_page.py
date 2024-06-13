from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_form_authentication(self):
        self.click_link("Form Authentication")
        return LoginPage(self.driver)

    def click_link(self, link_text):
        self.driver.find_element(By.LINK_TEXT, link_text).click();
