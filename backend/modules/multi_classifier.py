def classify_multi(email_text):

    # TEMP LOGIC
    text = email_text.lower()

    if "meeting" in text or "deadline" in text:
        return "important"

    if "please respond" in text:
        return "follow_up"

    if "offer" in text or "lottery" in text:
        return "spam"

    return "normal"
