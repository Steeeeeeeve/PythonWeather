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
    """
    Represents the Weather Processor where user feedback is given.
    """
    def __init__(self):
        self.conn = sqlite3.connect('weather.db')
        self.cursor = self.conn.cursor()

    def weather_menu(self):
        """
        This is the menu for the weather processor.
        """
        print("Weather Data")
        print("1. Download Full Weather Data.")
        print("2. Update Weather Data.")
        print("3. Show BoxPlot")
        print("4. Show LinePlot")
        print("5. Exit")

    def full_pull(self):
        """
        This does a full pull from todays date to the earliest date.
        """
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
        """
        This is used to update the weather data without scraping it all again.
        """
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

        with open(text_file, "r") as text_data:
            json_data = json.load(text_data)
            operations.save_data(json_data)

        for date in operations.fetch_data():
            print(f"Sample Date: {date[0]}, Location: {date[1]}, Min Temp: {date[2]}, Max Temp: {date[3]}, Average Temp: {date[4]}")
        print("Weather data updated.")

    def box_plot(self):
        """
        This initiates and sends the variables for the box plot.
        """
        self.cursor.execute("SELECT sample_date FROM weather ORDER BY DATE(sample_date) ASC LIMIT 1")
        first_year = int(str(self.cursor.fetchone()[0])[0:4])
        self.cursor.execute("SELECT sample_date FROM weather ORDER BY DATE(sample_date) DESC LIMIT 1")
        last_year = int(str(self.cursor.fetchone()[0])[0:4])
        while True:
            try:
                start_year = int(input(f"Enter a start year between {first_year} and {last_year}: "))
                if first_year <= start_year <= last_year:
                    break
                else:
                    print(f"Please enter a year between {first_year} and {last_year}.")
            except ValueError:
                print("Error: Enter a valid integer.")

        while True:
            try:
                end_year = int(input(f"Enter an end year between {first_year} and {last_year}: "))
                if first_year <= end_year <= last_year:
                    break
                else:
                    print(f"Please enter a year between {first_year} and {last_year}.")
            except ValueError:
                print("Error: Enter a valid integer.")

        data = []
        current_year = start_year
        while current_year <= end_year:
            self.cursor.execute(f"SELECT * FROM weather where sample_date LIKE '{current_year}-%-%'")
            data.append(self.cursor.fetchall())
            current_year+=1
        plot = PlotOperations()
        plot.create_boxplot(data, start_year, end_year)

    def line_plot(self):
        """
        line plot selects and calls up a line plot.
        """
        self.cursor.execute("SELECT sample_date FROM weather ORDER BY DATE(sample_date) ASC LIMIT 1")
        first_year = int(str(self.cursor.fetchone()[0])[0:4])
        self.cursor.execute("SELECT sample_date FROM weather ORDER BY DATE(sample_date) DESC LIMIT 1")
        last_year = int(str(self.cursor.fetchone()[0])[0:4])
        while True:
            try:
                year = int(input(f"Enter a year between {first_year} and {last_year}: "))
                if first_year <= year <= last_year:
                    break
                else:
                    print(f"Please enter a year between {first_year} and {last_year}.")
            except ValueError:
                print("Error: Enter a valid integer.")

        while True:
            try:
                month = int(input(f"Enter a month between 1 and 12: "))
                if 1 <= month <= 12:
                    break
                else:
                    print(f"Please enter a month between 1 and 12.")
            except ValueError:
                print("Error: Enter a valid integer.")
        db = DBOperations("weather.db")
        query = f"SELECT * FROM weather WHERE sample_date LIKE '{year}-{month}-%'"
        self.cursor.execute(query)
        data_list = self.cursor.fetchall()
        if not data_list:
            print(f"No data available for {month}/{year}.")
            return
        plotter = PlotOperations()
        plotter.create_lineplot(data_list, month, year)


    def user_choice(self, choice):
        """
        This handles the users choice in the dialogue.
        """
        if choice == 1:
            self.full_pull()
        elif choice == 2:
            self.update_weather()
        elif choice == 3:
            self.box_plot()
        elif choice == 4:
            self.line_plot()
        elif choice == 5:
            self.conn.close()
            exit()
        else:
            print("Invalid selection, try again.")

    def process(self):
        """
        This initiates the weather menu when called.
        """

        self.weather_menu()
        try:
            user_selection = int(input("Enter an option(1-5): "))
            self.user_choice(user_selection)
        except ValueError:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    weather_processor = WeatherProcessor()
    weather_processor.process()
