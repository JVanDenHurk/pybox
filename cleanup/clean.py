import json
from bs4 import BeautifulSoup

# Function to clean HTML by replacing img tags with alt text and removing other tags
def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Replace <img> tags with their alt text
    for img in soup.find_all('img'):
        alt_text = img.get('alt', '')
        img.replace_with(alt_text)

    # Remove all remaining tags and get text content
    cleaned_text = soup.get_text(separator="\n").strip()

    # Remove extra spaces and newlines
    cleaned_text = ' '.join(cleaned_text.split())

    return cleaned_text

# Load JSON data from file
with open('washed_secret_scripts.json', 'r', encoding='utf-8') as file:
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
