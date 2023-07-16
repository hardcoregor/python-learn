from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AutoSuggestion():
    def Auto_suggestion(self):
        driver = webdriver.Chrome()
        driver.get('https://google.com')
        driver.maximize_window()
        search = driver.find_element(By.XPATH, "//textarea[@name='q']")
        search.send_keys("python")
        time.sleep(2)
        # search.send_keys(Keys.RETURN) #Same to press enter
        search_result = driver.find_elements(By.XPATH, "//ul[@class='G43f7e' and @jsname='bw4e9b']//li")
        
        for results in search_result:
            if "python online" in results.text:
                results.click()
                time.sleep(10)
                break

        time.sleep(200)

display = AutoSuggestion()
display.Auto_suggestion()