import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="user-library-read"))

item_choice = input("Enter 1 for track, 2 for album, or 3 for playlist")
#track_url = "https://open.spotify.com/track/2fQxE0jVrjNMT9oJAXtSJR?si=498df3b185134f52"
track_url = input("Enter your Spotify URL:")
info = sp.track(track_url)
print(info['name'])


