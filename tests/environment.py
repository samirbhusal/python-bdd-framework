import datetime
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

    # Load userdata from behave.ini
    context.execution = context.config.userdata.get("execution", "local").lower()
    context.base_url = context.config.userdata.get("base_url")
    browser_list = context.config.userdata.get("browsers", "chrome").split(",")

    context.browsers = [b.strip() for b in browser_list]

    context.build_name = f"Samir Test Run - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def before_scenario(context, scenario):
    # Select a random browser (local only)
    context.browser = random.choice(context.browsers)

    if context.execution == "browserstack":
        context.driver = context.platform.start_browserstack_driver(
            browser_name=context.browser,
            scenario_name=scenario.name,
            build_name=context.build_name
        )
    else:
        context.driver = context.platform.start_driver(context.browser)

    context.login = LoginPage(context.driver)
    context.common = CommonPageActions(context.driver)
    context.dashboard = DashboardPageActions(context.driver)


def after_step(context, step):
    """Capture screenshot on step failure for Allure"""
    if step.status in ("failed", "error"):
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        filename = f"{step.name.replace(' ', '_')}.png"
        screenshot_path = os.path.join(screenshot_dir, filename)

        # Save screenshot
        try:
            context.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            print("Screenshot NOT saved:", e)
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
            print("Allure attachment failed:", e)


def after_scenario(context, scenario):
    """Update BrowserStack session result"""

    if context.execution != "browserstack":
        return context.driver.quit() # Skip for local execution

    try:
        status = "passed" if scenario.status == "passed" else "failed"
        reason = "Scenario executed" if status == "passed" else f"Failed: {scenario.name}"

        context.driver.execute_script(
            'browserstack_executor: {"action":"setSessionStatus", '
            f'"arguments": {{"status":"{status}", "reason":"{reason}"}} }}'
        )

    except Exception as e:
        print("BrowserStack status update failed:", e)

    try:
        context.driver.quit()
    except:
        pass


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
