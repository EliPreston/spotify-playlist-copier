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

 # scope not needed here
SP = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        username = UID,
        redirect_uri = uri
    )
)


# gets public playlists from spotify account
# returns list of playlist objects
def get_playlists_other(uID_other: str) -> list:

    playlists = SP.user_playlists(uID_other)
    return playlists['items']


# copy a one playlist (passed as name and id into function)
def copy_single_playlist(pName: str, pID: str) -> None:

    print(f'> Copying playlist {pName} : {pID}')

    new_playlist_name = pName + '-copy'
    tracks_to_add = []
    tracks_to_add_titles = []
    loc_user_modify.create_playlist(UID, new_playlist_name)

    tracks = SP.playlist_items(pID)
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

    print('\n => Adding the following list of tracks: ', end="")
    print(tracks_to_add_titles)
    print("\n")

    loc_user_modify.add_to_new_playlist(tracks_to_add)
        

# prompt user if they want to copy the playlist
def prompt_user_copy(pName: str, pID: str) -> None:

    ask = input(f"Copy playlist {pName}? [Y/n] ")
    if (ask.lower() == 'y'):
        copy_single_playlist(pName, pID)


def copy_playlists(uID_other: str, prompting: bool) -> bool:

    try:
        playlists_to_copy = get_playlists_other(uID_other)
        displayname_other = SP.user(uID_other)['display_name']
        print(f'\nCopying {displayname_other}\'s playlists:')

        # Looping over playlists, 
        # creating new playlsit for current user, 
        # appending all songs from external playlist to new (local) playlist
        for playlist in playlists_to_copy:
            try:
                pName = playlist['name']
                pID = playlist['id']
                
                if (prompting):
                    prompt_user_copy(pName, pID)
                else:
                    copy_single_playlist(pName, pID)

            except Exception as e:
                print("> error with a playlist, continuing...")
                print(" => ", end="")
                print(e)
        
        print('Finished playlists, exiting.')
        return True


    except Exception as e:
        print(f'Error occured while copying: {e}')
        return False




