from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Cloud DevOps AI Project",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "dev"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
