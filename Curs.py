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

### I will open the Chrome browser
options = Options()
options.add_experimental_option("detach", True)
service_obj = Service('D:/ChromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=options)

### I will go on test page
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

### I will hover the mouse over LIVRARE GRATUITA to see what it says
mouseHover = ActionChains(driver)
livrareGratuita = driver.find_element(By.XPATH, '//li[@class="shipping_delivery_info "]')
mouseHover.move_to_element(livrareGratuita).perform()
time.sleep(2)

### I will register to page
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

### I will log in to page
driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[5]').click()
driver.find_element(By.NAME, 'identity').clear()
driver.find_element(By.NAME, 'identity').send_keys('sergiu_vasilcin@yahoo.com')
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.ID, 'remember').click()
Conectare = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]/fieldset/div[4]/div/button'))).click()

### I will click on Brands
driver.find_element(By.LINK_TEXT, 'BRANDURI').click()
time.sleep(2)
### I will choose Brands with the letter F
driver.find_element(By.LINK_TEXT, 'F').click()
time.sleep(2)

### I will select FILA
driver.find_element(By.XPATH, '//*[@id="brands-letter-F"]/div[2]/ul/li/a').click()

### I will print the name and price of the available shoes
products = driver.find_elements(By.CLASS_NAME, 'col-xl-3')
print('Number of shoes available: ', len(products))
for product in products:
    name = product.find_element(By.XPATH, './/h2[@class="product_list_title"]').text
    price = product.find_element(By.XPATH, './/span[@class="price"]').text
    image = product.find_element(By.XPATH, './/*[@id="product_item_article"]/img').get_attribute('src')
    print('Name: ' +name)
    print('Price: ' +price)
    print('Image: ' +image + "\n")
time.sleep(2)

### I will add one pair to cart(select a shoe size)
driver.find_element(By.ID, 'proid-39728').click()
time.sleep(2)
driver.find_element(By.ID, '42').click()
time.sleep(2)
driver.find_element(By.NAME, 'cart_submit').click()
time.sleep(2)

### I will click on Pantofi Barbati
driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[4]/ul/li[3]/a').click()

### I will click the search box
driver.find_element(By.NAME, 'q').click()

### I will search for shoes
driver.find_element(By.NAME, 'q').send_keys('Timberland 6 In')
time.sleep(5)

### I will select the ones I want
driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/div[3]/ul/li[1]/form/div/div/div[1]/div[2]/a[2]/div[2]/div[1]').click()
time.sleep(4)

### I will select a colour I want and check them out
driver.find_element(By.XPATH, '//a[@href="HTTPS://www.officeshoes.ro/incaltaminte-timberland-bocanci-6-inch-premium-wp-boot/66788"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[7]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[5]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[3]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[1]/div[2]/div[4]/a').click()
time.sleep(2)

### I will select a size
marimi = driver.find_elements(By.XPATH, '//*[@id="add_cart_form"]/div[1]/ul/div[3]')
for marine in marimi:
    if marine.text == '42':
        marine.click()
        break
time.sleep(2)

### I will add the shoes to Cart
driver.find_element(By.NAME, 'cart_submit').click()
time.sleep(3)

### I will proceed to checkout
driver.find_element(By.CLASS_NAME, 'finish-order-btn').click()
time.sleep(3)

### I will finalise the billing process
driver.find_element(By.ID, 'billing_name').clear()
driver.find_element(By.ID, 'billing_name').send_keys('Vasilcin')
driver.find_element(By.ID, 'billing_surname').clear()
driver.find_element(By.ID, 'billing_surname').send_keys('Sergiu')
driver.find_element(By.ID, 'billing_email').clear()
driver.find_element(By.ID, 'billing_email').send_keys('sergiu_vasilcin@yahoo.com')
driver.find_element(By.ID, 'billing_phone').clear()
driver.find_element(By.ID, 'billing_phone').send_keys('0723456789')
driver.find_element(By.ID, 'billing_pnum').clear()
driver.find_element(By.ID, 'billing_pnum').send_keys('300977')
dropdown_pnum = Select(driver.find_element(By.NAME, 'billing_region'))
dropdown_pnum.select_by_visible_text('TIMIS')
time.sleep(2)
dropdown_city = Select(driver.find_element(By.NAME, 'billing_city'))
dropdown_city.select_by_visible_text('SANNICOLAU MARE')
driver.find_element(By.ID, 'billing_address').clear()
driver.find_element(By.ID, 'billing_address').send_keys('Gheorghe Lazar')
driver.find_element(By.ID, 'billing_address_number').clear()
driver.find_element(By.ID, 'billing_address_number').send_keys('7-9')
driver.find_element(By.ID, 'billing_entry').clear()
driver.find_element(By.ID, 'billing_entry').send_keys('A')
driver.find_element(By.ID, 'billing_building').clear()
driver.find_element(By.ID, 'billing_building').send_keys('L9')
driver.find_element(By.ID, 'billing_floor').clear()
driver.find_element(By.ID, 'billing_floor').send_keys('4')
driver.find_element(By.ID, 'billing_apartment').clear()
driver.find_element(By.ID, 'billing_apartment').send_keys('11')
driver.find_element(By.ID, 'comment').clear()
driver.find_element(By.ID, 'comment').send_keys('Thank you and have a good day!')
time.sleep(2)
driver.close()