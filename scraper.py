from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import time

webdriver = r'/usr/local/bin/chromedriver'

driver = Chrome(executable_path=webdriver)

URL = 'https://www.airasia.com/select/en/gb/JHB/PEN/2020-04-30/N/1/0/0/O/N/MYR/ST'

driver.get(URL)

# execute script to scroll down the page
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(10)

# ticket price list
price_elements = []
price_wrappper = driver.find_elements_by_class_name('section-content')

for price in price_wrappper:
    amount = price.find_element_by_class_name('fare-amount')
    price_elements.append(amount.text)

print(f'Ticket price list: {price_elements}')

# departure time list
count = 0
departure_time_list = []
while count < 4:
    departure_time = driver.find_elements_by_id(
        'departing-time-desc-0-'+str(count))
    departure_time_list.append(departure_time[0].text)
    count += 1

print(f'Departure time list: {departure_time_list}')

driver.quit()
