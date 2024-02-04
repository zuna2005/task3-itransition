import secrets
import hmac
import hashlib


class Hmac:
    def __init__(self, moves):
        self.key = secrets.token_hex(64)
        self.move = secrets.choice(moves)
        self.move_index = moves.index(self.move)

    def get_hmac(self):
        hash_algorithm = hashlib.sha3_256

        # Calculate the HMAC using the specified key and message
        hmac_digest = hmac.new(self.key.encode(), self.move.encode(), hash_algorithm).hexdigest()

        return hmac_digest
