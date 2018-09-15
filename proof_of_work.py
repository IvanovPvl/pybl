import hashlib


target_bits = 22

class ProofOfWork:
    block = None
    target = 0

    def __init__(self, block):
        self.block = block
        self.target = 1 << (256 - target_bits)

    def run(self):
        print('Mining the block containing {}'.format(self.block.data))

        nonce = 0
        digest = None
        while True:
            data = self._prepare_data(nonce)
            h = hashlib.sha256()
            h.update(data.encode())
            digest = h.digest()
            hash_int = int.from_bytes(digest, byteorder='big')

            if hash_int < self.target:
                break
            else:
                nonce += 1

        print('{}'.format(digest.hex()))
        print()

        return nonce, digest.hex()

    def validate(self):
        data = self._prepare_data(self.block.nonce)
        h = hashlib.sha256()
        h.update(data.encode())
        hash_int = int.from_bytes(h.digest(), byteorder='big')
        return hash_int < self.target

    def _prepare_data(self, nonce):
        b = self.block
        return ''.join([b.prev_block_hash, b.data, str(b.timestamp), str(target_bits), str(nonce)])
