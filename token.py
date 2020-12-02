import os
import jwt


class TokenHandler:

    def __init__(self):
        pass

    def encode_auth_token(
        self,
        user_id: str,
        role: str,
        secret_key: str,
    ) -> str:
        try:
            payload = {
                'id': user_id,
                'role': role
            }
            return jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def generate_secret_key(self):
        return os.urandom(24)


if __name__ == "__main__":
    token_handler = TokenHandler
    key = token_handler.generate_secret_key()
    token = token_handler.encode_auth_token(user_id='a001', role='project_admin', secret_key=key)
    print(token)
