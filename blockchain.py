from block import Block
from storage import FileStorage


class Blockchain:

    def __init__(self):
        self.db = FileStorage('./pybl.db')
        self.current_hash = None

        if self.db.empty():
            genesis = Block.genesis_block()
            self.db.put_block(genesis)
            self.tip = genesis.hash
        else:
            self.tip = self.db.get_last_hash()

    def __iter__(self):
        self.current_hash = self.tip
        return self

    def __next__(self):
        if self.current_hash == '':
            raise StopIteration

        block = self.db.get_block(self.current_hash)
        prev_hash = block.prev_block_hash
        self.current_hash = prev_hash
        return block

    def add_block(self, data):
        last = self.db.get_last_hash()
        block = Block(data, last)
        self.db.put_block(block)
        self.tip = block.hash
