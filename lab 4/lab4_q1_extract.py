import math
import csv

# Step 1: Extract data from the log file and store it in a dictionary
data = {}  # Dictionary to store trial data

with open('fitts_experiment_results.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=' ')
    for row in csv_reader:
        amplitude = int(row[1])
        width = int(row[2])
        selection_number = int(row[3])
        time = float(row[4]) / 1000  # Convert time to seconds
        key = (amplitude, width)
        
        if key not in data:
            data[key] = []
        
        data[key].append(time)

# Step 2: Calculate the average time for each combination of amplitude and width after removing outliers
summary_data = []  # List to store summary data

for key, times in data.items():
    if len(times) >= 3:  # Ignore combinations with fewer than 3 trials
        mean_time = sum(times[2:]) / (len(times) - 2)  # Ignore the first two trials
        amplitude, width = key
        id_value = math.log2((amplitude / width) + 1)
        summary_data.append((id_value, mean_time))

# Step 3: Group results by ID and write the summary data to a file "summary.csv"
grouped_data = {}  # Dictionary to store grouped data

for id_value, mean_time in summary_data:
    if id_value not in grouped_data:
        grouped_data[id_value] = []
    grouped_data[id_value].append(mean_time)

# Calculate the mean time for each ID
summary_grouped_data = [(id_value, sum(times) / len(times)) for id_value, times in grouped_data.items()]

# Write the grouped summary data to "summary.csv"
with open('summary.csv', 'w', newline='') as summary_file:
    csv_writer = csv.writer(summary_file)
    csv_writer.writerow(["ID", "mean time"])
    
    for row in summary_grouped_data:
        csv_writer.writerow(row)
