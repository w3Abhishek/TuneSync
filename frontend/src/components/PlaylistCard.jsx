export default function PlaylistCard({ playlist }) {
    return (
      <div className="border rounded p-4 shadow-md">
        <h3 className="text-lg font-bold">{playlist.name || 'Playlist'}</h3>
        <pre className="text-sm mt-2">{JSON.stringify(playlist, null, 2)}</pre>
      </div>
    );
  }
  