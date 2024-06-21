users = []
methods = [
    {"id": 1, "caption": "Vigenere Cipher", "json_params": {}, "description": "Encrypts using Vigenere Cipher."},
    {"id": 2, "caption": "Shift Cipher", "json_params": {"shift": 3}, "description": "Encrypts using Shift Cipher with shift of 3."}
]
sessions = []

class User:
    def __init__(self, user_id, login, secret):
        self.user_id = user_id
        self.login = login
        self.secret = secret

class Method:
    def __init__(self, id, caption, json_params, description):
        self.id = id
        self.caption = caption
        self.json_params = json_params
        self.description = description

class Session:
    def __init__(self, id, user_id, method_id, data_in, data_out, status, created_at, time_op):
        self.id = id
        self.user_id = user_id
        self.method_id = method_id
        self.data_in = data_in
        self.data_out = data_out
        self.status = status
        self.created_at = created_at
        self.time_op = time_op
