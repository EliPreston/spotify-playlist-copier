# external dependancies for current file
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

# local dependancies
import funcs.local_user_access_read as local_user_access_read


# commonly used env variables
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
UID = os.environ['USERNAME']
uri = os.environ['REDIRECT_URI']


scope = 'playlist-modify-private'
SP = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        username = UID,
        redirect_uri = uri,
        scope = scope
    )
)

# ------------


# create playlist with name playlist_name, returns nothing
def create_playlist(uID: str, playlist_name: str) -> None:

    playlists = SP.user_playlist_create(uID, playlist_name, public = False)
    return



def add_to_new_playlist(tracks: list) -> None:

    new_pID = local_user_access_read.get_most_recent_playlist(UID)
    SP.user_playlist_add_tracks(UID, new_pID, tracks = tracks)
    return
