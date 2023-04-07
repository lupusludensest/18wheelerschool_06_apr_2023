from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then('Verify text 1 "{txt}" is here')
def vrfy_txt_here(context, txt):
    """
    Verify text 1 "Please sign in" is here
    """
    context.app.main_page.vrfy_txt_here(txt)

@then('Send correct login "{txt}"')
def send_login(context, txt):
    """
    Send correct login "gurovvic@gmail.com"
    """
    context.app.main_page.send_login(txt)

@then('Send correct password "{txt}"')
def send_password(context, txt):
    """
    Send correct password "QWERTY_GUROV"
    """
    context.app.main_page.send_password(txt)

@then('Click on "Sign in" button')
def click_sign_in_btn(context):
    """
    Click on "Sign in" button
    """
    context.app.main_page.click_sign_in_btn()

@then('Verify text 2 "{txt}" is here')
def vrfy_txt_here_2(context, txt):
    """
    Verify text 2 "Start your test" is here
    """
    context.app.main_page.vrfy_txt_here_2(txt)

@then('Verify username "{txt}" is here')
def vrf_username_here(context, txt):
    """
    Verify username "gurovvic@gmail.com" is here
    """
    context.app.main_page.vrf_username_here(txt)