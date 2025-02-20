import { useUser } from '@clerk/clerk-react';

export default function useAuth() {
  const { user, isLoaded, isSignedIn } = useUser();
  return { user, isLoaded, isSignedIn };
}
