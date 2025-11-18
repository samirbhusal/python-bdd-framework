from behave import *


@then("user is navigated to dashboard")
def navigate_to_dashboard_page(context):
    context.dashboard.verify_dashboard_page()