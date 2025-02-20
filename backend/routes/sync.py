from flask import Blueprint, request, jsonify
import requests

sync_bp = Blueprint('sync', __name__)

@sync_bp.route('/', methods=['GET'])
def sync_playlists():
    # In a real app, use the authenticated user info (e.g., via Clerk) to look up tokens in Supabase.
    # Here we use dummy tokens for demonstration.
    spotify_token = "dummy_spotify_token"
    youtube_token = "dummy_youtube_token"

    spotify_playlists = get_spotify_playlists(spotify_token)
    youtube_playlists = get_youtube_playlists(youtube_token)

    # Sync logic: Compare and merge playlists as needed.
    return jsonify({
        'spotify_playlists': spotify_playlists,
        'youtube_playlists': youtube_playlists
    })

def get_spotify_playlists(token):
    url = "https://api.spotify.com/v1/me/playlists"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch Spotify playlists"}

def get_youtube_playlists(token):
    url = "https://www.googleapis.com/youtube/v3/playlists"
    params = {"part": "snippet,contentDetails", "mine": "true"}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch YouTube playlists"}
