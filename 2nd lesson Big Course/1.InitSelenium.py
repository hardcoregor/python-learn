from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SelectById():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get('https://facebook.com')
        driver.maximize_window()

        email = driver.find_element(By.ID, "email")
        password = driver.find_element(By.ID, "pass")
        email.send_keys("test@gmail.com")
        password.send_keys("123@312415%")
        time.sleep(500)

class SelectByName():
    def locate_by_name(self):
        driver = webdriver.Chrome()
        driver.get('https://facebook.com')
        driver.maximize_window()

        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME, "pass")
        email.send_keys("test@gmail.com")
        password.send_keys("123@312415%")
        time.sleep(500)

class SelectByLink():
    def locate_by_link(self):
        driver = webdriver.Chrome()
        driver.get('https://facebook.com')
        driver.maximize_window()

        link = driver.find_element(By.LINK_TEXT, "Забыли пароль?")
        link.click()
        time.sleep(500)

# findbyid = SelectById()
# findbyid.locate_by_id()
# findbyname = SelectByName()
# findbyname.locate_by_name()
clickOnLink = SelectByLink()
clickOnLink.locate_by_link()


