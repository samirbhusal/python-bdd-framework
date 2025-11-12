from behave import given
from tests.pages.login_page_actions import LoginPage

@given("user navigates to Orange HRM Login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load_login_page()
