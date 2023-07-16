from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropDownSelect():
    def dropdown(self):
        driver = webdriver.Chrome()
        driver.get('https://facebook.com/signup')
        driver.maximize_window()
        dropdown = driver.find_element(By.ID, "month")
        dd = Select(dropdown)
        dd.select_by_value("4") #Апрель
        time.sleep(2)
        dd.select_by_index(10) #Ноябрь
        time.sleep(2)
        dd.select_by_visible_text("сен")
        time.sleep(200)
        

display = DropDownSelect()
display.dropdown()