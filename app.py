from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY", "admin123")

@app.route("/")
def home():
    return jsonify({"message": "Bienvenue-Soutenance"})

@app.route("/sante")
def sante():
    return jsonify({"status": "OK"})

@app.route("/connexion", methods=["POST"])
def connexion():
    data = request.get_json()

    if data.get("key") == SECRET_KEY:
        return jsonify({"message": "Connexion réussie"})

    return jsonify({"error": "Accès refusé"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    