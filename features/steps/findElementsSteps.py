from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'I will open the chrome browser')
def step_impl(context):
    options = Options()
    options.add_experimental_option("detach", True)
    service_obj = Service('D:/ChromeDriver/chromedriver.exe')
    context.driver = webdriver.Chrome(service=service_obj, options=options)


@given(u'I will go on test page')
def step_impl(context):
    context.driver.get('https://www.officeshoes.ro/')


@given(u'I will register to page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[4]/a').click()
    context.driver.find_element(By.XPATH, '//div[@class="col-md-8"]').click()
    dropdown_Gender = Select(context.driver.find_element(By.NAME, 'gender'))
    dropdown_Gender.select_by_visible_text('Bărbat')
    context.driver.find_element(By.ID, 'first_name').clear()
    context.driver.find_element(By.ID, 'first_name').send_keys('Sergiu Vasilcin')
    context.driver.find_element(By.ID, 'phone').clear()
    context.driver.find_element(By.ID, 'phone').send_keys('0721234567')
    context.driver.find_element(By.ID, 'pcode').clear()
    context.driver.find_element(By.ID, 'pcode').send_keys('300779')
    context.driver.find_element(By.ID, 'pcode').clear()
    context.driver.find_element(By.ID, 'pcode').send_keys('300779')
    context.driver.find_element(By.ID, 'city').clear()
    context.driver.find_element(By.ID, 'city').send_keys('Sannicolau Mare')
    dropdown_Judet = Select(context.driver.find_element(By.NAME, 'region'))
    dropdown_Judet.select_by_visible_text('Timiş')
    context.driver.find_element(By.ID, 'address_number').clear()
    context.driver.find_element(By.ID, 'address_number').send_keys('7-9')
    context.driver.find_element(By.ID, 'entry').clear()
    context.driver.find_element(By.ID, 'entry').send_keys('A')
    context.driver.find_element(By.ID, 'building').clear()
    context.driver.find_element(By.ID, 'building').send_keys('L9')
    context.driver.find_element(By.ID, 'floor').clear()
    context.driver.find_element(By.ID, 'floor').send_keys('4')
    context.driver.find_element(By.ID, 'apartment').clear()
    context.driver.find_element(By.ID, 'apartment').send_keys('11')
    context.driver.find_element(By.ID, 'address').clear()
    context.driver.find_element(By.ID, 'address').send_keys('Gheorghe Lazar')
    context.driver.find_element(By.ID, 'email').clear()
    context.driver.find_element(By.ID, 'email').send_keys('sergiu_vasilcin@yahoo.com')
    context.driver.find_element(By.ID, 'password').clear()
    context.driver.find_element(By.ID, 'password').send_keys('123456')
    context.driver.find_element(By.ID, 'password_confirm').clear()
    context.driver.find_element(By.ID, 'password_confirm').send_keys('123456')
    dropdown_Day = Select(context.driver.find_element(By.ID, 'day_selector'))
    dropdown_Day.select_by_visible_text('20')
    dropdown_Month = Select(context.driver.find_element(By.ID, 'month_selector'))
    dropdown_Month.select_by_visible_text('7')
    dropdown_Year = Select(context.driver.find_element(By.ID, 'year_selector'))
    dropdown_Year.select_by_visible_text('1980')
    context.driver.find_element(By.ID, 'register_gdpr').click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="login_form"]/fieldset/div[20]/button').click()
    time.sleep(1)

@given(u'I will log in to page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[5]').click()
    context.driver.find_element(By.NAME, 'identity').clear()
    context.driver.find_element(By.NAME, 'identity').send_keys('sergiu_vasilcin@yahoo.com')
    context.driver.find_element(By.NAME, 'password').clear()
    context.driver.find_element(By.NAME, 'password').send_keys('123456')
    context.driver.find_element(By.ID, 'remember').click()
    Conectare = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]/fieldset/div[4]/div/button'))).click()

@given(u'I will click on Pantofi Barbati')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[4]/ul/li[3]/a').click()

@given('I will click the search box')
def step_impl(context):
    context.driver.find_element(By.NAME, 'q').click()

@given('I will search for shoes')
def step_impl(context):
    context.driver.find_element(By.NAME, 'q').send_keys('Timberland 6 In')
    time.sleep(5)

@given("I will select the ones I want")
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[1]/form/div/div/div[1]/div[2]/a[2]/div[2]/div[1]').click()
    time.sleep(2)

@given("I will select a colour I want and check them out")
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[2]/div[3]/div[5]/a/img').click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[7]/a').click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[5]/a').click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[4]/a').click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[3]/a').click()
    time.sleep(2)

@given('I will select a size')
def step_impl(context):
    marimi = context.driver.find_elements(By.XPATH, '//*[@id="add_cart_form"]/div[1]/ul/div[3]')
    for marine in marimi:
        if marine.text == '42':
            marine.click()
            break
    time.sleep(2)

@given('I will add the shoes to Cart')
def step_impl(context):
    context.driver.find_element(By.NAME, 'cart_submit').click()
    time.sleep(2)

@given('I will proceed to checkout')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'finish-order-btn').click()
    time.sleep(2)

@given('I will finalise the billing process')
def step_impl(context):
    context.driver.find_element(By.ID, 'billing_name').clear()
    context.driver.find_element(By.ID, 'billing_name').send_keys('Vasilcin')

    context.driver.find_element(By.ID, 'billing_surname').clear()
    context.driver.find_element(By.ID, 'billing_surname').send_keys('Sergiu')

    context.driver.find_element(By.ID, 'billing_email').clear()
    context.driver.find_element(By.ID, 'billing_email').send_keys('sergiu_vasilcin@yahoo.com')

    context.driver.find_element(By.ID, 'billing_phone').clear()
    context.driver.find_element(By.ID, 'billing_phone').send_keys('0723456789')

    context.driver.find_element(By.ID, 'billing_pnum').clear()
    context.driver.find_element(By.ID, 'billing_pnum').send_keys('300977')

    dropdown_pnum = Select(context.driver.find_element(By.NAME, 'billing_region'))
    dropdown_pnum.select_by_visible_text('TIMIS')