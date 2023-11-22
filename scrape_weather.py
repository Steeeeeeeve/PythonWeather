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
