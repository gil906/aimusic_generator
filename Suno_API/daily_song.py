import os
import datetime
import requests

def generate_song():
    # URL for the unofficial Suno API (adjust if not running locally or on a different port)
    url = "http://localhost:3000/api/generate"
    
    # Here you would normally set the SUNO_COOKIE from your environment variables or a secure config file
    # For this example, we'll assume it's set here directly:
    headers = {
        "Cookie": "SUNO_COOKIE=YOUR_COOKIE_HERE"
    }
    
    payload = {
        "prompt": "Daily generative music piece",  # Adjust the prompt to what you want for your song
        "title": "AI Generated Music - " + datetime.datetime.now().strftime("%Y-%m-%d")
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON with song details or direct links
    else:
        print(f"Failed to generate song: {response.status_code}, {response.text}")
        return None

def save_song(song_info):
    if song_info:
        # Assuming 'song_info' contains a URL or path where the song can be downloaded
        if 'audio_url' in song_info:
            audio_url = song_info['audio_url']
            audio_response = requests.get(audio_url)
            
            if audio_response.status_code == 200:
                date_str = datetime.datetime.now().strftime("%Y%m%d")
                filename = f"song_{date_str}.mp3"  # Assuming the song is in MP3 format
                filepath = os.path.join("/mnt/media/aimusic_generator", filename)
                with open(filepath, "wb") as f:
                    f.write(audio_response.content)
                return filepath
            else:
                print(f"Failed to download song: {audio_response.status_code}")
        else:
            print("No audio URL found in the response")
    return None

def main():
    song_info = generate_song()
    if song_info:
        saved_path = save_song(song_info)
        if saved_path:
            print(f"Song saved to: {saved_path}")
            # Here you would call upload_to_platforms if you want to proceed with uploads
        else:
            print("Failed to save the song.")
    else:
        print("Failed to generate song.")

if __name__ == "__main__":
    main()