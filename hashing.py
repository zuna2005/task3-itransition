import secrets
import hmac
import hashlib

NUM_BYTES = 64


class Hmac:
    def __init__(self, moves):
        self.key = secrets.token_hex(NUM_BYTES)
        self.move = secrets.choice(moves)
        self.move_index = moves.index(self.move)

    def get_hmac(self):
        hash_algorithm = hashlib.sha3_256
        hmac_digest = hmac.new(self.key.encode(), self.move.encode(), hash_algorithm).hexdigest()
        return hmac_digest
