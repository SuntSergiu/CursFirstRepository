from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# I will open the chrome browser
options = Options()
options.add_experimental_option("detach", True)
service_obj = Service('D:/ChromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=options)

# I will go on test page
driver.get('https://www.officeshoes.ro/pantofi-barbati-converse-42-albastru-rosu/20707409/48/order_asc')
# I will maximize the page window
# driver.maximize_window()
# time.sleep(2)
# I will print the current url
# print(driver.current_url)
time.sleep(2)
# I will accept the cookies
driver.find_element(By.XPATH, '//div[@class="cookie-button"]').click()
time.sleep(2)

# prods = driver.find_elements(By.CLASS_NAME, 'product-article_wrapper')
# print(len(prods))
# prod_list = []
# for prod in prods:
#     shoes = prod.find_element(By.XPATH, './/div[@class="product-article__title"]').text
#     oldPrice = prod.find_element(By.XPATH, './/span[@class="old-price"]').text
#     price = prod.find_element(By.XPATH, './/span[@class="price"]').text
#     # print(shoes, price)
#
#     prod_item = {
#         'Shoe Selection': shoes,
#         'Old Price': oldPrice,
#         'New Price': price
#     }
#     prod_list.append(prod_item)
#
# df = pd.DataFrame(prod_list)
# print(df)
# time.sleep(3)
# converses = driver.find_elements(By.CLASS_NAME, 'product_list_title')
# for convers in converses:
#     if convers.text == 'El Distrito 2.0 Ox':
#         convers.click()
#         break


prods = driver.find_elements(By.CLASS_NAME, 'product-article_wrapper')
print(len(prods))
# prod_list = []
for prod in prods:
    shoes = prod.find_element(By.XPATH, './/div[@class="product-article__title"]').text
    img = prod.find_element(By.CLASS_NAME, 'img-responsive').get_attribute('src')
    print('Shoe Name: ' + shoes)
    print('Shoe Image: ' + img + '\n')
