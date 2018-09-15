import time
import hashlib

from proof_of_work import ProofOfWork


class Block:
    timestamp = 0
    data = ''
    prev_block_hash = ''
    hash = ''
    nonce = 0

    def __init__(self, data, prev_block_hash):
        self.timestamp = int(time.time())
        self.data = data
        self.prev_block_hash = prev_block_hash
        pow = ProofOfWork(self)
        nonce, hash = pow.run()
        self.hash = hash
        self.nonce = nonce

    @staticmethod
    def genesis_block():
        return Block('Genesis Block', '')

    # def _set_hash(self):
    #     headers = ''.join([self.prev_block_hash, self.data, str(self.timestamp)])
    #     h = hashlib.sha256()
    #     h.update(headers.encode())
    #     self.hash = h.hexdigest()
