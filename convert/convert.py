from pydub import AudioSegment

# Load the WAV file
wav_file_path = './input/Watch out for the mercha 1.wav'
audio = AudioSegment.from_wav(wav_file_path)

# Define the output MP3 file path
mp3_file_path = './output/script128.mp3'

# Export the audio to MP3 format
audio.export(mp3_file_path, format='mp3')

mp3_file_path
