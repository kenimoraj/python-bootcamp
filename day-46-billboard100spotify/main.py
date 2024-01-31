import os

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pprint

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDIRECT_URI = os.environ["REDIRECT_URI"]


#Log into Spotify

scope = "playlist-modify-private"
soauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)

##Checking if token expired
with open("./token.txt", "r") as token_file:
    token_str = token_file.read()
    token_str = token_str.replace('\'','\"')
    print(token_str)
    token_info = json.loads(token_str)


if token_info == {} or soauth.is_token_expired(token_info):
    token_info = soauth.get_access_token()
    with open("./token.txt", "w") as token_file:
        token_file.write(str(token_info))

sp = spotipy.Spotify(auth_manager=soauth)
current_user = sp.current_user()

#Get songs
# date = input("Pick a date (YYYY-MM-DD): ")
date = "1994-04-12"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs = [song.getText().strip() for row in rows for song in row.find("h3", id="title-of-a-story")]
print(songs)

#Get song URIs
song_uris = []
for song in songs:
    search_res = sp.search(q=f"track:{song} year:{1994}", type="track")['tracks']['items']
    if len(search_res) > 0:
        song_uris.append(search_res[0]["uri"])

print(song_uris)

#Create playlist

url1 = f'https://api.spotify.com/v1/users/{current_user['id']}/playlists/'
json1 = {
    "name": f"{date} Billboard Top 100",
    "public": "false",
    "collaborative": "false",
    "description": f"Top 100 hits from {date}"
}
headers = {
    "Authorization": f"Bearer {token_info['access_token']}"
}
response = requests.post(url=url1, json=json1, headers=headers)
print(f"Creating playlist: {response.status_code}")
playlist_id = response.json()['id']

#Add songs to playlist

url2 = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
json2 = {
    "uris": song_uris
}
response = requests.post(url=url2, json=json2, headers=headers)
print(f"Adding songs: {response.status_code}")