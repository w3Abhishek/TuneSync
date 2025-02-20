# TuneSync

TuneSync is a web application that allows you to connect your Spotify and YouTube Music accounts to seamlessly sync your playlists. Users can register and log in using Clerk, while TuneSync handles the OAuth flows for Spotify and YouTube Music. Playlist data and OAuth tokens are stored securely using Supabase.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [File Structure](#file-structure)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

TuneSync provides an intuitive platform to connect your Spotify and YouTube Music accounts. By syncing your playlists, you can enjoy a unified music experience across platforms. The backend is built using Flask and integrates with Supabase for data storage, while the frontend leverages React, Next.js, Tailwind CSS, and Shadcn UI for a responsive design.

## Features

- **User Authentication:** Seamless sign-up and login powered by Clerk.
- **OAuth Integration:** Secure OAuth flows for Spotify and YouTube Music.
- **Playlist Syncing:** Fetch and merge playlists from both platforms.
- **Responsive UI:** Modern, responsive design using Tailwind CSS and Shadcn UI components.

## Tech Stack

- **Backend:** Python (Flask), Supabase, Clerk, OAuth (Spotify & YouTube Music)
- **Frontend:** React, Next.js, Tailwind CSS, Shadcn UI, Clerk

## File Structure

### Backend (`tunesync-backend/`)

```
tunesync-backend/
├── app.py                   # Main Flask application
├── config.py                # Configuration & environment variables
├── requirements.txt         # Python dependencies
├── models.py                # (Optional) Data models
├── routes/                  # Route handlers
│   ├── auth.py              # User authentication endpoints
│   ├── spotify.py           # Spotify OAuth and API endpoints
│   ├── youtube.py           # YouTube Music OAuth and API endpoints
│   └── sync.py              # Playlist syncing endpoint
├── supabase/                
│   ├── supabase_client.py   # Supabase client initialization
│   └── schema.sql           # Database schema for Supabase
└── utils/
    └── helpers.py           # Utility functions (e.g., token refresh)
```

### Frontend (`tunesync-frontend/`)

```
tunesync-frontend/
├── package.json             # NPM dependencies and scripts
├── next.config.js           # Next.js configuration
├── tailwind.config.js       # Tailwind CSS configuration
├── postcss.config.js        # PostCSS configuration
├── .env.local               # Environment variables (Clerk keys, API URLs)
├── public/                  
│   └── assets/              # Static assets (images, icons, etc.)
└── src/
    ├── components/          # React components (Navbar, Footer, etc.)
    ├── pages/               # Next.js pages (Home, Dashboard, OAuth callbacks)
    ├── hooks/               # Custom hooks (e.g., for authentication)
    ├── styles/              # Global and Tailwind styles
    └── utils/               # API client functions
```

## Setup Instructions

### Backend Setup

1. **Clone the Repository & Create Virtual Environment:**

   ```bash
   cd tunesync-backend
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**

   Create a `.env` file in the `tunesync-backend` directory with the following:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key

   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_api_key

   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:5000/spotify/callback

   YOUTUBE_CLIENT_ID=your_youtube_client_id
   YOUTUBE_CLIENT_SECRET=your_youtube_client_secret
   YOUTUBE_REDIRECT_URI=http://localhost:5000/youtube/callback

   CLERK_API_KEY=your_clerk_api_key
   ```

4. **Database Setup:**

   - Log into your Supabase dashboard.
   - Run the SQL commands in `supabase/schema.sql` to create the necessary tables.

5. **Run the Flask Server:**

   ```bash
   flask run
   ```

   Your API will be available at `http://localhost:5000`.

### Frontend Setup

1. **Clone the Repository & Install Dependencies:**

   ```bash
   cd tunesync-frontend
   npm install
   ```

2. **Configure Environment Variables:**

   Create a `.env.local` file in the `tunesync-frontend` directory with:

   ```env
   NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key_here
   NEXT_PUBLIC_API_URL=http://localhost:5000
   ```

3. **Setup Tailwind CSS:**

   Follow the [official Tailwind CSS guide for Next.js](https://tailwindcss.com/docs/guides/nextjs) if not already set up.

4. **Run the Development Server:**

   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`.

## Usage

1. **User Registration & Login:**
   - Users can register and log in via Clerk on the frontend.
2. **Connect Music Services:**
   - From the dashboard, click on "Connect Spotify" or "Connect YouTube" to initiate the OAuth flow.
3. **Sync Playlists:**
   - Once connected, click on the "Sync Playlists" button to fetch and merge your playlists from both platforms.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and open a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).