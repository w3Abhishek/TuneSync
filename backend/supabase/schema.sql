-- Create table for users (mapping Clerk users)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    clerk_id VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Table to store OAuth tokens for Spotify and YouTube
CREATE TABLE IF NOT EXISTS oauth_tokens (
    id SERIAL PRIMARY KEY,
    clerk_id VARCHAR(255) NOT NULL,
    provider VARCHAR(50) NOT NULL,  -- 'spotify' or 'youtube'
    access_token TEXT NOT NULL,
    refresh_token TEXT,
    expires_in INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (clerk_id) REFERENCES users(clerk_id) ON DELETE CASCADE
);

-- Table for playlists
CREATE TABLE IF NOT EXISTS playlists (
    id SERIAL PRIMARY KEY,
    clerk_id VARCHAR(255) NOT NULL,
    provider VARCHAR(50) NOT NULL, -- 'spotify' or 'youtube'
    playlist_id VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (clerk_id) REFERENCES users(clerk_id) ON DELETE CASCADE
);
