from typing import TypedDict


class Payload(TypedDict):
    sub: str
    iat: int
    exp: int
