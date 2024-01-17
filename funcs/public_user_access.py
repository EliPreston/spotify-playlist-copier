# external dependancies current file
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

# local dependancies
import funcs.local_user_access_modify as loc_user_modify


# commonly used env variables
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
UID = os.environ['USERNAME']
uri = os.environ['REDIRECT_URI']



# gets public playlists from spotify account
# returns list of playlist objects
def get_playlists_other(sp: spotipy.client.Spotify, uID_other: str) -> list:

    playlists = sp.user_playlists(uID_other)
    return playlists['items']


def copy_playlists(uID_other: str):

    # scope not needed here
    sp = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id = CLIENT_ID,
            client_secret = CLIENT_SECRET,
            username = UID,
            redirect_uri = uri
        )
    )    

    playlists_to_copy = get_playlists_other(sp, uID_other)
    displayname_other = sp.user(uID_other)['display_name']
    print(f'Copying {displayname_other}\'s playlists:')

    # Looping over playlists, 
    # creating new playlsit for current user, 
    # appending all songs from external playlist to new (local) playlist
    for playlist in playlists_to_copy:

        try:
            pName = playlist['name']
            pID = playlist['id']
            print(f'> Copying playlist {pName} : {pID}')


            new_playlist_name = pName + '-copy'
            tracks_to_add = []
            tracks_to_add_titles = []
            loc_user_modify.create_playlist(UID, new_playlist_name)

            tracks = sp.playlist_items(pID)
            for item in tracks['items']:

                try:
                    trackName = item['track']['name']
                    trackID = item['track']['id']
                    # print(f'{trackName} : {trackID}')

                    if trackID != None:
                        tracks_to_add.append(trackID)
                        tracks_to_add_titles.append(trackName)

                except Exception as e:
                    print(" => error encountered with a track, passing over")
                    print("  --> ", end="")
                    print(e)

            print(' => Adding the following list of tracks: ', end="")
            print(tracks_to_add_titles)
            print("\n")

            loc_user_modify.add_to_new_playlist(tracks_to_add)
        
        except Exception as e:
            print("> error with a playlist, continuing...")
            print(" => ", end="")
            print(e)
    
    print('All playlists copied')
        




