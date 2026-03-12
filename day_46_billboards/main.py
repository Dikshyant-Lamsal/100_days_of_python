import requests
from bs4 import BeautifulSoup
import re
import dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv()

# data = input("enter date in format yyyy-mm-dd: ")
date="20210309"
official_charts_url =  f"https://www.officialcharts.com/charts/singles-chart/{date}/7501/"
official_charts_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(official_charts_url,headers=official_charts_headers)
response.raise_for_status()
data = response.text
soup = BeautifulSoup(data,"html.parser")
script = soup.find("script", string=re.compile(r'"title"'))

titles = re.findall(r'"([^"]{2,60})","\/songs\/', script.string)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-private playlist-modify-public"
))
user_id = sp.current_user()["id"]
print(user_id)
playlist = sp.current_user_playlist_create(
    name=f"Charts {date}",
    public=False,
    description=f"Official Singles Chart - {date}"
)
playlist_id = playlist["id"]

track_uris = []
not_found = []

for title in titles:
    result = sp.search(q=title, type="track", limit=1)
    tracks = result["tracks"]["items"]
    if tracks:
        track_uris.append(tracks[0]["uri"])
        print(f"✓ Found: {title}")
    else:
        not_found.append(title)
        print(f"✗ Not found: {title}")

sp.playlist_add_items(playlist_id, track_uris[:100])
print(f"\nPlaylist '{playlist['name']}' created with {len(track_uris)} songs!")