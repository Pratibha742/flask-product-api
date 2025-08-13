from flask import jsonify, request
from functools import wraps

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if auth != "Bearer mysecrettoken":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return wrapper