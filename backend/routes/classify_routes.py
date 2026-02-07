from flask import Blueprint, request, jsonify
from modules.classifier import classify_spam

classify_bp = Blueprint("classify", __name__)

@classify_bp.route("/classify", methods=["POST"])
def classify_email():
    data = request.json
    email = data.get("email")

    result = classify_spam(email)

    return jsonify({
        "label": result
    })
