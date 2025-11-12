from selenium import webdriver

class WebPlatform:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        return self.driver

    def stop_driver(self):
        if self.driver:
            self.driver.quit()
