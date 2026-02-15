from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
import base64
from .auth import authenticate_gmail

def get_gmail_service():
    creds = authenticate_gmail()
    if not creds:
        return None
    service = build("gmail", "v1", credentials=creds)
    return service

def parse_header(headers, name):
    for header in headers:
        if header['name'].lower() == name.lower():
            return header['value']
    return ""

def read_emails(max_results=10):
    service = get_gmail_service()
    if not service:
        return {"error": "Authentication failed or credentials missing"}

    try:
        results = service.users().messages().list(userId="me", maxResults=max_results).execute()
        messages = results.get("messages", [])

        email_list = []
        for msg in messages:
            txt = service.users().messages().get(userId="me", id=msg["id"]).execute()
            payload = txt.get("payload", {})
            headers = payload.get("headers", [])
            
            subject = parse_header(headers, "Subject")
            sender = parse_header(headers, "From")
            date = parse_header(headers, "Date")
            
            email_list.append({
                "id": msg["id"],
                "snippet": txt.get("snippet", ""),
                "subject": subject,
                "sender": sender,
                "date": date
            })

        return email_list
    except Exception as e:
        return {"error": str(e)}

def fetch_recent_emails(max_results=10):
    return read_emails(max_results)
