import os
import json
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to convert text to audio using ElevenLabs API
def convert_text_to_audio(text):
    # Get API key from environment variable
    api_key = os.environ.get('ELEVENLABS_API_KEY')

    if not api_key:
        raise ValueError("ELEVENLABS_API_KEY environment variable is not set.")

    # ID of the voice to be used for speech
    voice_id = 'piTKgcLEGmPE4e6mEKli'

    # API endpoint
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'

    # Request headers
    headers = {
        'Content-Type': 'application/json',
        'xi-api-key': api_key
    }

    # Request data
    data = {
        'text': text
    }

    # Send POST request to ElevenLabs API
    response = requests.post(url, json=data, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        return response.content
    else:
        # Print the response for debugging purposes
        print(f"Error: Received status code {response.status_code}")
        print(f"Response: {response.text}")
        raise ValueError(f"Failed to generate audio for text: {text}")

# Ensure 'output' directory exists
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read skip_indices list from JSON file
with open('skip_indices.json', 'r') as f:
    skip_indices = json.load(f)

# Read data from Excel file
df = pd.read_excel('output.xlsx')

# Process each row from index 3 to 1232
for index in range(2, 1232):  # Index 2 corresponds to the third row in DataFrame
    script_number = index + 1

    # Skip if the script number is in the skip list
    if script_number in skip_indices:
        print(f"Skipping script{script_number}.")
        continue

    script_name = f'{output_dir}/script{script_number}.mp3'

    # Check if file already exists
    if os.path.exists(script_name):
        print(f"Audio file for script{script_number} already exists. Skipping.")
        continue

    text = df.iloc[index]['Text']
    try:
        audio_data = convert_text_to_audio(text)
    except ValueError as e:
        print(e)
        print(f"Stopping script due to failure in script{script_number}")
        break
    
    if audio_data:
        # Save the audio file
        with open(script_name, 'wb') as f:
            f.write(audio_data)
        print(f"Audio file for script{script_number} generated successfully.")
    else:
        print(f"Failed to generate audio for script{script_number}.")
