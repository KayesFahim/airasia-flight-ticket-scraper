## Project Intro:

A terminal based program written in Python for web scraping against [AirAsia](https://www.airasia.com/en/gb) flight tickets (for educational purpose). The ticket price will be capture based on the departure code and date, and output the result as CSV format.

## Platform/Tools:

Python 3.8.2, selenium, pandas, BeautifulSoup, ChromeDriverManager

## Running the application:

- Activating the virtual environment

  - on macOS or Linux:

  ```
    source env/bin/activate
  ```

  - On Windows

  ```
    .\env\Scripts\activate
  ```

- Install dependencies

```
pip3 install requirements.txt
```

- Execute script

```
python3 scraper.py
```
