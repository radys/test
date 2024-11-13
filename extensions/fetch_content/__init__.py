import subprocess
import sys
from flask import Blueprint, jsonify

# Automatická instalace knihovny `requests`, pokud není dostupná
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# Vytvoření Blueprintu pro rozšíření
fetch_content_extension = Blueprint("fetch_content_extension", __name__)

@fetch_content_extension.route("/fetch_content", methods=["GET"])
def fetch_content():
    url = "http://static-flab3-250.flab.cesnet.cz:8000/"
    try:
        # Načtení obsahu z URL
        response = requests.get(url)
        response.raise_for_status()
        return jsonify({"content": response.text})
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Funkce pro načtení rozšíření
def load():
    return fetch_content_extension
