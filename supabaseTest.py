import os
from supabase import create_client, Client
#from decouple import config

# Read the variables from the .env file may not be needed
#username = config('USERNAME')
#password = config('PASSWORD')

# Use the variables as needed
#print(f'Username: {username}')
#print(f'Password: {password}')


url: str = os.environ.get("https://zjhemihkjcspikabnabb.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpqaGVtaWhramNzcGlrYWJuYWJiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ1NDU4ODUsImV4cCI6MjAxMDEyMTg4NX0.OlzWaElvTMe1eUfFTkxSmG7y9xaKGDWgV5mMjlzDCuU")

supabase: Client = create_client(url, key)

#signing in implementation
data = supabase.auth.sign_in_with_password({"email": "jlmoraws@uark.edu", "password": "5B2G6N~RWyz8hK"})
