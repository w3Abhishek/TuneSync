import { ClerkProvider } from '@clerk/clerk-react';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return (
    <ClerkProvider publishableKey={process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY}>
      <Component {...pageProps} />
    </ClerkProvider>
  );
}

export default MyApp;
