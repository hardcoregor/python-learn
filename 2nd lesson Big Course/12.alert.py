from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Alert():
    def test_alert(self):
        driver = webdriver.Chrome()
        driver.get('https://w3schools.com/js/tryit.asp?filename=tryjs_prompt')
        driver.maximize_window()

        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[text()='Try it']").click()
        driver.switch_to.alert.accept() #switch to alert pop up window
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[text()='Try it']").click()
        driver.switch_to.alert.dismiss() #switch to alert pop up window
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[text()='Try it']").click()
        driver.switch_to.alert.send_keys("Exploit") #switch to alert pop up window
        driver.switch_to.alert.accept()
        time.sleep(1)

        time.sleep(20000)

display = Alert()
display.test_alert()