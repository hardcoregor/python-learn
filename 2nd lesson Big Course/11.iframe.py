from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Iframe():
    def iframe(self):
        driver = webdriver.Chrome()
        driver.get('https://w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css')
        driver.maximize_window()

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@id='w3loginbtn']").click()

        time.sleep(20000)

display = Iframe()
display.iframe()