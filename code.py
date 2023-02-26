import csv
import json
import datetime

# Create a dictionary to store pomodoros and minutes for each date
data = {}

# Open the CSV file and read the data
with open('history.csv') as f:
    reader = csv.reader(f)
    next(reader) # Skips the first row
    for row in reader:
        # Extract the date and time from the first column of the CSV data
        dt = datetime.datetime.strptime(row[0][:10], '%Y-%m-%d')
        date = dt.strftime('%Y-%m-%d')
        time_in_sec = int(row[5])

        # Check if the date already exists in the dictionary
        if date in data:
            data[date]['pomodoros'] += 1
            data[date]['minutes'] += time_in_sec // 60
        else:
            # Add the date to the dictionary with initial values
            data[date] = {'pomodoros': 1, 'minutes': time_in_sec // 60, 'weekday': dt.strftime('%A')}

# Write the data to a JSON file
with open('output.json', 'w') as f:
    json.dump(data, f)
