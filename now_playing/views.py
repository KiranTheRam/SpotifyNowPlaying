import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import render
from django.http import JsonResponse
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config.get('spotify', 'client_id')
client_secret = config.get('spotify', 'client_secret')
redirect_uri = config.get('spotify', 'redirect_uri')

# Initialize Spotipy with the necessary scopes
scope = 'user-read-currently-playing'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


def playing(request):
    # Fetch currently playing track
    current_track = sp.current_user_playing_track()

    track_name = None
    artist_name = None
    album_art_url = None

    if current_track is not None:
        # Get track information
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        album_art_url = current_track['item']['album']['images'][0]['url']

    context = {
        'track_name': track_name,
        'artist_name': artist_name,
        'album_art_url': album_art_url,
    }
    return render(request, 'now_playing.html', context)


def update_playing(request):
    # Fetch currently playing track
    current_track = sp.current_user_playing_track()

    track_name = None
    artist_name = None
    album_art_url = None

    if current_track is not None:
        # Get track information
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        album_art_url = current_track['item']['album']['images'][0]['url']

    context = {
        'track_name': track_name,
        'artist_name': artist_name,
        'album_art_url': album_art_url,
    }
    return JsonResponse(context)
