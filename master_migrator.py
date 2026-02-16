import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic

# --- 1. SETUP & AUTHENTICATION ---

# Spotify Keys (Paste yours here!)
CLIENT_ID = 'YOUR_CLIENT_ID_HERE'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET_HERE'
REDIRECT_URI = 'https://www.google.com/'

print("Connecting to Spotify...")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read"
))

print("Connecting to YouTube Music...")
yt = YTMusic()

# --- 2. THE EXTRACTION (Get Spotify Songs) ---

print("Fetching your Liked Songs from Spotify...\n")
# Grabbing just 5 songs for our first test run
spotify_results = sp.current_user_saved_tracks(limit=5) 

# --- 3. THE ENGINE (Loop & Search) ---

print("--- STARTING MIGRATION SEARCH ---\n")

for idx, item in enumerate(spotify_results['items']):
    track = item['track']
    song_name = track['name']
    artist_name = track['artists'][0]['name']
    
    # Create the exact string we want to search on YouTube
    search_query = f"{song_name} {artist_name}"
    print(f"[{idx + 1}] Searching for: {search_query}...")
    
    # --- 4. ERROR HANDLING (The Try/Except Block) ---
    try:
        # Ask YouTube for the song
        yt_results = yt.search(search_query, filter="songs")
        
        # Check if YouTube actually returned anything
        if len(yt_results) > 0:
            top_match = yt_results[0]
            video_id = top_match['videoId']
            print(f"    ✅ MATCH FOUND! YouTube ID: {video_id}")
        else:
            print(f"    ❌ NO RESULTS: YouTube couldn't find this song.")
            
    except Exception as e:
        # If the internet drops or the API crashes, it skips to the next song instead of dying
        print(f"    ⚠️ ERROR: Something went wrong with this track. Skipping.")

print("\n--- SEARCH COMPLETE ---")