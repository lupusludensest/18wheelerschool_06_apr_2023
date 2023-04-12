from behave import *

@then('Login with the right credentials')
def login_with_the_right_credentials(context):
    """
    Login with the right credentials
    """
    context.app.main_page.login_with_the_right_credentials()

@then('Verify 1 "{txt}" button text is here')
def gnrl_knwldg_txt_btn(context, txt):
    """
    Verify 1 "General knowledge (continue)" button text is here
    """
    context.app.main_page.gnrl_knwldg_txt_btn(txt)

@then('Verify 2 "{txt}" button text is here')
def air_brks_txt_btn(context, txt):
    """
    Verify 2 "Air brakes" button text is here
    """
    context.app.main_page.air_brks_txt_btn(txt)

@then('Verify 3 "{txt}" button text is here')
def cmmbtn_vhcls_txt_btn(context, txt):
    """
    Verify "Combination vehicles" button text is here
    """
    context.app.main_page.cmmbtn_vhcls_txt_btn(txt)

@then('Verify 4 "{txt}" button text is here')
def eldt_hzmt_endrsmnt_txt_btn(context, txt):
    """
    Verify "ELDT Hazmat endorsement" button text is here
    """
    context.app.main_page.eldt_hzmt_endrsmnt_txt_btn(txt)

@then('Verify "{txt}" text is here')
def all_rghts_rsrvs_txt(context, txt):
    """
    Verify "© 2023. All rights reserved. text is here
    """
    context.app.main_page.all_rghts_rsrvs_txt(txt)