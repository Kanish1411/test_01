import jwt
from flask import request

SECRET_KEY = "admin123-secret-key"


def verify_token(token):
    try:
        # Accepts unsigned tokens
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded
    except Exception:
        return None


def login_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return {"error": "Unauthorized"}, 401

        user = verify_token(token)
        request.user = user
        return f(*args, **kwargs)

    return wrapper