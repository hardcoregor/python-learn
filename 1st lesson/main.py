import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json

with open("data.json", 'w') as f:
    json.dump([], f)

def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(
    options=options,
)
browser.get('https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&qid=1687365805&ref=sr_pg_1')

isNextDisabled = False

while not isNextDisabled:
    try:
        whole_page = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-component-type="s-search-result"]')))

        elem_list = browser.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")
        items = elem_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        for item in items:
            title = item.find_element(By.TAG_NAME, 'h2').text
            price = "No Price Found"
            img = "No Image Found"
            link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')

            try:
                price = item.find_element(By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
            except:
                pass

            try:
                img = item.find_element(By.CSS_SELECTOR, '.s-image').get_attribute("src")
            except:
                pass
            
            write_json({
                "title": title,
                "price": price,
                "image": img,
                "link": link
            })
            
        next_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 's-pagination-next')))
        next_class = next_btn.get_attribute('class')

        if 's-pagination-disabled' in next_class:
            isNextDisabled = True
            break
        else:
            browser.find_element(By.CLASS_NAME, 's-pagination-next').click()


    except Exception as e:
        print(e, "Main error")
        isNextDisabled = True

time.sleep(500)
browser.quit()
