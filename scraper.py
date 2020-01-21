from selenium.webdriver import Chrome
import pandas as pd

webdriver = r'/usr/local/bin/chromedriver'

driver = Chrome(executable_path=webdriver)

# URL = 'http://quotes.toscrape.com/js/page/1/'
URL = 'https://www.airasia.com/select/en/gb/JHB/PEN/2020-04-30/N/1/0/0/O/N/MYR/ST?key=4e8837c2-3b85-11ea-bd63-c724cbdfa8891579525432.25'

driver.get(URL)
