import { useState } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import ConnectButton from '../components/ConnectButton';
import PlaylistCard from '../components/PlaylistCard';
import axios from 'axios';

export default function Dashboard() {
  const [playlists, setPlaylists] = useState({ spotify_playlists: null, youtube_playlists: null });
  const [loading, setLoading] = useState(false);

  const handleSync = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/sync/`);
      setPlaylists(response.data);
    } catch (error) {
      console.error("Sync failed", error);
    }
    setLoading(false);
  };

  return (
    <div>
      <Navbar />
      <main className="container mx-auto p-8">
        <h1 className="text-3xl font-bold mb-4">Dashboard</h1>
        <div className="flex space-x-4 mb-8">
          <ConnectButton provider="spotify" />
          <ConnectButton provider="youtube" />
        </div>
        <button
          onClick={handleSync}
          className="bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded mb-8"
        >
          {loading ? 'Syncing...' : 'Sync Playlists'}
        </button>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {playlists.spotify_playlists && (
            <div>
              <h2 className="text-2xl font-semibold mb-2">Spotify Playlists</h2>
              <PlaylistCard playlist={playlists.spotify_playlists} />
            </div>
          )}
          {playlists.youtube_playlists && (
            <div>
              <h2 className="text-2xl font-semibold mb-2">YouTube Playlists</h2>
              <PlaylistCard playlist={playlists.youtube_playlists} />
            </div>
          )}
        </div>
      </main>
      <Footer />
    </div>
  );
}
