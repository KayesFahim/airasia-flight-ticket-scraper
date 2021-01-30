# Project Intro

A terminal based program written in Python for web scraping against AirAsia flight tickets (for educational purpose). The result will be output as CSV formatted file.

# Setup

- Environment setup

```
from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv
from csv import DictWriter
import os
from datetime import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
```

## Activating a virtual environment

- On macOS and Linux:

```
source env/bin/activate
```

- On Windows

```
.\env\Scripts\activate
```
