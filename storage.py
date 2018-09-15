import pickle


class InMemoryStorage:
    db = {}

    def get_block(self, hash):
        block_bytes = self.db.get(hash)
        return pickle.loads(block_bytes)

    def put_block(self, block):
        self.db[block.hash] = pickle.dumps(block)
        self.db['last'] = block.hash

    def get_last_block(self):
        last_hash = self.get_last_hash()
        return self.get_block(last_hash)

    def get_last_hash(self):
        return self.db.get('last')

    def empty(self):
        return self.get_last_hash() == None
