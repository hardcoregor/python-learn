import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json

from solveRecaptcha import solveRecaptcha

browser = webdriver.Chrome()
browser.get('https://google.com/recaptcha/api2/demo')

result = solveRecaptcha(
    "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
    "https://2captcha.com/demo/recaptcha-v2"
)

# code = result['code']
# print(code)

# WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
# )

# browser.execute_script(
#     "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

# browser.find_element(By.ID, "recaptcha-demo-submit").click()

time.sleep(500)
browser.quit()