import os
import psycopg2

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


""" 
Authenticate with Client Id and Client Secret Key
"""
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=os.getenv('CLIENT_ID'),
client_secret=os.getenv('CLIENT_SECRET')))


conn = psycopg2.connect(host=os.getenv('HOST'), dbname=os.getenv('DB_NAME'),
                        user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD')
                        )
cur = conn.cursor()
""" 
Connect with the postgresql database
"""

def get_tracklist(playlist_id):
    results = spotify.playlist(playlist_id, additional_types=("track",))
    """ 
    Get the data in results from Spotipy API in JSON form
    """
    playlist_name = results['name']
    playlist_followers = results['followers']['total']
    playlist_id = playlist_id
    cur.execute("INSERT INTO playlist VALUES (%s, %s, %s)", (playlist_name, playlist_followers, playlist_id))

    tracks = results['tracks']['items']
    for track in tracks:
        artist_name = track['track']['album']['name']
        track_id = track['track']['id']
        track_name = track['track']['name']
        external_urls = track['track']['external_urls']['spotify']
        added_at = track['added_at']
        release_date = track['track']['album']['release_date']
        popularity = track['track']['popularity']
        playlist_name = results['name']
        playlist_id = playlist_id
        cur.execute("INSERT INTO tracklist VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (artist_name, track_id, track_name, external_urls, added_at, release_date, popularity, playlist_name, playlist_id))
    conn.commit()
    """ 
    Save data into database
    """

playlist_urls = [
    "https://open.spotify.com/playlist/37i9dQZF1DWW4igXXl2Qkp",
    "https://open.spotify.com/playlist/6oZhNW8o5ru7mb4RFkWn0M",
    "https://open.spotify.com/playlist/4EtswXAGuGuUQcW9ctRour",
    "https://open.spotify.com/playlist/6hWMmrVlMTvME8u0KchOpa",
    "https://open.spotify.com/playlist/0c6wMHB5HsuZUscv3PQpih",
    "https://open.spotify.com/playlist/6e8MhEouOuoBRYnV9GuGtK",
    "https://open.spotify.com/playlist/5L3vZ9scrlV9DAcDEagI4c",
    "https://open.spotify.com/playlist/0UHup1TpaqtEUD3k8H6LG5"
]

def get_playlists():
    for playlist_url in playlist_urls:
        playlist_id = playlist_url.split('/')[-1]
        print(playlist_id)
        get_tracklist(playlist_id=playlist_id)


if __name__ == "__main__":
    get_playlists()
