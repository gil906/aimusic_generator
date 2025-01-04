import os
import datetime
import requests
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def get_secret_from_keyvault(secret_name):
    # Use DefaultAzureCredential for authentication with Azure AD
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
    url = "http://suno-api:3000/api/generate"
    
    # Retrieve secrets from Azure Key Vault
    azure_tenant_id = get_secret_from_keyvault("azuretenantid")
    azure_client_id = get_secret_from_keyvault("azureclientid")
    azure_client_secret = get_secret_from_keyvault("azureclientsecret")
    
    if not azure_tenant_id or not azure_client_id or not azure_client_secret:
        print("Failed to retrieve Azure credentials from Key Vault.")
        return None

    # Use these credentials to get the SUNO_COOKIE or any other necessary secret
    suno_cookie = get_secret_from_keyvault("sunocookie")
    
    if not suno_cookie:
        print("Failed to retrieve SUNO_COOKIE from Key Vault.")
        return None

    headers = {
        "Cookie": f"SUNO_COOKIE={suno_cookie}"
    }
    
    payload = {
        "prompt": "Reggaeton modern vulgar and ordinary talking about sex, drugs and money",
        "title": "AI_Music_Match-" + datetime.datetime.now().strftime("%Y-%m-%d")
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to generate song: {response.status_code}, {response.text}")
        return None

# Rest of the code remains the same