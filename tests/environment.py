from tests.core.web_platform import WebPlatform
import random

from tests.pages.common_page_actions import CommonPageActions
from tests.pages.login_page_actions import LoginPage


def before_all(context):
    """Setup before all tests"""
    context.platform = WebPlatform()

    context.base_url = context.config.userdata.get("base_url")

    # Get list of browsers from behave.ini or fallback
    browser_list = "chrome,firefox"
    if hasattr(context.config, "userdata"):
        browser_list = context.config.userdata.get("browsers", browser_list)

    # Convert string to list and pick one randomly
    browsers = [b.strip() for b in browser_list.split(",")]
    selected_browser = random.choice(browsers)

    # Allow override via CLI if desired
    cli_browser = context.config.userdata.get("browser", None)
    browser = cli_browser or selected_browser

    context.driver = context.platform.start_driver(browser)


def before_scenario(context, scenario):
    context.login = LoginPage(context.driver)
    context.common = CommonPageActions(context.driver)


def after_all(context):
    """Cleanup after all tests"""
    context.platform.stop_driver()
