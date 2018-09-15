from block import Block
from storage import InMemoryStorage


class Blockchain:
    tip = ''
    db = InMemoryStorage()

    def __init__(self):
        if self.db.empty():
            genesis = Block.genesis_block()
            self.db.put_block(genesis)
            self.tip = genesis.hash
        else:
            self.tip = self.db.get_last_hash()

    def add_block(self, data):
        last = self.db.get_last_hash()
        block = Block(data, last)
        self.db.put_block(block)
        self.tip = block.hash
