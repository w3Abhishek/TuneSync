# models.py
# This file can define data models (or ORM classes) if you choose to use them.
# In this project, we rely on Supabase for database management.

class User:
    def __init__(self, clerk_id, email):
        self.clerk_id = clerk_id
        self.email = email

class OAuthToken:
    def __init__(self, clerk_id, provider, access_token, refresh_token=None, expires_in=None):
        self.clerk_id = clerk_id
        self.provider = provider
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in
