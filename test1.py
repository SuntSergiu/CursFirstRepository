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
driver.get('https://www.officeshoes.ro/')
# I will maximize the page window
driver.maximize_window()
time.sleep(2)
# I will print the current url
print(driver.current_url)
time.sleep(2)
# I will accept the cookies
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/button').click()
time.sleep(2)
# # I will hover the mouse over LIVRARE GRATUITA to see what it says
# mouseHover = ActionChains(driver)
# livrareGratuita = driver.find_element(By.XPATH, '//li[@class="shipping_delivery_info "]')
# mouseHover.move_to_element(livrareGratuita).perform()
# time.sleep(2)
# # I will click on Pantofi Barbati
# driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[4]/ul/li[3]/a').click()
# time.sleep(2)
# # I will click the search box
# driver.find_element(By.NAME, 'q').click()
# time.sleep(2)
# # I will search for shoes
# driver.find_element(By.NAME, 'q').send_keys('Timberland 6 In')
# time.sleep(5)
# # I will select the ones I want
# driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[1]/form/div/div/div[1]/div[2]/a[2]/div[2]/div[1]').click()
# time.sleep(2)
# # I will select a colour I want
# driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[2]/div[3]/div[3]/a').click()
# time.sleep(1)
# # I will look at them from different point of view
# driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[7]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[5]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[4]/a').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[3]/a').click()
# time.sleep(2)
# # I will select a size
# marimi = driver.find_elements(By.XPATH, '//*[@id="add_cart_form"]/div[1]/ul/div[3]')
# for marine in marimi:
#     if marine.text == '42':
#         marine.click()
#         break
# time.sleep(2)
# # I will scroll the page down
# html = driver.find_element(By.TAG_NAME, 'html')
# html.send_keys(Keys.END)


# I will click on Magazine
driver.find_element(By.LINK_TEXT, 'MAGAZINE').click()
time.sleep(2)

magazine = driver.find_elements(By.CLASS_NAME, 'row')
# print(len(magazine))
for magazin in magazine:
    if magazin.text == 'Office Shoes Alba Iulia':
        magazin.click()
        break



