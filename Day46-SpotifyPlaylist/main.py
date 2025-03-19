import pprint as pp
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

## This script requires a Spotify and Spotify Developers profile
# https://developer.spotify.com/documentation/web-api
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URL = "https://example.com/"
BASE_URL = "https://www.billboard.com/charts/hot-100/"


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
date = "1996-07-29"
url = BASE_URL + date + "/"

#  scrape the top 100 song titles on that date into a Python List
response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

row_tags = soup.find_all("div",class_="o-chart-results-list-row-container")
# print(row_tag)

top100 = {}
for t in row_tags:
    placement = t.find("span").get_text().strip()
    title_tag = t.find("h3",id="title-of-a-story")
    art_tag = t.find("h3",id="title-of-a-story").findNext('span')
    title = title_tag.get_text().strip()
    artist = art_tag.get_text().strip()
    top100[placement] = [title, artist]

# pp.pprint(top100)

scope = "playlist-modify-public"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope, 
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET, 
        redirect_uri=REDIRECT_URL,
        cache_path="token.txt"
        )
    )

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

my_info = sp.me()

# print('display name: '+my_info['display_name'])
# print('id: '+ my_info['id'])
my_id = my_info['id']

# query = "track:Higher artist:Creed"
# song = sp.search(q=query, limit=1)
# pp.pprint(song)

# song_uri = song['tracks']['items'][0]['uri']
# print(song_uri)

# Get URI for each song in top 100
uri_list = []
year = date.split("-")[0]
for k,s in top100.items():
    query = f"track:{s[0]} year:{year}"
    song = sp.search(q=query, limit=1, type="track")
    try:
        song_uri = song['tracks']['items'][0]['uri']
        uri_list.append(song_uri)
    except IndexError:
        pass

# print(uri_list)

# Create playlist for the songs
playlist_name = f"{date} Billboard 100"
list_id = sp.user_playlist_create(user=my_id, name=playlist_name)['id']

# Add playlist items
sp.playlist_add_items(playlist_id=list_id, items=uri_list)

print("Playlist created!")