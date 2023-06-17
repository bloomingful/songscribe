import os
import csv
import sys
from dotenv import load_dotenv
from lyricsgenius import Genius

load_dotenv()

client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET")
# redirect_uri = os.getenv("REDIRECT_URI")

genius = Genius(client_id)

title = input("Enter song title: ")
artist = input("Enter song artist: ")

song = genius.search_song(title, artist)

lyrics = song.lyrics

filename = f"songscribe/tests/{title} - {artist}.txt"

with open(filename, 'w', encoding="utf-8") as f:
    f.write(lyrics)