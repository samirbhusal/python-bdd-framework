from behave import given


@given("user navigates to Orange HRM Login page")
def navigate_login_page(context):
    context.common.open_base_url()
