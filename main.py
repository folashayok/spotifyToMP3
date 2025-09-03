
# 1. Imports and Configuration
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from secrets import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, YOUTUBE_API_KEY

# 2. Constants
SPOTIFY_SCOPE = "user-library-read"
YOUTUBE_SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CLIENT_SECRETS_FILE = "youtube_client_secret.json"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SPOTIFY_SCOPE
    ))
    return sp

def authenticate_youtube():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, YOUTUBE_SCOPES)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)
    return youtube

def get_spotify_info(sp, url):
    # For now, only handle track URLs
    try:
        info = sp.track(url)
        return info
    except Exception as e:
        print(f"Error fetching Spotify info: {e}")
        return None

def search_youtube(youtube, query):
    try:
        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=query
        )
        response = request.execute()
        return response
    except Exception as e:
        print(f"Error searching YouTube: {e}")
        return None

def main():
    # 3. User Input
    item_choice = input("Enter 1 for track, 2 for album, or 3 for playlist: ")
    track_url = input("Enter your Spotify URL: ")

    # 4. Spotify Data Retrieval
    sp = authenticate_spotify()
    info = get_spotify_info(sp, track_url)
    if not info:
        print("Could not retrieve Spotify info.")
        return
    print("Spotify info:", info)

    # 5. YouTube Search
    youtube = authenticate_youtube()
    # Use track name and artist for search query
    track_name = info.get('name', '')
    artist_name = info['artists'][0]['name'] if info.get('artists') else ''
    search_query = f"{track_name} {artist_name}"
    yt_response = search_youtube(youtube, search_query)
    print("YouTube search result:", yt_response)

    # 6. Download/Conversion (Optional)
    # ...future implementation...

    # 7. Output
    # ...additional output formatting...

if __name__ == "__main__":
    main()


