export default function ConnectButton({ provider }) {
    const handleConnect = () => {
      if (provider === 'spotify') {
        window.location.href = `${process.env.NEXT_PUBLIC_API_URL}/spotify/login`;
      } else if (provider === 'youtube') {
        window.location.href = `${process.env.NEXT_PUBLIC_API_URL}/youtube/login`;
      }
    };
  
    return (
      <button
        onClick={handleConnect}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Connect {provider.charAt(0).toUpperCase() + provider.slice(1)}
      </button>
    );
  }
  