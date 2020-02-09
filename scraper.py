from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv
import os
from datetime import datetime

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
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# insert current date time
empty_date_list = list()
empty_date_list.append(dt_string)
departure_time_map_price["Request On"] = empty_date_list

for content in content_wrapper:
    amount = content.find_element_by_class_name('fare-amount')
    price_elements.append(amount.text)
    departure_time = driver.find_elements_by_id(
        'departing-time-desc-0-'+str(count))
    departure_time_list.append(departure_time[0].text)
    count += 1
    empty_list = list()
    empty_list.append("RM: "+amount.text)
    departure_time_map_price[departure_time[0].text] = empty_list

# print(f'Ticket price list: {price_elements}')

# print(f'Departure time list: {departure_time_list}')

print(departure_time_map_price)

driver.quit()

try:
    if os.path.isfile('Tickets.csv') is False:
        map_to_csv = pd.DataFrame.from_dict(
            departure_time_map_price)
        map_to_csv.to_csv('Tickets.csv', index=False)
    else:
        departure_time_key = []
        price_values = []
        for keys, values in departure_time_map_price.items():
            departure_time_key.append(keys)
            price_values.append(values[0])
        with open('Tickets.csv', 'a+', newline='') as write_obj:
            dict_writer = csv.writer(write_obj)
            dict_writer.writerow(price_values)
except Exception as e:
    raise e
