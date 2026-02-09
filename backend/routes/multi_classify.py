from flask import Blueprint, request, jsonify
from modules.multi_classifier import classify_multi
from modules.reply_generator import generate_reply

multi_bp = Blueprint("multi", __name__)

@multi_bp.route("/multi_classify", methods=["POST"])
def multi():

    email = request.json.get("email")

    category = classify_multi(email)

    reply = generate_reply(email)

    return jsonify({
        "category": category,
        "reply": reply
    })
