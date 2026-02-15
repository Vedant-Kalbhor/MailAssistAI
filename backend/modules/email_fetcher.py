from utils.gmail_api import fetch_recent_emails
from modules.classifier import classify_spam

def get_emails():
    # Fetch from Gmail
    email_data = fetch_recent_emails()
    
    # If there's an error in the Gmail API response, return it
    if isinstance(email_data, dict) and "error" in email_data:
        return email_data
        
    # Classify each email
    processed_emails = []
    for email in email_data:
        label = classify_spam(email['snippet'])
        email['label'] = label
        processed_emails.append(email)
        
    return processed_emails
