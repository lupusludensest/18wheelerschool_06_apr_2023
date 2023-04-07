from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
TEXT_IS_HERE_4 = EC.presence_of_element_located((By.XPATH, "//h1[@class='h3 mb-3 fw-normal']"))
LGN_FLD = (By.ID, "username")
PSSWRD_FLD = (By.ID, "password")
SGN_IN_BTN = (By.XPATH, "//button[@class='w-100 btn btn-lg btn-primary']")
LOGIN = "WRONG@gmail.com"
PSSWRD = "WRONG_GUROV"
TEXT_IS_HERE_5 = EC.presence_of_element_located((By.XPATH, "//ul[@class='mb-0']"))

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://portal.18wheelerschool.com/' )

# 2. Verify text "Please sign in" is here
expected_text = 'Please sign in'
actual_text = wait.until(TEXT_IS_HERE_4).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n ')

# 3. Send wrong login "WRONG@gmail.com"
wait.until(EC.presence_of_element_located(LGN_FLD)).clear()
wait.until(EC.presence_of_element_located(LGN_FLD)).send_keys(LOGIN)

# 4. Send wrong password "WRONG_GUROV"
wait.until(EC.presence_of_element_located(PSSWRD_FLD)).clear()
wait.until(EC.presence_of_element_located(PSSWRD_FLD)).send_keys(PSSWRD)

# 5. Click on Sign in button
wait.until(EC.element_to_be_clickable(SGN_IN_BTN)).click()

# 6. Verify text "Invalid Login or Password" is here
expected_text = 'Invalid Login or Password'
actual_text = wait.until(TEXT_IS_HERE_5).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

driver.close()

# Sleep to see what we have
sleep(4)

# Driver quit
driver.quit()

