import datetime
from typing import Dict

import jwt

from payload import Payload
from secret_key import SecretKeyHandler


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
    ) -> Dict[str, str]:
        try:
            payload = jwt.decode(token, secret_key)
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
        expire_time=datetime.datetime.utcnow() + datetime.timedelta(seconds=5),
        secret_key=key,
    )
    print(token)
    payload = token_handler.decode_auth_token(token, key)
    print(payload)
