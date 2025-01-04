import os
import datetime
import requests
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def get_secret_from_keyvault(secret_name):
    # This will use the Azure CLI, environment variables, managed identities, etc. for authentication
    credential = DefaultAzureCredential()
    key_vault_url = "https://aimusicgenerator.vault.azure.net/"
    client = SecretClient(vault_url=key_vault_url, credential=credential)
    
    try:
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        print(f"An error occurred while fetching the secret: {e}")
        return None

def generate_song():
    # URL for the unofficial Suno API (adjust if not running locally or on a different port)
    url = "http://localhost:3000/api/generate"
    
    # Retrieve the SUNO_COOKIE from Azure Key Vault
    suno_cookie = get_secret_from_keyvault("sunocookie")
    
    if not suno_cookie:
        print("Failed to retrieve SUNO_COOKIE from Key Vault.")
        return None

    headers = {
        "Cookie": f"SUNO_COOKIE={suno_cookie}"
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

# ... (rest of your function definitions remain the same)

if __name__ == "__main__":
    main()