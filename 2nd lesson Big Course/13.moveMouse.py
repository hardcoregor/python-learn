from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Mouse():
    def move(self):
        driver = webdriver.Chrome()
        driver.get('https://like4like.org/login/')
        driver.maximize_window()

        login = driver.find_element(By.XPATH, "//input[@name='username']")
        login.send_keys('from env')
        psw = driver.find_element(By.XPATH, "//input[@name='password']")
        psw.send_keys('from env')

        psw.send_keys(Keys.RETURN)
        time.sleep(2)

        free_credits = driver.find_element(By.XPATH, "//*[@id='navbar']/ul/li[3]/a")
        chain = ActionChains(driver)
        chain.move_to_element(free_credits).perform()

        time.sleep(5)

        driver.find_element(By.XPATH, "//*[@id='navbar']/ul/li[3]/ul/li[6]/a[1]").click()

        time.sleep(20000)

display = Mouse()
display.move()