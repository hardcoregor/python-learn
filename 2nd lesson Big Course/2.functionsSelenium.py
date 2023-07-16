from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SelectById():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get('https://facebook.com')

        h2 = driver.find_element(By.TAG_NAME, 'h2')
        print(h2.text)

        # lista = driver.find_elements(By.TAG_NAME, 'a')
        # for i in lista:
        #     print(i.text)

        # driver.current_url
        # driver.back back to previous page
        # driver.forward() back to next page
        # driver.refresh() ref page
        # driver.title
        # driver.get()
        # driver.maximize_window()
        # driver.minimize_window()
        # driver.fullscreen_window() F11
        # driver.close() only one tab
        # driver.quit() whole browser
        time.sleep(500)

findbyid = SelectById()
findbyid.locate_by_id()