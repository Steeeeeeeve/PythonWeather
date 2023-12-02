import matplotlib.pyplot as plt
import random
# Be sure to install this - pip install matplotlib

class PlotOperations:
    def create_boxplot(self, data):
        plt.boxplot(data.values())
        plt.xlabel('Month')
        plt.ylabel('Temperature (Celsius)')
        plt.title('Monthly Temperature Distribution for 2013 to 2023')
        plt.xticks(range(1, len(data) + 1), data.keys())
        plt.show()

    def create_lineplot(self, month, year, data):
        plt.plot(range(1, len(data) + 1), data)
        plt.xlabel('Day of Month')
        plt.ylabel('Avg Daily Temp')
        plt.title(f'Mean Daily Temperature for {month} {year}')
        # plt.xticks(range(1, len(data) + 1), range(1, len(data) + 1)),
        plt.xticks(range(1, len(data) + 1), range(1, len(data) + 1), rotation=45, fontsize=8)
        plt.grid()
        plt.show()

# Calling it and testing
plotter = PlotOperations()

# Box plot
weather_data = {1: [round(random.uniform(-20, 5), 1) for _ in range(31)],
                2: [round(random.uniform(-18, 10), 1) for _ in range(10)],
                3: [round(random.uniform(-5, 15), 1) for _ in range(10)],
                4: [round(random.uniform(5, 20), 1) for _ in range(10)],
                5: [round(random.uniform(10, 20), 1) for _ in range(10)],
                6: [round(random.uniform(15, 30), 1) for _ in range(10)],
                7: [round(random.uniform(17, 35), 1) for _ in range(10)],
                8: [round(random.uniform(15, 30), 1) for _ in range(10)],
                9: [round(random.uniform(15, 25), 1) for _ in range(10)],
                10: [round(random.uniform(10, 15), 1) for _ in range(10)],
                11: [round(random.uniform(0, 10), 1) for _ in range(10)],
                12: [round(random.uniform(-5, 10), 1) for _ in range(10)]}
                #{1: [1.1, 5.5, 6.2, 7.1], 2: [8.1, 5.4, 9.6, 4.7],
                # 3: [2.3, 5.5, 6.4, 4.3], 4: [2.4, 3.6, 2.5, 8.6],
                # 5: [2.3, 5.5, 6.4, 4.3], 6: [2.4, 3.6, 2.5, 8.6],
                # 7: [2.3, 5.5, 6.4, 4.3], 8: [2.4, 3.6, 2.5, 8.6],
                # 9: [2.3, 5.5, 6.4, 4.3], 10: [2.4, 3.6, 2.5, 8.6],
                # 11: [2.3, 5.5, 6.4, 4.3], 12: [2.4, 3.6, 2.5, 8.6]}
plotter.create_boxplot(weather_data)

# Line plot
january_data = weather_data[1]
plotter.create_lineplot('January', 2023, january_data)
