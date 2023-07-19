import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URL = "http://example.com"
SCOPE = "playlist-modify-private"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{BILLBOARD_URL}{date}")
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")

songs = [song.text.strip() for song in soup.select("h3.c-title.a-no-trucate")]
artists = [artist.text.strip() for artist in soup.select("span.c-label.a-no-trucate")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URL,
        scope=SCOPE,
    ))

current_user = sp.current_user()

tracks_uris = []

for i in range(len(songs)):
    tracks = sp.search(q=f"track:{songs[i]} artist:{artists[i]}", type="track")
    try:
        tracks_uris.append(f'spotify:track:{tracks["tracks"]["items"][0]["id"]}')
    except IndexError:
        print(f"track {songs[i]} artist:{artists[i]} not found.")

playlist = sp.user_playlist_create(user=current_user.get("id"), name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist.get("id"), items=tracks_uris)
