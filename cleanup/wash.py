import json
from bs4 import BeautifulSoup

# Function to clean HTML and keep only image tags with alt text
def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove all tags except <img>
    for tag in soup.find_all(True):  # True matches all tags
        if tag.name != 'img':
            tag.unwrap()  # Unwrap removes the tag but keeps its content

    # Return the cleaned HTML as a string
    return str(soup)

# Load JSON data from file
with open('secret_scripts.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Clean each text entry in the JSON
for key, value in data.items():
    raw_html = value['text']
    cleaned_text = clean_html(raw_html)
    data[key]['text'] = cleaned_text

# Save the cleaned JSON data back to file
with open('cleaned_secret_scripts.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print("Cleaned data has been saved to cleaned_secret_scripts.json")
