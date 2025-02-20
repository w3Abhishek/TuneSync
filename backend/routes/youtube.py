from flask import Blueprint, redirect, request, jsonify
import requests
from config import Config

youtube_bp = Blueprint('youtube', __name__)

YOUTUBE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
YOUTUBE_TOKEN_URL = "https://oauth2.googleapis.com/token"

@youtube_bp.route('/login')
def youtube_login():
    scope = "https://www.googleapis.com/auth/youtube.readonly"
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": Config.YOUTUBE_REDIRECT_URI,
        "scope": scope,
        "client_id": Config.YOUTUBE_CLIENT_ID,
        "access_type": "offline",
        "prompt": "consent"
    }
    url_args = "&".join(["{}={}".format(key, requests.utils.quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = f"{YOUTUBE_AUTH_URL}?{url_args}"
    return redirect(auth_url)

@youtube_bp.route('/callback')
def youtube_callback():
    code = request.args.get('code')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    payload = {
        'code': code,
        'client_id': Config.YOUTUBE_CLIENT_ID,
        'client_secret': Config.YOUTUBE_CLIENT_SECRET,
        'redirect_uri': Config.YOUTUBE_REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(YOUTUBE_TOKEN_URL, data=payload, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to get token', 'details': response.json()}), response.status_code

    token_info = response.json()
    # TODO: Save token_info in Supabase associated with the Clerk user.
    return jsonify(token_info)
