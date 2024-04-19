from functools import wraps
from utils import auth_fns
from fastapi import HTTPException

class AuthMiddleware:
    def __init__(self, jwt_payload):
        self.jwt_payload = jwt_payload

    def check_auth(self, role):
        if "user role" in self.jwt_payload and self.jwt_payload["user role"] == role:
            return True
        return False
    

def auth_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = auth_fns.check_token(kwargs['request'])
            auth_middleware = AuthMiddleware(token)
            if not auth_middleware.check_auth(role):
                raise HTTPException(status_code=403, detail="Access denied")
            return func(*args, **kwargs)
        return wrapper
    return decorator

