from flask import Blueprint, jsonify
from utils.gmail_api import read_emails
from modules.email_fetcher import get_emails

email_bp = Blueprint("email", __name__)

@email_bp.route("/emails", methods=["GET"])
def get_emails():
    emails = read_emails()
    return jsonify(emails)


@email_bp.route("/emails", methods=["GET"])
def emails():
    return jsonify(get_emails())
