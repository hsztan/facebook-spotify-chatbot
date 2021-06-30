from os import getenv
from requests import post, get
from base64 import b64encode

AUTH_ENDPOINT = 'https://accounts.spotify.com/api/token'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
GET_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}'
RELATED_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/related-artists'
TRACKS_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'
TRACK_ID_ENDPOINT = 'https://api.spotify.com/v1/tracks/{id}'


def auth_token():
    client_id = getenv('SPOTIFY_CLIENT_ID')
    client_secret = getenv('SPOTIFY_CLIENT_SECRET')

    # Authorization BASE64
    auth_client = f'{client_id}:{client_secret}'
    message = auth_client.encode('ascii')
    bs4_encode = b64encode(message)
    b64_token = bs4_encode.decode('ascii')

    headers = {
        'Authorization': f'Basic {b64_token}'
    }

    data = {
        'grant_type': 'client_credentials'
    }

    response = post(AUTH_ENDPOINT, headers=headers, data=data)
    return response.json()['access_token']


def search_artist_name(name):
    params = {
        'q': name,
        'type': 'artist'
    }
    token = auth_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = get(SEARCH_ENDPOINT, params=params, headers=headers)
    return response.json()

def search_songs(name):
    params = {
        'q': name,
        'type': 'track'
    }
    token = auth_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = get(SEARCH_ENDPOINT, params=params, headers=headers)
    return response.json()


def get_artist(artist_id):
    url = GET_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = get(url, headers=headers)
    return response.json()

def get_track(track_id):
    url = GET_ARTIST_ENDPOINT.format(id=track_id)
    token = auth_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = get(url, headers=headers)
    return response.json()


def get_artist_relateds(artist_id):
    url = RELATED_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = get(url, headers=headers)
    return response.json()


def get_artist_tracks(artist_id):
    url = TRACKS_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'market': 'US'
    }
    response = get(url, headers=headers, params=params)
    return response.json()
