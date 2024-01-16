# Spotify Playlist Copier
*This program automates copying many playlists into your own library where you can modify them*


### Dependancies (modules)
- os
- spotipy
    - SpotifyOAuth (from spotipy.oauth2 import SpotifyOAuth)
- dotenv
    - load_dotenv (from dotenv import load_dotenv)


### Setup and Usage
1. Install modules via pip, brew, etc. 
2. Create or login to the spotify developer console
    a. Go to dashboard > click on "Create app" > fill out information & select "Web API" as the API/SDK you will use
    b. Create your .env file in the same directory as main.py and add the following variables
        - CLIENT_ID = ''
        - CLIENT_SECRET = ''
        - USERNAME = ''
        - REDIRECT_URI = ''
    c. Click on your newly created project > click on "Settings" and copy your Client ID & Client Secret into the corresponding variables in the .env file
    d. Similarily, your username (which is actually your user ID) goes into the USERNAME variable, and the redirect uri should match what you entered when setting up the app in step 2a (ex. http://localhost:3000)
3. Get the user ID of the person you want to copy playlists from 
    a. This can be done by clicking on their profile > the three dots next to the "following" button > the "Copy link to profile" option
    b. Pasting this into a text file (or wherever) and copying the characters after the '...user/' and before the '?....'
4. Run main.py and paste the user ID when prompted