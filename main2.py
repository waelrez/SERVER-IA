from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os

from config.settings import APP_NAME, PORT
from api.routes import api
from database.database import initialize_database


app = Flask(__name__)

CORS(app)

app.register_blueprint(api, url_prefix="/api")

initialize_database()


@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "server": APP_NAME,
        "status": "online",
        "type": "AI SERVER",
        "time": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy",
        "ai": "ready",
        "database": "ready"
    })


if __name__ == "__main__":

    port = int(os.environ.get("PORT", PORT))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
