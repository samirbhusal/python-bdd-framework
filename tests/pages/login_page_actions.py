from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.base_page import BasePage
from tests.pages.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_username(self, username):
        self.type(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(LoginPageLocators.PASSWORD_INPUT, password)
        self.sleep(5)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.sleep(10)
