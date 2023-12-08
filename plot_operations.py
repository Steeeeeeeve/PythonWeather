"""
Cedric Pereira, Steven Hurkett, Zack Bowles-Lapointe
November 22 2023
Weather App - scraper page
"""

from DBCM import DBCM
import matplotlib.pyplot as plt

class PlotOperations:
    def create_boxplot(self, data_list, start_year, end_year):
        monthly_temps = {}
        for item in data_list[0]:
            date, avg_temp = str(item[1]).rstrip('-'), item[5]
            month_raw = date[5:7]
            month = int(str(month_raw).rstrip('-'))

            if month not in monthly_temps:
                monthly_temps[month] = []

            monthly_temps[month].append(avg_temp)

        data_months = sorted(monthly_temps.keys())

        plt.boxplot([monthly_temps[month] for month in data_months])
        plt.xlabel('Month')
        plt.ylabel('Temperature (Celsius)')
        plt.title(f'Monthly Temperature Distribution from {start_year} to {end_year}')
        plt.xticks(range(1, len(data_months) + 1), [f'{month}' for month in data_months])
        plt.show()


    def create_lineplot(self, data_list, month, year):
        month_names = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        days = [item[1] for item in data_list]
        temperatures = [item[4] for item in data_list] 
        month_pretty = month_names.get(month, 'Invalid Month')
        plt.plot(days, temperatures)
        plt.xlabel('Day of Month')
        plt.ylabel('Avg Daily Temp')
        plt.title(f'Mean Daily Temperature for {month_pretty}, {year}')
        plt.xticks(days, rotation=45, fontsize=8)
        plt.grid()
        plt.show()

