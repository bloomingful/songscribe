import genius_fetch as gf
from music_tag import load_file

# Load the mp3 file
audio_file = load_file('Evanescence - Lithium.mp3')

# Read the lyrics from a text file
with open('path/to/lyrics/file.txt', 'r') as f:
    lyrics = f.read()

# Set the lyrics tag
audio_file['lyrics'] = lyrics

# Save the changes to the file
audio_file.save()