from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Mouse():
    def move(self):
        driver = webdriver.Chrome()
        driver.get('https://jqueryui.com/droppable/')
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        drag = driver.find_element(By.XPATH, "//div[@id='draggable']")
        drop = driver.find_element(By.XPATH, "//div[@id='droppable']")
        # ActionChains(driver).drag_and_drop(drag, drop).perform()
        ActionChains(driver).drag_and_drop_by_offset(drag,100,100).perform() #in pixels

        time.sleep(20000)

display = Mouse()
display.move()