import os
import numpy as np
import torch
from bark import SAMPLE_RATE, generate_audio, preload_models
import soundfile as sf

# Set environment variables to reduce VRAM usage
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

# Set device to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Function to get the next script number
def get_next_script_number(directory, base_name="script"):
    existing_files = os.listdir(directory)
    numbers = [int(file.split('.')[0].replace(base_name, '')) for file in existing_files if file.startswith(base_name) and file.split('.')[0].replace(base_name, '').isdigit()]
    return max(numbers) + 1 if numbers else 1

# Create the output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Get the next script number
script_number = get_next_script_number(output_dir)
file_name = f"script{script_number}.wav"
file_path = os.path.join(output_dir, file_name)

# Download and load all models
preload_models()

# Generate audio from text with GPU support
text_prompt = """
     We see nothing but omnipresent mist...\n\nIf you're reading this script, it means that something has gone wrong.\n\nNo path leads to this script - maybe you started reading the Secret Scripts book from the beginning, which is against the rules.\n\nDuring the game, you will be pointed to read certain scripts - search for the script's number, then read it and resolve all its effects.\n\nStop reading now and go back to your game.
"""

# Assuming generate_audio can take a device argument
audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_3")

# Ensure the audio array is in the correct format
audio_array = np.array(audio_array)

# Save the audio as a WAV file using soundfile
sf.write(file_path, audio_array, SAMPLE_RATE)

print(f"Audio saved successfully to {file_path}")