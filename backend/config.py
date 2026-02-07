import os

class Config:
    SECRET_KEY = "email_assistant_secret"

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    MODEL_DIR = os.path.join(BASE_DIR, "models")

    GMAIL_CREDENTIALS = os.path.join(BASE_DIR, "utils", "credentials.json")
    GMAIL_TOKEN = os.path.join(BASE_DIR, "utils", "token.json")

    LOG_FILE = os.path.join(BASE_DIR, "logs.txt")
