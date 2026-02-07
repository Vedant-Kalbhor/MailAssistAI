from flask import Blueprint, request, jsonify
from modules.multi_classifier import classify_multi

multi_bp = Blueprint("multi", __name__)

@multi_bp.route("/multi_classify", methods=["POST"])
def multi_classify():
    data = request.json
    email = data.get("email")

    result = classify_multi(email)

    return jsonify({
        "category": result
    })
