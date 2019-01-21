import time
import hashlib

from proof_of_work import ProofOfWork


class Block:

    def __init__(self, data, prev_block_hash):
        self.timestamp = int(time.time())
        self.data = data
        self.prev_block_hash = prev_block_hash
        pow = ProofOfWork(self)
        nonce, hash = pow.run()
        self.hash = hash
        self.nonce = nonce

    def __str__(self):
        pow = ProofOfWork(self)
        return "Prev. hash: {}\nData: {}\nHash: {}\nPoW: {}".format(
            self.prev_block_hash,
            self.data,
            self.hash,
            pow.validate())

    @staticmethod
    def genesis_block():
        return Block('Genesis Block', '')
