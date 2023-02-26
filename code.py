import csv
import json
from collections import defaultdict
from datetime import datetime

# Create a dictionary to store pomodoros and minutes for each date
data = defaultdict(lambda: {"pomodoros": 0, "minutes": 0})

# Open the CSV file and read the data
with open('input.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        # Extract the date and time from the first column of the CSV data
        dt = datetime.strptime(row[0][:10], '%Y-%m-%d')
        date = dt.strftime('%Y-%m-%d')
        time_in_sec = int(row[5])

        # Add the values to the dictionary
        data[date]['pomodoros'] += 1
        data[date]['minutes'] += time_in_sec // 60
        data[date]['weekday'] = dt.strftime('%A')

# Write the data to a JSON file
with open('output.json', 'w') as f:
    json.dump(data, f)
