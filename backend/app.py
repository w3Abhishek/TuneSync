from flask import Flask
from flask_cors import CORS
from config import Config

# Create Flask app and load config
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Allow CORS – adjust as needed for production

# Import and register blueprints (routes)
from routes.auth import auth_bp
from routes.spotify import spotify_bp
from routes.youtube import youtube_bp
from routes.sync import sync_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(spotify_bp, url_prefix='/spotify')
app.register_blueprint(youtube_bp, url_prefix='/youtube')
app.register_blueprint(sync_bp, url_prefix='/sync')

if __name__ == '__main__':
    app.run(debug=True)
