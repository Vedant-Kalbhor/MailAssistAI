from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from config import Config

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():

    creds = None

    if os.path.exists(Config.GMAIL_TOKEN):
        with open(Config.GMAIL_TOKEN, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(Config.GMAIL_CREDENTIALS):
                print(f"Error: {Config.GMAIL_CREDENTIALS} not found. Please provide Gmail API credentials.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(
                Config.GMAIL_CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(Config.GMAIL_TOKEN, 'wb') as token:
            pickle.dump(creds, token)

    return creds
