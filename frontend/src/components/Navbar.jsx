import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="bg-gray-800 p-4 text-white">
      <div className="container mx-auto flex justify-between">
        <Link href="/">
          <a className="text-xl font-bold">TuneSync</a>
        </Link>
        <div>
          <Link href="/dashboard">
            <a className="mr-4">Dashboard</a>
          </Link>
          <a href="/api/auth/logout" className="hover:underline">Logout</a>
        </div>
      </div>
    </nav>
  );
}
