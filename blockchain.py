from block import Block


class Blockchain:
    blocks = []

    def __init__(self):
        self.blocks.append(Block.genesis_block())

    def add_block(self, data):
        last = self.blocks[-1]
        block = Block(data, last.hash)
        self.blocks.append(block)
