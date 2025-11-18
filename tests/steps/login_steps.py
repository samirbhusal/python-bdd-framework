from behave import *


@given('user enters username as {username}')
def enter_username(context, username):
    context.login.enter_username(username)


@when('user enters password as {password}')
def enter_password(context, password):
    context.login.enter_password(password)

@when("user clicks the login button")
def click_login_button(context):
    context.login.click_login()