import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint


CLIENT_ID = "c0590610b1f24dd5be193c3b92bece66"
CLIENT_SECRET = "91e30ada6e854fceb71b7afaa34fec13"
PLAYLIST_ID = "0QuWsMYV0sNCmULrQugnhS"
SPOTIPY_REDIRECT_URI = "http://example.com"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
year = date.split("-")[0]

titles = []


title = soup.select(selector = "li ul li h3")
titles = [song.getText().strip() for song in title]
print(titles)

#titles.append(title.strip())
#author = soup.select_one(selector = "li ul li span").getText()
scope = "playlist-modify-public"

#authentication = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope)
#authentication.get_cached_token()


sp = spotipy.Spotify(auth= "BQDlbULdqRCuWwXN1amHDC9ixAlBIpLKKZSyuD_DOP68d41kGUFTsLHqZ940tUz7IUAs1YneFF0002I24xMpCy40CumkhUK6FEKPhJVKZsuV6TwknRfigfKi9etf8s22RHQ-cf5Zamjx1nmrDAtJJJ2tUQSpeJY_S7GzXhSTaL6fN7xOBiN4skqLCZFNoBwmSqYJ1CRSEA")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))

id = sp.current_user()["id"]

playlist_uri = []

#print(sp.search(f"track:{titles[0]} year:{year}", type="track"))
for title in titles:
    result = sp.search(f"track:{title}",type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        playlist_uri.append(uri)
    except IndexError:
        print("Doesn't exist")
#
print(playlist_uri)
print(id)
#sp.user_playlist_create(user = id, name = date + " Billboard 100", collaborative=False, description='')

#print(sp.current_user_playlists())
sp.playlist_add_items(playlist_id = PLAYLIST_ID, items = playlist_uri, position=None)
print(sp.playlist(playlist_id=PLAYLIST_ID))