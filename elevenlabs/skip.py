import os
import json
import pandas as pd
from gradio_client import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to convert text to audio using Coqui XTTS on Hugging Face Spaces
def convert_text_to_audio(text):
    client = Client("https://coqui-xtts.hf.space/--replicas/4accn/")
    try:
        result = client.predict(
            text,  # Text Prompt
            "en,en",  # Language (change as needed)
            "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",  # Reference Audio
            "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",  # Use Microphone for Reference
            True,  # Use Microphone
            True,  # Cleanup Reference Voice
            True,  # Do not use language auto-detect
            True,  # Agree
            fn_index=1
        )
        audio_url = result[1]  # Synthesised Audio URL
        audio_data = requests.get(audio_url).content
        return audio_data
    except Exception as e:
        print(f"Error during prediction: {e}")
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
