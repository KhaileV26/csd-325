
print("Welcome to the Sitka Weather Menu!")
import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Read dates, high, & low temperatures
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)


# Display the menu until the user chooses Exit.

while True:
    print("\nSITKA WEATHER MENU")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        # Plot the high temperatures in red.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == 2:
        # Plot the low temperatures in blue.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == 3:
        print("\nThank you for using the Sitka Weather Program. Goodbye!")
        sys.exit()

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")
