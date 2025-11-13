from behave import given

from tests.pages.common_page_actions import CommonPageActions


@given("user navigates to Orange HRM Login page")
def navigate_login_page(context):
    context.common.open_base_url()
