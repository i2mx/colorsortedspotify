import asyncio
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from colorthief import ColorThief
import urllib.request
import colorsys
import bisect

async def main():
    print("SPOTIFY COLOR SORTER \n")

    client_id = os.getenv("CLIENT_ID")
    if not client_id:
        exit("CLIENT_ID missing in .env")

    client_secret = os.getenv("CLIENT_SECRET")
    if not client_secret:
        exit("CLIENT_SECRET missing in .env")

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id,
            client_secret,
            redirect_uri="http://localhost:3000/",
            scope="playlist-read-private playlist-modify-private playlist-modify-public",
        )
    )

    playlists = sp.current_user_playlists(limit=50)["items"]

    for i, playlist in enumerate(playlists):
        print(f"{i}. {str(playlist['name'])}")
        print(playlist["description"])
        print()

    playlist_index = int(input("Select a playlist: "))
    print()

    id = playlists[playlist_index]["id"]
    playlist = sp.playlist_items(id)["items"]

    sorted_list = []

    for i, item in enumerate(playlist):
        name = item['track']['name']
        print(f"{i}. {item['track']['name']}")

        preview_url = item["track"]["preview_url"]
        print(f"{preview_url=}")

        image_url = item["track"]["album"]["images"][2]["url"]
        print(f"{image_url=}")

        # --> Color Sort <--
        urllib.request.urlretrieve(image_url, "image.jpg")

        r,g,b = ColorThief("image.jpg").get_color()
        h,s,v = colorsys.rgb_to_hsv(r,g,b)

        insert_index = bisect.bisect(sorted_list, h)
        sp.playlist_reorder_items(id, i, insert_index)
        bisect.insort(sorted_list, h)

        print()

if __name__ == "__main__":
    asyncio.run(main())
