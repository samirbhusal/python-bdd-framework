from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load_login_page(self, url="https://opensource-demo.orangehrmlive.com/"):
        self.driver.get(url)
