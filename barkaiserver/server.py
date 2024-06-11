from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import numpy as np
from bark import SAMPLE_RATE, generate_audio
import soundfile as sf

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

@app.route('/generate-speech', methods=['POST'])
def generate_speech():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        print(f"Generating speech for text: {text}")
        audio_array = generate_audio(text)
        
        # Save audio to a file for verification
        sf.write('output.wav', audio_array, SAMPLE_RATE)
        
        return jsonify({'audio': audio_array.tolist()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Test text route
@app.route('/test-text', methods=['GET'])
def test_text():
    test_text = "Really? Nothing? Nothing at all? We pass the beast, still gliding into the ever-increasing emptiness of outer space.\n\nFrom here on out, we are alone and there is nothing in front of us.\n\nFailure.\n\nReturn all cards and tiles of this Dream (except for those already gained by Dreamers or added to the game decks) to the Secrets.\n\nKeep the Dream Gate tile of this Dream - you can still come back here to try again.\n\nChange the Season to Season of Plague .\n\nReveal the 2 Starting Slumber Map tiles and place the Dreamers in start spaces.\n\nYou are back on the Dreamworld Map."
    return jsonify({'text': test_text}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
