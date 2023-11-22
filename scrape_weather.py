"""
Zach Lapointe
November 22 2023
Weather App
"""

from html.parser import HTMLParser
import urllib.request
from datetime import datetime
import json

class WeatherScraper(HTMLParser):
    """
    Represents the HTML parser.
    """
    def __init__(self):
        super().__init__()
        self.td = False
        self.a_tag = False
        self.tbody = False
        self.date_value = False
        self.month_end = False
        self.column = 1
        self.daily_temp = {}
        self.weather = {}
        self.last_month = False
        self.first_year = 1999
        self.first_month = datetime.now().month
        self.data_end = False
        self.day = 0

    def scrape_data(self):
        """
        helps scrape the data from the specified site starting on specified date
        """
        while not self.data_end:
            print(self.first_year)
            while self.first_month > 0 and not self.last_month:
                print(self.first_month)
                url = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?timeframe=2&StationID=27174&Year={self.first_year}&Month={self.first_month}&Day={1}'
                with urllib.request.urlopen(url) as response:
                    html = str(response.read())
                self.feed(html)
                self.first_month-=1
            self.first_year-=1
            self.first_month = 12
        if self.data_end:
            with open('test.txt', 'w') as myfile:
                myfile.write(json.dumps(self.weather))
            print(self.weather)

    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self.tbody = True
        if tag == "td":
            self.td = True
        if tag == "abbr":
            if str(self.first_year) in str(attrs):
                self.date_value = True
        if tag == "a":
            self.a_tag = True

    def handle_endtag(self, tag):
        if tag == "tbody":
            self.tbody = False
        if tag == "td":
            self.td = False
        if self.tbody and tag == "tr":
            self.column = 1
        if tag == "td":
            self.column += 1
        if tag == "abbr":
            self.date_value = False
        if tag == "a":
            self.a_tag = False