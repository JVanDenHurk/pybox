import json

# Load the JSON data from the file
with open('cleaned_secret_scripts_copy.json', 'r') as file:
    data = json.load(file)

# Iterate through each item in the JSON data
for key, value in data.items():
    # Modify the text by adding newline characters where needed
    value['text'] = value['text'].replace('. ', '.\n\n')

# Write the modified JSON data back to the file
with open('cleaned_secret_scripts_copy.json', 'w') as file:
    json.dump(data, file, indent=4)