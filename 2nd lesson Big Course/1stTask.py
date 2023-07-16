import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get('https://www.like4like.org/login/')
# # username = driver.find_element(By.ID, 'username')
# # username.send_keys('hello') #Typping in input

# password = driver.find_element(By.TAG_NAME, 'label') and driver.find_element(By.CLASS_NAME, 'bold') and driver.find_element(By.ID, 'password_text')
# print(password.text)

# time.sleep(500)

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the thrd number: "))

if(num1>=num2) and (num1>=num3):
    largest = num1
elif(num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3
print("the largest number: ", largest)