from behave import *

@then('Send wrong login "{txt}"')
def snd_wrng_lgn(context, txt):
    """
    Send wrong login "WRONG@gmail.com"
    """
    context.app.main_page.snd_wrng_lgn(txt)

@then('Send wrong password "{txt}"')
def snd_wrng_psswrd(context, txt):
    """
    Send wrong password "WRONG_GUROV"
    """
    context.app.main_page.snd_wrng_psswrd(txt)

@then('Click on Sign in button')
def click_sign_in_btn(context):
    """
    Click on Sign in button
    """
    context.app.main_page.click_sign_in_btn()

@then('Verify text "{txt}" is here')
def vrfy_txt_here_4(context, txt):
    """
    Verify text "Invalid Login or Password" is here
    """
    context.app.main_page.vrfy_txt_here_4(txt)