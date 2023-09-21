import os
from supabase import create_client, Client
from decouple import config

# Read the variables from the .env file
username = config('USERNAME')
password = config('PASSWORD')

# Use the variables as needed
print(f'Username: {username}')
print(f'Password: {password}')


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
