from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
TEXT_IS_HERE_1 = EC.presence_of_element_located((By.XPATH, "//h1[@class='h3 mb-3 fw-normal']"))
LGN_FLD = (By.ID, "username")
PSSWRD_FLD = (By.ID, "password")
SGN_IN_BTN = (By.XPATH, "//button[@class='w-100 btn btn-lg btn-primary']")
LOGIN = "gurovvic@gmail.com"
PSSWRD = "QWERTY_GUROV"
GNRL_KNWLDG_TXT_BTN = EC.presence_of_element_located((By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[1]"))
# GNRL_KNWLDG_TXT_BTN = EC.presence_of_element_located((By.XPATH, "//a[text()='General knowledge (continue)']"))
AIR_BRKS_TXT_BTN = EC.presence_of_element_located((By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[2]"))
CMBNTNS_VHCL_TXT_BTN = EC.presence_of_element_located((By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[3]"))
ELDT_HZMT_ENDRSMNT_TXT_BTN = EC.presence_of_element_located((By.XPATH, "(//div[@class='d-grid gap-2 m-3'])[4]"))
ALL_RGHTS_TXT = EC.presence_of_element_located((By.XPATH, "//footer[@class='text-black-50']"))

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://portal.18wheelerschool.com/' )

# 2. Login with the right credentials
wait.until(EC.presence_of_element_located(LGN_FLD)).clear()
wait.until(EC.presence_of_element_located(LGN_FLD)).send_keys(LOGIN)
wait.until(EC.presence_of_element_located(PSSWRD_FLD)).clear()
wait.until(EC.presence_of_element_located(PSSWRD_FLD)).send_keys(PSSWRD)
wait.until(EC.element_to_be_clickable(SGN_IN_BTN)).click()

# 3. Verify "General knowledge (continue)" button text is here
expected_text_1 = 'General knowledge'
expected_text_2 = 'General knowledge (continue)'
actual_text = wait.until(GNRL_KNWLDG_TXT_BTN).text
assert expected_text_1 == actual_text or expected_text_2 == actual_text
print(f'Expected username "{expected_text_1}" or "{expected_text_2}", and got: "{actual_text}"\n')

# 4. Verify "Air brakes" button text is here
expected_text = 'Air brakes'
actual_text = wait.until(AIR_BRKS_TXT_BTN).text
assert expected_text in actual_text
print(f'Expected username "{expected_text}", and got: "{actual_text}"\n')

# 5. Verify "Combination vehicle" button text is here
expected_text = 'Combination vehicle'
actual_text = wait.until(CMBNTNS_VHCL_TXT_BTN).text
assert expected_text in actual_text
print(f'Expected username "{expected_text}", and got: "{actual_text}"\n')

# 6. Verify "ELDT Hazmat endorsement" button text is here
expected_text = 'ELDT Hazmat endorsement'
actual_text = wait.until(ELDT_HZMT_ENDRSMNT_TXT_BTN).text
assert expected_text in actual_text
print(f'Expected username "{expected_text}", and got: "{actual_text}"\n')

# 7. Verify "© 2023. All rights reserved." text is here
expected_text = '© 2023. All rights reserved.'
actual_text = wait.until(ALL_RGHTS_TXT).text
assert expected_text in actual_text
print(f'Expected username "{expected_text}", and got: "{actual_text}"\n')

driver.close()

# Sleep to see what we have
sleep(4)

# Driver quit
driver.quit()