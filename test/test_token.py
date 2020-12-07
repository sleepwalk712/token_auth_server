from token_auth_server.server.token import TokenHandler


def test_encode_auth_token():
    token_handler = TokenHandler()

    user_id = 'a001'
    create_time = 1607330025
    expire_time = 5927330025
    key = b'\xa6\x97#G\x08\x82\xe5\xcfoB\x90\x10=k\x8f7\x18\xe3\xdfC1\xa5\xbb\x19'

    encoded_token = token_handler.encode_auth_token(user_id, create_time, expire_time, key)
    true_encoded_token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhMDAxIiwiaWF0IjoxNjA3MzMwMDI1LCJleHAiOjU5MjczMzAwMjV9.LU-VuueC-7SEWfd_X7BWq6SmRFGk8Kra1Bc_P47YneQ'

    assert encoded_token == true_encoded_token


def test_decode_auth_token():
    token_handler = TokenHandler()

    key = b'\xa6\x97#G\x08\x82\xe5\xcfoB\x90\x10=k\x8f7\x18\xe3\xdfC1\xa5\xbb\x19'
    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhMDAxIiwiaWF0IjoxNjA3MzMwMDI1LCJleHAiOjU5MjczMzAwMjV9.LU-VuueC-7SEWfd_X7BWq6SmRFGk8Kra1Bc_P47YneQ'

    decoded_token = token_handler.decode_auth_token(token=token, secret_key=key)

    assert decoded_token == {'sub': 'a001', 'iat': 1607330025, 'exp': 5927330025}
