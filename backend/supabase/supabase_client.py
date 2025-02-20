from supabase import create_client
from config import Config

url = Config.SUPABASE_URL
key = Config.SUPABASE_KEY

supabase_client = create_client(url, key)
