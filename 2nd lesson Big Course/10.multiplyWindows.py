from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Multiple_windows():
    def multi_windows(self):
        driver = webdriver.Chrome()
        driver.get('https://w3schools.com/html/default.asp')
        driver.maximize_window()

        print(driver.current_url)

        parent_handler = driver.current_window_handle
        print(parent_handler)

        driver.find_element(By.XPATH, "//div[@id='main']/div[4]/a").click()

        all_handle = driver.window_handles
        print(all_handle)

        for handle in all_handle: #switch on another window
            if handle != parent_handler:
                driver.switch_to.window(handle)
                time.sleep(5)
                driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/a[5]").click()
                time.sleep(5)
                driver.close()
                time.sleep(2)
                
        time.sleep(2000)

display = Multiple_windows()
display.multi_windows()