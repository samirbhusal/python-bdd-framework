from behave import *


@step('user enters username as {username}')
def enter_username(context, username):
    context.login.enter_username(username)


@step('user enters password as {password}')
def enter_password(context, password):
    context.login.enter_password(password)

@step("user clicks the login button")
def click_login_button(context):
    context.login.click_login()

@step("user validates login screen")
def validate_login_screen(context):
    context.login.validate_login_screen()