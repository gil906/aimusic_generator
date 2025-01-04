import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def upload_video(file_path):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    youtube = build('youtube', 'v3', credentials=creds)

    body = {
        'snippet': {
            'title': 'AI Generated Music - ' + os.path.basename(file_path).split('.')[0],
            'description': 'This song was generated using AI by AIMusicMatch',
            'tags': ['AI', 'Music', 'Generated'],
            'categoryId': '10'  # Music category
        },
        'status': {
            'privacyStatus': 'public'  # or 'private' or 'unlisted'
        }
    }

    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=googleapiclient.http.MediaFileUpload(file_path)
    )
    response = insert_request.execute()
    print(f"Video id '{response['id']}' was successfully uploaded.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        upload_video(sys.argv[1])
    else:
        print("Please provide path to the song file as an argument.")