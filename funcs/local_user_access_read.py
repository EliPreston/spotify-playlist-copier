# external dependancies for current file
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

# local dependancies
# N/A


# commonly used env variables
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
UID = os.environ['USERNAME']
uri = os.environ['REDIRECT_URI']


scope = 'playlist-read-private' # read private playlists
SP = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id = CLIENT_ID,
            client_secret = CLIENT_SECRET,
            username = UID,
            redirect_uri = uri,
            scope = scope
        )
    )


# gets personal playlists
# returns list of playlist objects
def get_playlists_personal(uID: str) -> list:

    playlists = SP.user_playlists(uID) # limited to 50 playlists at a time
    return playlists['items']


# gets most recently created personal playlist
# returns ID of playlist
def get_most_recent_playlist(uID: str) -> str:

    playlists = SP.user_playlists(uID, limit = 1) # explicitly limit to 1 because that's all we want
    return playlists['items'][0]['id']