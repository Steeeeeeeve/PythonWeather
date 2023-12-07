"""
Cedric Pereira, Steven Hurkett, Zack Bowles-Lapointe
December 6 2023
Weather App - User Interaction
"""
 
import sqlite3
import json
from datetime import datetime
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
        print("3. Show BoxPlot")
        print("4. Exit")

    def full_pull(self):
        print("Getting fresh data...")

        today = datetime.now().date()
        text_file = "test.txt"
        url = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?timeframe=2&StationID=27174&EndYear=1996&EndMonth=10&StartYear={today.year}&StartMonth={today.month}&Year={today.year}&Month={today.month}&Day={1}'
        scraper = WeatherScraper(url)
        scraper.scrape_data()
        operations = DBOperations("weather.db")
        operations.initialize_db()
        operations.purge_data()
        with open(text_file, "r") as text_data:
            json_data = json.load(text_data)
            operations.save_data(json_data)
        for date in operations.fetch_data():
            print(f"Sample Date: {date[0]}, Location: {date[1]}, Min Temp: {date[2]}, Max Temp: {date[3]}, Average Temp: {date[4]}")
        print("Full download completed")
    
    def update_weather(self):
        print("Updating weather data, please wait...")
        today = datetime.now().date()
        self.cursor.execute("SELECT sample_date FROM weather ORDER BY DATE(sample_date) DESC LIMIT 1")
        last_update_string = self.cursor.fetchone()[0]
        last_month_raw = last_update_string[5:7]
        last_month = last_month_raw.rstrip('-')
        last_year = last_update_string[0:4]
        text_file = "test.txt"
        url = f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?timeframe=2&StationID=27174&EndYear={last_year}&EndMonth={last_month}&StartYear={today.year}&StartMonth={today.month}&Year={today.year}&Month={today.month}&Day={1}'
        scraper = WeatherScraper(url)
        scraper.scrape_data()
        operations = DBOperations("weather.db")
        operations.initialize_db()

    def box_plot(self):
        db = DBOperations("weather.db")
        plot = PlotOperations()
        data = db.fetch_data()
        plot.create_boxplot(data)


        with open(text_file, "r") as text_data:
            json_data = json.load(text_data)
            operations.save_data(json_data)

        for date in operations.fetch_data():
            print(f"Sample Date: {date[0]}, Location: {date[1]}, Min Temp: {date[2]}, Max Temp: {date[3]}, Average Temp: {date[4]}")
        print("Weather data updated.")

    def user_choice(self, choice):
        if choice == 1:
            self.full_pull()
        elif choice == 2:
            self.update_weather()
        elif choice == 3:
            self.box_plot()
        elif choice == 4:
            self.conn.close()
            exit()
        else:
            print("Invalid selection, try again.")

    def process(self):
    
        self.weather_menu()
        try:
            user_selection = int(input("Enter an option(1-4): "))
            self.user_choice(user_selection)
        except ValueError:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    weather_processor = WeatherProcessor()
    weather_processor.process()
    
        
