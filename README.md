
# AI Music Match

This project automates the generation, saving, and uploading of AI-generated music to YouTube. It uses:

- **Suno API** for music generation
- **Azure Key Vault** for secure secret management
- **Google's YouTube API** for uploading

## Project Structure

/aimusicmatch/
│
├── CreateContainers.sh
├── docker-compose.yml
│
├── Music_Generator/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── daily_song.py
│
├── Suno_API/
│   ├── Dockerfile
│   └── package.json
│
├── YouTube_Uploader/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── credentials.json
│   └── youtube_uploader.py



## Setup

### Prerequisites

- Docker and Docker Compose installed
- Node.js (for Suno_API if running locally)
- Python 3.9+
- Azure AD credentials with access to Azure Key Vault
- Google OAuth credentials for the YouTube API

### Installation

1. **Clone the Repository:**
   ```bash
   git clone [your-repository-url]
   cd aimusicmatch



2. **Build Docker Images:**
chmod +x CreateContainers.sh
./CreateContainers.sh


3. **Configure Environment Variables:**
Create a .env file at the project root or set variables in docker-compose.yml:
AZURE_TENANT_ID
AZURE_CLIENT_ID
AZURE_CLIENT_SECRET
Ensure SUNO_COOKIE is stored in Azure Key Vault under the name sunocookie.
Place your Google API credentials in YouTube_Uploader/credentials.json.



4. **Start Services:**
docker-compose up -d

**Configuration**
Azure Key Vault: Ensure the KeyVaultPostmanAccess service principal has permission to read secrets.
Google Credentials: Update credentials.json with your actual Google OAuth credentials.

**Running**
The ofelia service automatically runs daily_song.py and youtube_uploader.py once a day.

**Useful Information**
Data Persistence: Directories like /mnt/media/aimusic_generator should exist on your host for storing generated music.
Suno API: Assumes it's available at http://localhost:3000/api/generate. Adjust as necessary.
Security: In production, use environment variables or secrets management tools for sensitive information.

**Testing the Application**
Manual Test: 
Run docker exec -it music-generator python daily_song.py to generate a song manually.
Check if the song file appears in /mnt/media/aimusic_generator.
Similarly, test the upload with docker exec -it youtube-uploader python youtube_uploader.py /mnt/media/aimusic_generator/your_song.mp3.

**API Testing:**
Use tools like Postman or cURL to test the Suno API endpoint manually.

**Customizing Generation Frequency**
To change from daily to twice-daily music generation:


Modify Docker Compose: Update the ofelia service in docker-compose.yml
1. labels:
  ofelia.job-exec.music_generation.schedule: "@every 12h"
  ofelia.job-exec.music_generation.command: "docker exec music-generator python daily_song.py && docker exec youtube-uploader python youtube_uploader.py /mnt/media/aimusic_generator/last_generated_song.mp3"
  ofelia.enabled: "true"


2. Restart Services: After modifying docker-compose.yml, run:
docker-compose down
docker-compose up -d



**Troubleshooting**
Permission Errors: Verify Docker volume permissions and Azure Key Vault access.
API Errors: Check API endpoints, authentication, and network settings.
Upload Failures: Ensure token.pickle exists or can be created during OAuth flow.

**License**
[Choose a license, e.g., MIT License]

**Contributing**
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

**Acknowledgements**
[Azure](https://azure.microsoft.com/)
[Google YouTube API](https://developers.google.com/youtube/v3)
[Suno AI (Assuming this is the music generation service)](https://www.suno.ai/)

Feel free to reach out if you have any questions or issues!





