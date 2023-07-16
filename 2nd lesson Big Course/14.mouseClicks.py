from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Mouse():
    def move(self):
        driver = webdriver.Chrome()
        driver.get('https://demo.guru99.com/test/simple_context_menu.html')
        driver.maximize_window()
        chain = ActionChains(driver)

        # rigth_click = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # chain.context_click(rigth_click).perform() #Rigth click
        # driver.find_element(By.XPATH, "//*[@id='authentication']/ul/li[1]").click()

        doubeClick = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
        chain.double_click(doubeClick).perform()

        time.sleep(20000)

display = Mouse()
display.move()