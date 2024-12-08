from flask import request, jsonify
from functools import wraps
# Mock token for simplicity
VALID_TOKEN = "secret-token"

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != VALID_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return wrapper
