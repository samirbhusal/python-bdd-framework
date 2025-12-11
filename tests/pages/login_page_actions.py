from tests.pages.base_page import BasePage
from tests.pages.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_username(self, username):
        self.type(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def validate_login_screen(self):
        actual_title = self.get_text(LoginPageLocators.LOGIN_BUTTON)
        assert actual_title == "Login", f"Login title mismatch. Expected 'Dashboard', got '{actual_title}'"