import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.like4like.org/login/register.php')
lastname = driver.find_element(By.XPATH, "//input[@id='password']")
lastname.send_keys("Egorshka")

time.sleep(500)