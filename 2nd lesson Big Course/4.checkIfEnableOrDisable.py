from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CheckState():
    def enable_disable(self):
        driver = webdriver.Chrome()
        driver.get('https://training.openspan.com/login')
        state = driver.find_element(By.XPATH, "//input[@id='user_name']").is_enabled()
        if(state == True):
            print('the button is enable')
        else:
            print('the button is disabled')

        time.sleep(20)

class CheckDisplay():
    def display(self):
        driver = webdriver.Chrome()
        driver.get('https://www.w3scools.com/howto/howto_js_toggle_hide_show.asp')
        # dis = driver.find_element(By.XPATH, "//input[@id='user_name']").is_enabled()

        time.sleep(20)
        

display = CheckDisplay()
display.display()