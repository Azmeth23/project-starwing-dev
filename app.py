from flask import Flask
from datetime import datetime
import socket


app = Flask(__name__)


@app.route("/health")
def home():
    return {
        "status": "running heathyly",
        "version": "1.0",
        "app": "DevOps Learning App"
    }


@app.route("/report")
def report():
    return {
        "service": "GCP Resource Reporter",
        "generated_at": datetime.utcnow().isoformat(),
        "hostname": socket.gethostname(),
        "status": "report generated"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )