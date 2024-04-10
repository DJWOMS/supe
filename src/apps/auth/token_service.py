from datetime import datetime, timedelta

import jwt

from esmerald.conf import settings

# from esmerald.security.jwt.token import Token
from esmerald.contrib.auth.mongoz.middleware import JWTAuthMiddleware
from src.apps.auth.dtos import TokenPayload, Token


class TokenService:
    @staticmethod
    def create_access_token(user_id: int, expires_delta: timedelta = None) -> Token:
        if expires_delta is not None:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode = {"exp": expire, "id": user_id}
        token = jwt.encode(payload=to_encode, key=settings.secret_key, algorithm=settings.algorithm)
        return Token(access_token=token)

    @staticmethod
    def decode_access_token(token: str) -> TokenPayload:
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            token_data = TokenPayload(**payload)
        except jwt.PyJWTError as e:
            raise Exception(f"Could not validate credentials\n{e}")
        return token_data
