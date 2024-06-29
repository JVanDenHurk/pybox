import pandas as pd
import json

# Read JSON data from file
with open('secret_scripts.json', 'r') as f:
    data = json.load(f)

# Initialize empty lists to store IDs and text sections
ids = []
texts = []

# Extract IDs and "text" sections from the JSON data
for key, value in data.items():
    ids.append(key)
    texts.append(value['text'])

# Create a DataFrame from the IDs and text sections
df = pd.DataFrame({'ID': ids, 'Text': texts})

# Write DataFrame to Excel file
df.to_excel('output.xlsx', index=False)
