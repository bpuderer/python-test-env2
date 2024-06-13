from selenium.webdriver.common.by import By
from pages.secure_area_page import SecureAreaPage

class LoginPage:

    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login button')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        return SecureAreaPage(self.driver)
