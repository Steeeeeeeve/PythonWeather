"""
Cedric Pereira, Steven Hurkett, Zack Bowles-Lapointe
November 22 2023
Weather App - scraper page
"""

import json
import sqlite3
import sys
from DBCM import DBCM
import matplotlib.pyplot as plt
from collections import defaultdict
from db_operations import DBOperations

class PlotOperations:
    def create_boxplot(self, data):
        plt.boxplot(data.values())
        plt.xlabel('Month')
        plt.ylabel('Temperature (Celsius)')
        plt.title(f'Monthly Temperature Distribution')
        plt.xticks(range(1, len(data) + 1), data.keys())
        plt.show()


    def create_lineplot(self, data_list, month, year):
        days = [item[1] for item in data_list]
        temperatures = [item[4] for item in data_list] 
        plt.plot(days, temperatures)
        plt.xlabel('Day of Month')
        plt.ylabel('Avg Daily Temp')
        plt.title(f'Mean Daily Temperature for {month}, {year}')
        plt.xticks(days, rotation=45, fontsize=8)
        plt.grid()
        plt.show()
