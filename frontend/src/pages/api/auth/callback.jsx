import { useRouter } from 'next/router';
import { useEffect } from 'react';

export default function Callback() {
  const router = useRouter();

  useEffect(() => {
    // Extract query parameters and handle them as needed.
    const { code, provider } = router.query;
    if (code && provider) {
      // Optionally, send these details to your backend.
      router.push('/dashboard');
    }
  }, [router]);

  return (
    <div className="container mx-auto p-8">
      <p>Processing callback...</p>
    </div>
  );
}
