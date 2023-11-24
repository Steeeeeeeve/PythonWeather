import sqlite3
from DBCM import DBCM
import json

class DBOperations:
    def __init__(self, database='weather.db'):
        self.database = database

    def initialize_db(self):
        with DBCM(self.database) as create:
            create.execute('''
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sample_date TEXT UNIQUE,
                    location TEXT,
                    min_temp REAL,
                    max_temp REAL,
                    avg_temp REAL
                )
            ''')
                
    def fetch_data(self):
        with DBCM(self.database) as fetch:
            fetch.execute('SELECT sample_date, location, min_temp, max_temp, avg_temp FROM weather')
            return fetch.fetchall()

    def save_data(self, scrape_weather):
        with DBCM(self.database) as new_data_finder:
            for sample_date, data in scrape_weather.items():
                location = "Winnipeg"
                min_temp = data["Min"]
                max_temp = data["Max"]
                avg_temp = data["Mean"]

                new_data_finder.execute('''
                    INSERT OR IGNORE INTO weather (sample_date, location, min_temp, max_temp, avg_temp)
                        VALUES (?, ?, ?, ?, ?)
                ''', (sample_date, location, min_temp, max_temp, avg_temp))

    def purge_data(self):
        with DBCM(self.database) as purge:
            purge.execute('DELETE FROM weather')
    

#Commands
db = DBOperations("weather.db")
db.initialize_db()
with open("test.txt", "r") as data_file:
    json = json.load(data_file)
    db.save_data(json) 
print(db.fetch_data())

