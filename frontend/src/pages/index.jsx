import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <Navbar />
      <main className="container mx-auto p-8">
        <h1 className="text-4xl font-bold mb-4">Welcome to TuneSync</h1>
        <p className="mb-8">Sync your Spotify and YouTube Music playlists effortlessly.</p>
        <Link href="/dashboard">
          <a className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
            Go to Dashboard
          </a>
        </Link>
      </main>
      <Footer />
    </div>
  );
}
