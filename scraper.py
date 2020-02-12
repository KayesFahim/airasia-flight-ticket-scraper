from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv
import os
from datetime import datetime


def get_current_date():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # insert current date time
    date_list = list()
    date_list.append(dt_string)
    return date_list


def write_to_csv(ticket_price_dict):
    try:
        if os.path.isfile('Tickets.csv') is False:
            map_to_csv = pd.DataFrame.from_dict(
                ticket_price_dict)
            map_to_csv.to_csv('Tickets.csv', index=False)
            print('CSV file created.')
        else:
            departure_time_key = []
            price_values = []
            for keys, values in ticket_price_dict.items():
                departure_time_key.append(keys)
                price_values.append(values[0])
            with open('Tickets.csv', 'a+', newline='') as write_obj:
                dict_writer = csv.writer(write_obj)
                dict_writer.writerow(price_values)
                print('CSV file updated.')
    except Exception as e:
        raise e


def main():
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

    departure_time_map_price["Request On"] = get_current_date()

    content_wrapper = driver.find_elements_by_class_name('section-content')

    for content in content_wrapper:
        amount = content.find_element_by_class_name('fare-amount')
        price_elements.append(amount.text)
        departure_time = driver.find_elements_by_id(
            'departing-time-desc-0-'+str(count))
        departure_time_list.append(departure_time[0].text)
        count += 1
        price_list = list()
        price_list.append("RM "+amount.text)
        departure_time_map_price[departure_time[0].text] = price_list

    driver.quit()

    # print(departure_time_map_price)

    write_to_csv(departure_time_map_price)


main()
