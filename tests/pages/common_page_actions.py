from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.base_page import BasePage


class CommonPageActions(BasePage):

    def open_base_url(self, url=""):
        uri = "https://opensource-demo.orangehrmlive.com/"
        self.driver.get(uri + url)
