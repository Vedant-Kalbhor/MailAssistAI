def generate_reply(email_text):
    """
    Temporary rule-based reply generator.
    Later we can replace with AI model.
    """

    email_text = email_text.lower()

    if "meeting" in email_text:
        return "Sure, I am available for the meeting. Please share the details."

    if "deadline" in email_text:
        return "Thanks for the update. I will make sure to complete it before the deadline."

    if "thank" in email_text:
        return "You're welcome! Happy to help."

    return "Thank you for your email. I will get back to you shortly."
