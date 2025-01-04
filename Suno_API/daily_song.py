def save_song(song_info):
    if song_info:
        # Assuming 'song_info' contains a URL or path where the song can be downloaded
        if 'audio_url' in song_info:
            audio_url = song_info['audio_url']
            audio_response = requests.get(audio_url)
            
            if audio_response.status_code == 200:
                date_str = datetime.datetime.now().strftime("%Y%m%d")
                filename = f"AI_Music_Match_{date_str}.mp3"  # Assuming the song is in MP3 format
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
        else:
            print("Failed to save the song.")
    else:
        print("Failed to generate song.")

if __name__ == "__main__":
    main()