
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "UAV Crack Detection service is running",
        "status": "ok"
    })

@app.route("/health")
def health():
    return jsonify({"health": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
