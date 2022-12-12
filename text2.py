from selenium import webdriver
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
# driver.get('https://www.officeshoes.ro/')
# time.sleep(2)

def login():
    driver.get('https://www.officeshoes.ro/')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[4]/a').click()
    driver.find_element(By.XPATH, '//div[@class="col-md-8"]').click()
    dropdown_Gender = Select(driver.find_element(By.NAME, 'gender'))
    dropdown_Gender.select_by_visible_text('Bărbat')
    driver.find_element(By.ID, 'first_name').clear()
    driver.find_element(By.ID, 'first_name').send_keys('Sergiu Vasilcin')
    driver.find_element(By.ID, 'phone').clear()
    driver.find_element(By.ID, 'phone').send_keys('0721234567')
    driver.find_element(By.ID, 'pcode').clear()
    driver.find_element(By.ID, 'pcode').send_keys('300779')
    driver.find_element(By.ID, 'pcode').clear()
    driver.find_element(By.ID, 'pcode').send_keys('300779')
    driver.find_element(By.ID, 'city').clear()
    driver.find_element(By.ID, 'city').send_keys('Sannicolau Mare')
    dropdown_Judet = Select(driver.find_element(By.NAME, 'region'))
    dropdown_Judet.select_by_visible_text('Timiş')
    driver.find_element(By.ID, 'address_number').clear()
    driver.find_element(By.ID, 'address_number').send_keys('7-9')
    driver.find_element(By.ID, 'entry').clear()
    driver.find_element(By.ID, 'entry').send_keys('A')
    driver.find_element(By.ID, 'building').clear()
    driver.find_element(By.ID, 'building').send_keys('L9')
    driver.find_element(By.ID, 'floor').clear()
    driver.find_element(By.ID, 'floor').send_keys('4')
    driver.find_element(By.ID, 'apartment').clear()
    driver.find_element(By.ID, 'apartment').send_keys('11')
    driver.find_element(By.ID, 'address').clear()
    driver.find_element(By.ID, 'address').send_keys('Gheorghe Lazar')
    driver.find_element(By.ID, 'email').clear()
    driver.find_element(By.ID, 'email').send_keys('sergiu_vasilcin@yahoo.com')
    driver.find_element(By.ID, 'password').clear()
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'password_confirm').clear()
    driver.find_element(By.ID, 'password_confirm').send_keys('123456')
    dropdown_Day = Select(driver.find_element(By.ID, 'day_selector'))
    dropdown_Day.select_by_visible_text('20')
    dropdown_Month = Select(driver.find_element(By.ID, 'month_selector'))
    dropdown_Month.select_by_visible_text('7')
    dropdown_Year = Select(driver.find_element(By.ID, 'year_selector'))
    dropdown_Year.select_by_visible_text('1980')
    driver.find_element(By.ID, 'register_gdpr').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login_form"]/fieldset/div[20]/button').click()
    time.sleep(1)
login()




# driver.find_element(By.XPATH, '/html/body/div[5]/div/div/button').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[4]/ul/li[3]/a').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//li[@class="shops"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="brands-letters"]/li[3]/a').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="brands-letters"]/li[18]/a').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="brands-letter-T"]/div[2]/ul/li[1]/a/img').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[2]/aside/div[2]/div[2]/section/form/div[1]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="type_inc_aside_desktop_list"]/li[32]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[2]/aside/div[2]/div[2]/section/form/div[2]/button[2]').click()
# time.sleep(2)
#
# # I will print the available products
# produse = driver.find_elements(By.CLASS_NAME, 'col-xl-3')
# print(len(produse))
# for prod in produse:
#     nume = prod.find_element(By.XPATH, './/*[@id="product_item_article"]/h2').text
#     pret = prod.find_element(By.XPATH, './/span[@class="price"]').text
#     link = prod.find_element(By.XPATH, './/*[@id="product_item_article"]/img').get_attribute('src')
#     print('Nume Produs: ' +nume)
#     print('Pret Produs: ' +pret)
#     print('Link Produs: ' +link + "\n")



# # I will Register
# driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[4]/a').click()
# driver.find_element(By.XPATH, '//div[@class="col-md-8"]').click()
# dropdown_Gender = Select(driver.find_element(By.NAME, 'gender'))
# dropdown_Gender.select_by_visible_text('Bărbat')
# driver.find_element(By.ID, 'first_name').clear()
# driver.find_element(By.ID, 'first_name').send_keys('Sergiu Vasilcin')
# driver.find_element(By.ID, 'phone').clear()
# driver.find_element(By.ID, 'phone').send_keys('0721234567')
# driver.find_element(By.ID, 'pcode').clear()
# driver.find_element(By.ID, 'pcode').send_keys('300779')
# driver.find_element(By.ID, 'pcode').clear()
# driver.find_element(By.ID, 'pcode').send_keys('300779')
# driver.find_element(By.ID, 'city').clear()
# driver.find_element(By.ID, 'city').send_keys('Sannicolau Mare')
# dropdown_Judet = Select(driver.find_element(By.NAME, 'region'))
# dropdown_Judet.select_by_visible_text('Timiş')
# driver.find_element(By.ID, 'address_number').clear()
# driver.find_element(By.ID, 'address_number').send_keys('7-9')
# driver.find_element(By.ID, 'entry').clear()
# driver.find_element(By.ID, 'entry').send_keys('A')
# driver.find_element(By.ID, 'building').clear()
# driver.find_element(By.ID, 'building').send_keys('L9')
# driver.find_element(By.ID, 'floor').clear()
# driver.find_element(By.ID, 'floor').send_keys('4')
# driver.find_element(By.ID, 'apartment').clear()
# driver.find_element(By.ID, 'apartment').send_keys('11')
# driver.find_element(By.ID, 'address').clear()
# driver.find_element(By.ID, 'address').send_keys('Gheorghe Lazar')
# driver.find_element(By.ID, 'email').clear()
# driver.find_element(By.ID, 'email').send_keys('sergiu_vasilcin@yahoo.com')
# driver.find_element(By.ID, 'password').clear()
# driver.find_element(By.ID, 'password').send_keys('123456')
# driver.find_element(By.ID, 'password_confirm').clear()
# driver.find_element(By.ID, 'password_confirm').send_keys('123456')
# dropdown_Day = Select(driver.find_element(By.ID, 'day_selector'))
# dropdown_Day.select_by_visible_text('20')
# dropdown_Month = Select(driver.find_element(By.ID, 'month_selector'))
# dropdown_Month.select_by_visible_text('7')
# dropdown_Year = Select(driver.find_element(By.ID, 'year_selector'))
# dropdown_Year.select_by_visible_text('1980')
# driver.find_element(By.ID, 'register_gdpr').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="login_form"]/fieldset/div[20]/button').click()
# time.sleep(1)
#
# # I will Sign In
# driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[5]').click()
# driver.find_element(By.NAME, 'identity').clear()
# driver.find_element(By.NAME, 'identity').send_keys('sergiu_vasilcin@yahoo.com')
# driver.find_element(By.NAME, 'password').clear()
# driver.find_element(By.NAME, 'password').send_keys('123456')
# driver.find_element(By.ID, 'remember').click()
# Conectare = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]/fieldset/div[4]/div/button'))).click()
















# magazine = driver.find_elements(By.CLASS_NAME, 'row')
# print(len(magazine))
# for magazin in magazine:
#     nume = magazin.find_element(By.XPATH, './/div[@class="col-lg-12"]/h2/a').text
#     adresa = magazin.find_element(By.XPATH, './/div[@class="col-lg-3"]/span').text
#     mail = magazin.find_element(By.XPATH, './/div[@class="col-lg-3"]/a').get_attribute('href')
#     tel = magazin.find_element(By.XPATH, './/div[@class="col-lg-3"]/a[2]').get_attribute('href')
#
#     print('Locatia: ' +nume)
#     print('Adresa: ' +adresa)
#     print('Mail: ' +mail)
#     print(tel + '\n')







