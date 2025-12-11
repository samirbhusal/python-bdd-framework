from behave import *


@step("user is navigated to dashboard")
def navigate_to_dashboard_page(context):
    context.dashboard.verify_dashboard_page()

@step("user click the log out button")
def click_logout_button(context):
    context.dashboard.click_logout_button()