from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Screen():
    def screen_shot(self):
        driver = webdriver.Chrome()
        driver.get('https://facebook.com/')
        driver.maximize_window()
        login = driver.find_element(By.XPATH, "//button[@name='login']")
        login.screenshot(".\\button.png")
        login.click()

        driver.get_screenshot_as_file(".\\page.png")
        driver.save_screenshot(".\\bysavescreen.png")
        
        time.sleep(2000)

display = Screen()
display.screen_shot()