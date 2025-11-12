from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON   = (By.CLASS_NAME, "orangehrm-login-button")
