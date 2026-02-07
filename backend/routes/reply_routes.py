from flask import Blueprint, request, jsonify
from modules.reply_generator import generate_reply

reply_bp = Blueprint("reply", __name__)

@reply_bp.route("/reply", methods=["POST"])
def reply():

    email = request.json.get("email")

    response = generate_reply(email)

    return jsonify({"reply": response})
