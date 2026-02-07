import re

def detect_followup(email):

    keywords = ["please respond", "waiting for reply", "reminder"]

    for k in keywords:
        if k in email.lower():
            return True

    return False
