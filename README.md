##Spotify
First Create Virtual env

then Activate Virtual env

Install requirements - pip install -r requirements.txt

Provide client id and client secret key in .env file

Create database and provide DB credentials in .env file

If you are using windows OS run command - 
env.bat
#see env.example

If you are using Linux OS command -
source .env
#see env.example

Run these queries to create DB tables

    CREATE TABLE playlist(
        playlist text,
        followers integer,
        playlist_id text
        )

    CREATE TABLE tracklist(
        artist_name text,
        track_id text,
        track_name text,
        external_urls text,
        added_at TIMESTAMP,
        release_date TIMESTAMP,
        popularity integer,
        playlist_name text,
        playlist_id text
    )

Run command - python spotify.py 