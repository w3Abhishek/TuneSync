from flask import Blueprint, redirect, request, jsonify
import requests
from config import Config

spotify_bp = Blueprint('spotify', __name__)

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

@spotify_bp.route('/login')
def spotify_login():
    scope = "playlist-read-private playlist-read-collaborative"
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": Config.SPOTIFY_REDIRECT_URI,
        "scope": scope,
        "client_id": Config.SPOTIFY_CLIENT_ID,
    }
    url_args = "&".join(["{}={}".format(key, requests.utils.quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = f"{SPOTIFY_AUTH_URL}/?{url_args}"
    return redirect(auth_url)

@spotify_bp.route('/callback')
def spotify_callback():
    code = request.args.get('code')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': Config.SPOTIFY_REDIRECT_URI,
        'client_id': Config.SPOTIFY_CLIENT_ID,
        'client_secret': Config.SPOTIFY_CLIENT_SECRET,
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(SPOTIFY_TOKEN_URL, data=payload, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to get token', 'details': response.json()}), response.status_code

    token_info = response.json()
    # TODO: Save token_info in Supabase associated with the Clerk user.
    return jsonify(token_info)
