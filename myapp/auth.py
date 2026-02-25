from jose import jwt, JWTError
from datetime import datetime, timedelta
from django.conf import settings

ALGORITHM = "HS256"

def create_access_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        "type": "access"
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)

def create_refresh_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.now() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        "type": "refresh"
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)

def verify_token(token, token_type="access"):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        if payload["type"] != token_type:
            return None
        return payload["user_id"]
    except JWTError:
        return None
