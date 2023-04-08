from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import time

# Locators
TEXT_IS_HERE_1 = (By.XPATH, "//h1[@class='h3 mb-3 fw-normal']")
LGN_FLD = (By.ID, "username")
PSSWRD_FLD = (By.ID, "password")
SGN_IN_BTN = (By.XPATH, "//button[@class='w-100 btn btn-lg btn-primary']")
LOGIN = "gurovvic@gmail.com"
PSSWRD = "QWERTY_GUROV"
TEXT_IS_HERE_2 = (By.XPATH, "//h1[@class='m-3']")
TEXT_IS_HERE_3 = (By.XPATH, "//span[@class='px-3']")
TEXT_IS_HERE_4 = TEXT_IS_HERE_1
INVLD_LGN_OR_PSWRD_TXT = (By.XPATH, "//ul[@class='mb-0']")
# GNRL_KNWLDG_TXT_BTN = (By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[1]")
GNRL_KNWLDG_TXT_BTN = (By.XPATH, "//a[text()='General knowledge (continue)']")
AIR_BRKS_TXT_BTN = (By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[2]")
CMBNTNS_VHCL_TXT_BTN = (By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[3]")
ELDT_HZMT_ENDRSMNT_TXT_BTN = (By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[4]")
ALL_RGHTS_TXT = (By.XPATH, "//footer[@class='text-black-50']")

class MainPage(Page):

    # 1 Verify text 1 "Please sign in" is here
    def vrfy_txt_here(self, txt):
        self.verify_text(txt, *TEXT_IS_HERE_1)

    # 2 Send correct login "gurovvic@gmail.com"
    def send_login(self, txt):
        self.input_text(txt, *LGN_FLD)

    # 3 Send correct password "QWERTY_GUROV"
    def send_password(self, txt):
        self.input_text(txt, *PSSWRD_FLD)

    # 4 Click on Sign in button
    def click_sign_in_btn(self):
        self.click(*SGN_IN_BTN)

    # 5 Verify text 2 "Start your test" is here
    def vrfy_txt_here_2(self, txt):
        self.verify_text(txt, *TEXT_IS_HERE_2)

    # 6 Verify username "gurovvic@gmail.com" is here
    def vrf_username_here(self, txt):
        self.verify_text(txt, *TEXT_IS_HERE_3)

    # 7 Send wrong login "WRONG@gmail.com"
    def snd_wrng_lgn(self, txt):
        self.input_text(txt, *LGN_FLD)

    # 8 Send wrong password "WRONG_GUROV"
    def snd_wrng_psswrd(self, txt):
        self.input_text(txt, *PSSWRD_FLD)

    # 9 Verify text "Invalid Login or Password" is here
    def vrfy_txt_here_4(self, txt):
        self.verify_text(txt, *INVLD_LGN_OR_PSWRD_TXT)

    # 10 Click on Sign in button
    def click_sign_in_btn(self):
        self.click(*SGN_IN_BTN)

    # 11 Login with the right credentials
    def login_with_the_right_credentials(self):
        self.send_login(LOGIN)
        self.send_password(PSSWRD)
        self.click_sign_in_btn()

    # 12 Verify "General knowledge (continue)" button text is here
    def gnrl_knwldg_txt_btn(self, txt):
        self.verify_text(txt, *GNRL_KNWLDG_TXT_BTN)

    # 13 Verify "Air brakes" button text is here
    def air_brks_txt_btn(self, txt):
        self.verify_text(txt, *AIR_BRKS_TXT_BTN)

    # 14 Verify "Combination vehicles" button text is here
    def cmmbtn_vhcls_txt_btn(self, txt):
        self.verify_text(txt, *CMBNTNS_VHCL_TXT_BTN)

    # 15 Verify "ELDT Hazmat endorsement" button text is here
    def eldt_hzmt_endrsmnt_txt_btn(self, txt):
        self.verify_text(txt, *ELDT_HZMT_ENDRSMNT_TXT_BTN)

    # 16 Verify "All rights reserved" text is here
    def all_rghts_rsrvs_txt(self, txt):
        self.verify_text(txt, *ALL_RGHTS_TXT)

    # End of the above code
