from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv
from csv import DictWriter
import os
from datetime import datetime


def get_current_date():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # insert current date time
    date_list = list()
    date_list.append(dt_string)
    return date_list[0]


def write_to_csv(ticket_price_dict):
    departure_time_key = []
    price_values = []
    fields_name = ['Request On', 'Departure - Destination', 'Date', 'Slot 1',
                   'Slot 2', 'Slot 3', 'Slot 4', 'Slot 5', 'Slot 6', 'Slot 7', 'Slot 8', 'Slot 9']
    try:
        if os.path.isfile('Tickets.csv') is False:
            init_set = {
                "Request On": "",
                "Departure - Destination": "",
                "Date": "",
                "Slot 1": [],
                "Slot 2": [],
                "Slot 3": [],
                "Slot 4": [],
                "Slot 5": [],
                "Slot 6": [],
                "Slot 7": [],
                "Slot 8": [],
                "Slot 9": [],
            }
            map_to_csv = pd.DataFrame.from_dict(
                init_set)
            map_to_csv.to_csv('Tickets.csv', index=False)

            for keys, values in ticket_price_dict.items():
                departure_time_key.append(keys)
                price_values.append(values[0])
            with open('Tickets.csv', 'a+', newline='') as write_obj:
                dict_writer = DictWriter(write_obj, fieldnames=fields_name)
                dict_writer.writerow(ticket_price_dict)
                print('CSV file created.')
        else:
            for keys, values in ticket_price_dict.items():
                departure_time_key.append(keys)
                price_values.append(values[0])
            with open('Tickets.csv', 'a+', newline='') as write_obj:
                dict_writer = DictWriter(write_obj, fieldnames=fields_name)
                dict_writer.writerow(ticket_price_dict)
                print('CSV file updated.')
    except Exception as e:
        raise e


def input_request():
    input_list = []

    departure = input("Departure code: ").upper()
    input_list.append(departure)
    destination = input("Destination code: ").upper()
    input_list.append(destination)
    departure_date = input("Departure date in Y-M-D format: ")
    input_list.append(departure_date)
    return input_list


def main():

    input_response = input_request()

    webdriver = r'/usr/local/bin/chromedriver'

    driver = Chrome(executable_path=webdriver)

    # URL = 'https://www.airasia.com/select/en/gb/JHB/PEN/2020-04-30/N/1/0/0/O/N/MYR/ST'

    format_url = 'https://www.airasia.com/select/en/gb/' + \
        input_response[0]+'/'+input_response[1]+'/' + \
        input_response[2]+'/N/1/0/0/O/N/MYR/ST'

    driver.get(format_url)
    # driver.get(URL)

    # execute script to scroll down the page
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # sleep for 30s
    time.sleep(10)

    # ticket price list
    price_elements = []
    departure_time_list = []
    departure_time_map_price = {}
    departure_destination_list = []
    departure_date_list = []
    count = 0

    departure_time_map_price["Request On"] = get_current_date()
    departure_destination_list.append(input_response[0] +
                                      ' - ' + input_response[1])
    departure_date_list.append(input_response[2])
    departure_time_map_price["Departure - Destination"] = departure_destination_list[0]
    departure_time_map_price["Date"] = departure_date_list[0]

    content_wrapper = driver.find_elements_by_class_name('section-content')

    for content in content_wrapper:
        amount = content.find_element_by_class_name('fare-amount')
        price_elements.append(amount.text)
        departure_time = driver.find_elements_by_id(
            'departing-time-desc-0-'+str(count))
        departure_time_list.append(departure_time[0].text)
        count += 1
        price_list = list()
        price_list.append(departure_time[0].text + " - " + " RM "+amount.text)
        departure_time_map_price["Slot "+str(count)] = price_list[0]

    driver.quit()

    if not price_elements:
        print("Requested URL is invalid. Please check.")
    else:
        write_to_csv(departure_time_map_price)

    # print(departure_time_map_price)


main()
