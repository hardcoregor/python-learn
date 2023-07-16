from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Calendat():
    def date_clicker(self):
        driver = webdriver.Chrome()
        driver.get('https://yatra.com')
        driver.maximize_window()

        dates = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        dates.click()

        time.sleep(2)

        # selected_date = driver.find_element(By.XPATH, "//td[@id='20/07/2023']")
        # selected_date.click()

        all_date = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_date:
            if date.get_attribute("data-date") == "30/07/2023":
                date.click()
                time.sleep(2)
                break

        time.sleep(2000)

display = Calendat()
display.date_clicker()