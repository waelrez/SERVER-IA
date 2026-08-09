from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "server": "REAL AI SERVER",
        "status": "online",
        "message": "AI server is ready",
        "time": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "processing": True
    })


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json(silent=True) or {}

    text = data.get("text", "")

    if not text:
        return jsonify({
            "success": False,
            "error": "text is required"
        }), 400

    # AI processing will be added here
    result = {
        "input": text,
        "response": "AI processing module is ready.",
        "processed": True
    }

    return jsonify({
        "success": True,
        "result":
