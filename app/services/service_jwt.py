from decouple import config
from typing import Dict
import jwt
import time

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 86400,
        "refresh": True
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token["expires"] < time.time():
            if decoded_token["refresh"] == True:
                new_token = refreshJWT(decoded_token["user_id"])
                decoded_new_token = jwt.decode(new_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
                return decoded_new_token
            else:
                return None
        else:
            return decoded_token
    except:
        return {}

def refreshJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 86400,
        "refresh": True
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)