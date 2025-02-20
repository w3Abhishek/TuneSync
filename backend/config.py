import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')

    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:5000/spotify/callback')

    YOUTUBE_CLIENT_ID = os.getenv('YOUTUBE_CLIENT_ID')
    YOUTUBE_CLIENT_SECRET = os.getenv('YOUTUBE_CLIENT_SECRET')
    YOUTUBE_REDIRECT_URI = os.getenv('YOUTUBE_REDIRECT_URI', 'http://localhost:5000/youtube/callback')

    CLERK_API_KEY = os.getenv('CLERK_API_KEY')
