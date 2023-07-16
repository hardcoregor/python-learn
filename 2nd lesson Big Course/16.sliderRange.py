from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Mouse():
    def move(self):
        driver = webdriver.Chrome()
        driver.get('https://www.snapdeal.com/search?keyword=phone%20mobile&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Price%3A3755%2C6499%7C')
        driver.maximize_window()
        slider1 = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
        slider2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")

        # ActionChains(driver).drag_and_drop_by_offset(slider1,50,0).perform()
        # ActionChains(driver).click_and_hold(slider1).pause(1).move_by_offset(50,0).release().perform()
        ActionChains(driver).click_and_hold(slider1).pause(1).move_to_element(slider2).perform()


        time.sleep(20000)

display = Mouse()
display.move()