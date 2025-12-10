import os
import random

from selenium import webdriver

class WebPlatform:
    def __init__(self):
        self.driver = None

    def get_browser_options(self, browser_name):
        browser_name = browser_name.lower()

        if browser_name == "chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_argument("--start-maximized")
            return options

        elif browser_name == "firefox":
            from selenium.webdriver.firefox.options import Options
            options = Options()
            return options

        elif browser_name == "edge":
            from selenium.webdriver.edge.options import Options
            options = Options()
            options.add_argument("--start-maximized")
            return options

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    def start_driver(self, browser_name=None):

        browser = (browser_name or os.getenv("BROWSER", "chrome")).lower()
        print(f"➡ Launching {browser.capitalize()} browser...")

        options = self.get_browser_options(browser_name)

        # Mapping browser names → WebDriver classes
        driver_map = {
            "chrome": webdriver.Chrome,
            "firefox": webdriver.Firefox,
            "edge": webdriver.Edge,
            "safari": webdriver.Safari
        }

        if browser_name not in driver_map:
            raise ValueError(f"Unsupported browser: {browser_name}")

        # Safari does not accept "options"
        if browser_name == "safari":
            self.driver = driver_map[browser_name]()
        else:
            self.driver = driver_map[browser_name](options=options)

        self.driver.implicitly_wait(10)
        return self.driver

    def start_browserstack_driver(self, browser_name, scenario_name, build_name):
        print("➡ Initializing BrowserStack WebDriver...")

        username = os.getenv("BROWSERSTACK_USERNAME")
        access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

        if not username or not access_key:
            raise RuntimeError("Missing BrowserStack credentials!")

        remote_url = f"https://{username}:{access_key}@hub.browserstack.com/wd/hub"

        # normalize browser name
        browser_name = browser_name.lower().strip()
        options = self.get_browser_options(browser_name)

        # Browser capabilities
        options.set_capability("browserName", browser_name)
        options.set_capability("browserVersion", "latest")

        # OS Matrix (Safari allowed only on macOS)
        if browser_name == "safari":
            os_matrix = [
                {"os": "OS X", "osVersion": "Monterey"},
                {"os": "OS X", "osVersion": "Ventura"},
            ]
        else:
            os_matrix = [
                {"os": "Windows", "osVersion": "11", "browser": "chrome"},
                {"os": "Windows", "osVersion": "10", "browser": "firefox"},
                {"os": "OS X", "osVersion": "Ventura", "browser": "safari"},
                {"os": "OS X", "osVersion": "Monterey", "browser": "chrome"},
            ]

        selected_os = random.choice(os_matrix)

        # BrowserStack options
        bstack_options = {
            "os": selected_os["os"],
            "osVersion": selected_os["osVersion"],
            "buildName": build_name,
            "sessionName": scenario_name,
            "seleniumVersion": "4.22.0",
            "local": "false"
        }

        options.set_capability("bstack:options", bstack_options)

        # Initialize Remote driver
        self.driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )
        return self.driver

    def stop_driver(self):
        if self.driver:
            self.driver.quit()
