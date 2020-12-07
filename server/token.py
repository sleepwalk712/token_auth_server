import datetime

import jwt

from token_auth_server.server.payload import Payload
from token_auth_server.server.secret_key import SecretKeyHandler


class TokenHandler:

    def __init__(self):
        pass

    def encode_auth_token(
        self,
        user_id: str,
        create_time: int,
        expire_time: int,
        secret_key: str,
    ) -> str:
        try:
            payload = Payload(sub=user_id, iat=create_time, exp=expire_time)
            return jwt.encode(
                payload,
                secret_key,
                algorithm='HS256',
            )
        except Exception as e:
            return e

    def decode_auth_token(
        self,
        token: str,
        secret_key: str,
    ) -> Payload:
        try:
            payload = jwt.decode(jwt=token, key=secret_key, algorithms='HS256')
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired.'
        except jwt.InvalidTokenError:
            return 'Invalid token.'


if __name__ == "__main__":
    secret_key_handler = SecretKeyHandler()
    key = secret_key_handler.generate_auth_key()
    token_handler = TokenHandler()
    token = token_handler.encode_auth_token(
        user_id='a001',
        create_time=datetime.datetime.utcnow(),
        expire_time=datetime.datetime.utcnow() + datetime.timedelta(days=50000),
        secret_key=key,
    )
    print(key)
    print(token)
    payload = token_handler.decode_auth_token(token, key)
    print(payload)
