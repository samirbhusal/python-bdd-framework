import os
from selenium import webdriver

class WebPlatform:
    def __init__(self):
        self.driver = None

    def start_driver(self, browser_name=None):

        browser = (browser_name or os.getenv("BROWSER", "chrome")).lower()
        print(f"➡ Launching {browser.capitalize()} browser...")

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(options=options)

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Edge(options=options)

        elif browser == "safari":
            self.driver = webdriver.Safari()  # macOS only

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.driver.implicitly_wait(10)
        return self.driver

    def stop_driver(self):
        if self.driver:
            self.driver.quit()
