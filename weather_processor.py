"""
Cedric Pereira, Steven Hurkett, Zack Bowles-Lapointe
December 6 2023
Weather App - User Interaction
"""
 
import sqlite3
import json
from datetime import datetime, timedelta
from scrape_weather import WeatherScraper
from db_operations import DBOperations
from plot_operations import PlotOperations

class WeatherProcessor:
    def __init__(self):
        self.conn = sqlite3.connect('weather.db')
        self.cursor = self.conn.cursor()

    def weather_menu(self):
        print("Weather Data")
        print("1. Download Full Weather Data.")
        print("2. Update Weather Data.")
        print("3. Exit")

    def full_pull(self):
        print("Getting fresh data...")
        today = datetime.now().date()

        text_file = "test.txt"
        url = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?timeframe=2&StationID=27174&Year={today.year}&Month={today.month}&Day={1}'
        scraper = WeatherScraper(url)
        operations = DBOperations(weather.db)

        scraper.scrape_data()
        operations = DBOperations(weather.db)
        operations.initialize_db()
        operations.purge_data()
        with open(text_file, "r") as text_data:
            json_data = json.load(text_data)
            operations.save_data()
        
        print("Full download completed")
    
    def update_weather(self):
        print("Updating weather data, please wait...")
        today = datetime.now().date()
        self.cursor.execute("SELECT MAX(date) FROM weather")
        last_update = self.cursor(fetchone()[0])
        days_missing = (today - last_update).days

        text_file = "test.txt"
        url = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?timeframe=2&StationID=27174&StartYear={last_update.year}&StartMonth{last_update.month}&StartDay={last_update.day}&EndYear={today.year}Year={today.year}&Month={today.month}&Day={1}'
        scraper = WeatherScraper(url)

        with open(text_file, "r") as text_data:
            json_data = json.load(text_data)
            operations.save_data
        print("Weather data updated.")

    def user_choice(self, choice):
        if choice == 1:
            self.full_pull()
        elif choice == 2:
            self.update_weather()
        elif choice == 3:
            self.conn.close()
            exit()
        else:
            print("Invalid selection, try again.")

    def process(self):
        while True:
            self.weather_menu()
            try:
                user_selection = int(input("Enter an option(1-3): "))
                self.user_choice(user_selection)
            except ValueError:
                print("Invalid selection, try again.")

if __name__ == "__main__":
    weather_processor = WeatherProcessor()
    weather_processor.process()
    
        
