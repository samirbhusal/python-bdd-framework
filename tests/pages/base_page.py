from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Wait until visible
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Wait until clickable
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Click element
    def click(self, locator):
        element = self.wait_clickable(locator)
        element.click()

    # Type text
    def type(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    # Wait until present in DOM
    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Wait until invisible (spinners/loaders)
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    # Wait for text to appear
    def wait_text(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    # Open URL
    def open_url(self, url):
        self.driver.get(url)

    # General sleep (optional)
    def sleep(self, seconds):
        import time
        time.sleep(seconds)

    def get_text(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))
        return elem.text.strip()
