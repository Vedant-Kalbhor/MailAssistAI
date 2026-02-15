from flask import Blueprint, jsonify
from modules.email_fetcher import get_emails
from utils.auth import authenticate_gmail
import os
from config import Config

email_bp = Blueprint("email", __name__)

@email_bp.route("/auth/status", methods=["GET"])
def auth_status():
    connected = os.path.exists(Config.GMAIL_TOKEN)
    return jsonify({"connected": connected})

@email_bp.route("/auth/connect", methods=["GET"])
def auth_connect():
    try:
        creds = authenticate_gmail()
        if creds:
            return jsonify({"status": "success", "message": "Authenticated successfully"})
        return jsonify({"status": "error", "message": "Authentication failed"}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@email_bp.route("/emails", methods=["GET"])
def fetch_emails():
    emails = get_emails()
    return jsonify(emails)
