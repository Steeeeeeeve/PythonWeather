from html.parser import HTMLParser
from datetime import date
import urllib.request

day = date.day
month = date.month
year = date.year
url = "http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=",year,"&Day=",day,"&Year=",year,"&Month=5"
class WeatherScraper(url):
    