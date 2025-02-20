import requests
from config import Config

def refresh_spotify_token(refresh_token):
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': Config.SPOTIFY_CLIENT_ID,
        'client_secret': Config.SPOTIFY_CLIENT_SECRET,
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def refresh_youtube_token(refresh_token):
    payload = {
        'client_id': Config.YOUTUBE_CLIENT_ID,
        'client_secret': Config.YOUTUBE_CLIENT_SECRET,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post("https://oauth2.googleapis.com/token", data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None
