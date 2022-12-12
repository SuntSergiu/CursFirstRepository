from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# # I will open the chrome browser
# options = Options()
# options.add_experimental_option("detach", True)
# service_obj = Service('D:/ChromeDriver/chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj, options=options)
#
# # I will go on test page
# driver.get('https://www.nike.com/ro')
# # I will maximize the page window
# driver.maximize_window()
# time.sleep(3)
# # I will print the current url
# print(driver.current_url)
# # I will accept cookies
# driver.find_element(By.ID, 'hf_cookie_text_cookieAccept').click()
# time.sleep(3)
# # I will click the Sign In
# driver.find_element(By.ID, 'hf_title_signin_membership').click()
# time.sleep(3)
# # I will enter the email address
# driver.find_element(By.NAME, 'emailAddress').clear()
# driver.find_element(By.NAME, 'emailAddress').send_keys('sergiu_vasilcin@yahoo.com')
# time.sleep(2)
# # I will enter the password
# driver.find_element(By.NAME, 'password').clear()
# driver.find_element(By.NAME, 'password').send_keys('Slickback1!')
# time.sleep(2)
# # I will uncheck the Keep me signed in box
# driver.find_element(By.ID, 'keepMeLoggedIn').click()
# time.sleep(2)
# # I will Sign In
# driver.find_element(By.CSS_SELECTOR, '5e8603f-f9ed-427b-8a5e-6b52b0a37fa0').click()




