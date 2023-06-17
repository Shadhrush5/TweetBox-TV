import json

# Load the JSON file into a dictionary
with open('data.json', 'r') as file:
    data = json.load(file)

# Remove duplicates in the specific field
unique_field = set()
unique_data = []
for item in data:
    if item['text'] not in unique_field:
        unique_field.add(item['text'])
        unique_data.append(item)

# Write the unique data back to the JSON file
with open('data.json', 'w') as file:
    json.dump(unique_data, file, indent=4)

