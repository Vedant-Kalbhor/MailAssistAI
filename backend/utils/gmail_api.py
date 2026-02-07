from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_gmail_service():
    creds = Credentials.from_authorized_user_file("token.json")
    service = build("gmail", "v1", credentials=creds)
    return service

def read_emails():
    service = get_gmail_service()

    results = service.users().messages().list(userId="me").execute()
    messages = results.get("messages", [])

    email_list = []

    for msg in messages[:10]:
        txt = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        email_list.append(txt["snippet"])

    return email_list
