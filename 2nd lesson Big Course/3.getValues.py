from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetAttrValue():
    def get_value(self):
        driver = webdriver.Chrome()
        driver.get('https://www.like4like.org/login/')
        attr = driver.find_element(By.TAG_NAME, "input").get_attribute("id")
        print(attr)
        time.sleep(5)

attrObj = GetAttrValue()
attrObj.get_value()