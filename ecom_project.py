import time
from selenium.webdriver import ActionChains
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/sirwi/Downloads/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=serv_obj, options=options)
driver.implicitly_wait(10)

driver.get("http://tutorialsninja.com/demo/")

# laptops
laptops = driver.find_element(By.XPATH, "//a[text()='Laptops & Notebooks']")
action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2 = driver.find_element(By.XPATH, "(//a[normalize-space()='Show All Laptops & Notebooks'])[1]")
laptops_2.click()
time.sleep(1)

# click on HP laptop
HP = driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']")
HP.click()

# first picture
first_pic = driver.find_element(By.XPATH, "(//img[@title='HP LP3065'])[1]")
first_pic.click()

# right arrow button
right_arrow_btn = driver.find_element(By.XPATH, "(//button[@title='Next (Right arrow key)'])[1]")

for i in range(0, 2):
    right_arrow_btn.click()
    time.sleep(1)

# save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(1, 101)) + '.png')

# close
x_btn = driver.find_element(By.XPATH, "//button[normalize-space()='×']")
x_btn.click()
time.sleep(1)

# quantity
quantity = driver.find_element(By.ID, "input-quantity")
quantity.click()
time.sleep(1)

# clear and then add 2
quantity.clear()
time.sleep(1)
quantity.send_keys("2")
time.sleep(1)

# scroll
add_to_btn_2 = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
driver.execute_script("arguments[0].scrollIntoView();", add_to_btn_2)
time.sleep(1)

# calendar
calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

# date
right_click_calender = driver.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='next'][contains("
                                                     "text(),'›')]")
month_year = driver.find_element(By.XPATH, '//th[@class="picker-switch"]')

# year 2023 and month December
while month_year.text != 'December 2023':
    right_click_calender.click()
time.sleep(2)

# day 31
calendar_date = driver.find_element(By.XPATH, '//td[normalize-space()="31"]')
calendar_date.click()
time.sleep(2)

# add to button
add_to_btn_2.click()
time.sleep(1)

# checkout
go_to_cart = driver.find_element(By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
go_to_cart.click()
time.sleep(1)

checkout = driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[2]/strong')
checkout.click()
time.sleep(1)

# click on guest account
guest = driver.find_element(By.XPATH, "//input[@value='guest']")
guest.click()

# click continue
continue_1 = driver.find_element(By.XPATH, "//input[@id='button-account']")
continue_1.click()
time.sleep(1)

step_2 = driver.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]')
driver.execute_script("arguments[0].scrollIntoView();", step_2)
time.sleep(1)

# first name
first_name = driver.find_element(By.ID, "input-payment-firstname")
first_name.click()
time.sleep(1)
first_name.send_keys("test_first_name")

# last name
last_name = driver.find_element(By.ID, "input-payment-lastname")
last_name.click()
time.sleep(1)
last_name.send_keys("test_last_name")

# email
email = driver.find_element(By.ID, "input-payment-email")
email.click()
time.sleep(1)
email.send_keys("test@test.com")

# telephone
telephone = driver.find_element(By.ID, "input-payment-telephone")
telephone.click()
time.sleep(1)
telephone.send_keys("012345678")

# address
address = driver.find_element(By.XPATH, "//*[@id='input-payment-address-1']")
address.click()
time.sleep(1)
address.send_keys("teststreet 742")

# city
city = driver.find_element(By.ID, "input-payment-city")
city.click()
time.sleep(1)
city.send_keys("Calgary")

# post code
post_code = driver.find_element(By.ID, "input-payment-postcode")
post_code.click()
time.sleep(1)
post_code.send_keys("T2A0P9")
time.sleep(1)

# country
country = driver.find_element(By.ID, "input-payment-country")
dropdown_1 = Select(country)
time.sleep(1)
dropdown_1.select_by_index("41")
time.sleep(1)

# region
region = driver.find_element(By.ID, "input-payment-zone")
dropdown_2 = Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text("Alberta")
time.sleep(1)

# click continue
continue_2 = driver.find_element(By.XPATH, "//input[@id='button-guest']")
continue_2.click()
time.sleep(1)

# click continue
continue_3 = driver.find_element(By.XPATH, "//input[@id='button-shipping-method']")
continue_3.click()
time.sleep(1)

# accept terms and conditions
t_c = driver.find_element(By.XPATH, "//input[@name='agree']")
t_c .click()
time.sleep(1)

# click continue
continue_4 = driver.find_element(By.XPATH, "//input[@id='button-payment-method']")
continue_4.click()
time.sleep(1)

# final price
final_price = driver.find_element(By.XPATH, "//td[normalize-space()='$205.00']")
print("The final price of both products is: " + final_price.text)
time.sleep(2)

# click confirm order button
confirm_btn = driver.find_element(By.XPATH, "//input[@id='button-confirm']")
confirm_btn.click()

# success text
success_text = driver.find_element(By.XPATH, "//h1[normalize-space()='Your order has been placed!']")
print(success_text.text)
time.sleep(1)

driver.close()
