import os
import csv
import json

csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
json_file = 'data.json'

data = []
for csv_file in csv_files:
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)

