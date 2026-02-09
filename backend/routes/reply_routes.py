from flask import Blueprint, request, jsonify
from modules.reply_generator import generate_reply

reply_bp = Blueprint("reply", __name__)

@reply_bp.route("/generate_reply", methods=["POST"])
def reply_email():
    data = request.json
    email = data.get("email")

    if not email:
        return jsonify({"error": "email text required"}), 400

    reply = generate_reply(email)

    return jsonify({
        "reply": reply
    })
