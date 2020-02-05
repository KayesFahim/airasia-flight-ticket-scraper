from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv
import os

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
departure_time_list = []
departure_time_map_price = {}
count = 0
content_wrapper = driver.find_elements_by_class_name('section-content')

for content in content_wrapper:
    amount = content.find_element_by_class_name('fare-amount')
    price_elements.append(amount.text)
    departure_time = driver.find_elements_by_id(
        'departing-time-desc-0-'+str(count))
    departure_time_list.append(departure_time[0].text)
    count += 1
    departure_time_map_price[departure_time[0].text] = amount.text

# print(f'Ticket price list: {price_elements}')

# print(f'Departure time list: {departure_time_list}')

print(departure_time_map_price)

driver.quit()

try:
    if os.path.isfile('Tickets.csv') is False:
        map_to_csv = pd.DataFrame.from_dict(
            departure_time_map_price, orient="index")
        map_to_csv.to_csv('Tickets.csv')
    else:  # Todo: append list of price into existing csv file

except Exception as e:
    raise e
