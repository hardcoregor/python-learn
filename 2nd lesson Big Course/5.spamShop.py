from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class Spam():
    def spamSprays(self):
      for _ in range(10):
          driver = webdriver.Chrome()
          driver.get('https://spraytown.com.ua/product/kobra-hp-400ml-%d0%ba%d1%80%d0%b0%d1%81%d0%ba%d0%b0-%d0%b4%d0%bb%d1%8f-%d0%b3%d1%80%d0%b0%d1%84%d1%84%d0%b8%d1%82%d0%b8/')
          driver.maximize_window()

          addToCartButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'single_add_to_cart_button')]")))

          swatchButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='swatch swatch-color swatch-white_1 ']")))
          swatchButton.click()

          wait = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".blockUI.blockOverlay")))

          addToCartButton.click()

          nextButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'wc-forward')]")))
          nextButton.click()

          goBacket = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'checkout-button')]")))
          goBacket.click()

          firstName = driver.find_element(By.NAME, "billing_first_name").send_keys('test')
          lastName = driver.find_element(By.NAME, "billing_last_name").send_keys('test')
          phone = driver.find_element(By.NAME, "billing_phone").send_keys('0939999999')
          mail = driver.find_element(By.NAME, "billing_email").send_keys('test@gmail.com')
          city = driver.find_element(By.NAME, "billing_city").send_keys('Krivoy Rog')
          np = driver.find_element(By.NAME, "billing_address_1").send_keys('228')
          comment = driver.find_element(By.NAME, "order_comments").send_keys('Позвоните срочно')

          try:
              suggest = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='payment']/div/div/p/label")))
              suggest.click()
          except:
              pass
          
          try:
              suggest = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='payment']/div/div/p/label")))
              suggest.click()
          except:
              pass

          order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@name, 'woocommerce_checkout_place_order')]")))
          order.click()

      time.sleep(20)

spam = Spam()
spam.spamSprays()
