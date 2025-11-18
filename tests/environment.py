import os
import subprocess

import allure
from allure_commons.types import AttachmentType

from tests.core.web_platform import WebPlatform
import random

from tests.pages.common_page_actions import CommonPageActions
from tests.pages.dashboard_page_actions import DashboardPageActions
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
    context.dashboard = DashboardPageActions(context.driver)


def after_step(context, step):

    if step.status in ("failed", "error"):
        results_dir = "reports/allure-results"
        os.makedirs(results_dir, exist_ok=True)

        filename = f"{step.name.replace(' ', '_')}.png"
        screenshot_path = os.path.join(results_dir, filename)

        # Save screenshot
        try:
            context.driver.save_screenshot(screenshot_path)
            print(f"[✓] Screenshot saved: {screenshot_path}")
        except Exception as e:
            print("[✗] Screenshot NOT saved:", e)
            return

        # Attach to Allure
        try:
            with open(screenshot_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name=f"Screenshot - {step.name}",
                    attachment_type=AttachmentType.PNG
                )
        except Exception as e:
            print("[✗] Allure attachment failed:", e)

def after_all(context):
    """Cleanup after all tests"""
    context.platform.stop_driver()

    # Generate allure HTML automatically
    try:
        subprocess.call([
            "allure",
            "generate",
            "reports/allure-results",
            "-o",
            "reports/allure-report",
            "--clean"
        ])
        print("Allure HTML Report generated successfully.")
    except Exception as e:
        print("Allure report generation failed:", e)


