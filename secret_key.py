import os


class SecretKeyHandler:

    def __init__(self):
        pass

    def generate_auth_key(self) -> str:
        return os.urandom(24)

    def save_key_from_sql(self):
        pass

    def get_key_from_sql(self):
        pass
