from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import time

webdriver = r'/usr/local/bin/chromedriver'

driver = Chrome(executable_path=webdriver)

# URL = 'http://quotes.toscrape.com/js/page/1/'
URL = 'https://www.airasia.com/select/en/gb/JHB/PEN/2020-04-30/N/1/0/0/O/N/MYR/ST'

driver.get(URL)

# execute script to scroll down the page
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(10)

price_element = driver.find_element_by_xpath(
    '//*[@id="lf-low-amount-desc-0-0"]')

price = price_element.text

print(price)

driver.quit()
