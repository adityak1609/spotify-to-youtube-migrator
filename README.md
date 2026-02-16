# 🎵 Spotify to YouTube Music Playlist Migrator

An automated Python tool that extracts a user's Spotify library and locates the exact matching tracks on YouTube Music. 

## 🚀 The Problem
Manually migrating a music library between streaming platforms is tedious. This tool automates the process by acting as a bridge between the Spotify and YouTube Music ecosystems.

## 🛠️ Tech Stack & Concepts Learned
* **Language:** Python 3
* **Libraries:** `spotipy`, `ytmusicapi`
* **Core Concepts:** REST APIs, OAuth 2.0 Authentication Flows, JSON Data Parsing, Error Handling.

## ⚙️ How It Works (The Architecture)
1. **Authentication:** Authenticates the user via Spotify's OAuth 2.0 flow to grant secure, temporary access to private playlists.
2. **Data Extraction:** Sends a `GET` request to Spotify and parses the returned JSON payload to isolate the `Track Name` and `Artist`.
3. **Data Transformation:** Formats the extracted data into a highly specific search query.
4. **Target Query:** Pings the YouTube Music API with the query, filters for audio-only results, and retrieves the unique destination `videoId`. 

## 🚧 Challenges Overcome
* **OAuth Redirects:** Successfully navigated Spotify's strict Redirect URI requirements by implementing a secure callback loop.
* **Messy Data:** Handled deeply nested JSON dictionaries to reliably extract artist data, even when tracks featured multiple collaborators.
* **Missing Tracks:** Built `try/except` error handling to prevent the script from crashing when a Spotify indie track did not exist on YouTube Music.
