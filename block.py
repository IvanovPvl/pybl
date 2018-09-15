import time
import hashlib


class Block:
    timestamp = 0
    data = ''
    prev_block_hash = ''
    hash = ''

    def __init__(self, data, prev_block_hash):
        self.timestamp = int(time.time())
        self.data = data
        self.prev_block_hash = prev_block_hash
        self._set_hash()

    @staticmethod
    def genesis_block():
        return Block('Genesis Block', '')

    def _set_hash(self):
        headers = ''.join([self.prev_block_hash, self.data, str(self.timestamp)])
        h = hashlib.sha256()
        h.update(headers.encode())
        self.hash = h.hexdigest()
