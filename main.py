from blockchain import Blockchain


bc = Blockchain()
bc.add_block('Send 1 BTC to Pavel')
bc.add_block('Send 2 BTC to Pavel')

for b in bc.blocks:
    print('Prev. hash: {}'.format(b.prev_block_hash))
    print('Data: {}'.format(b.data))
    print('Hash: {}'.format(b.hash))
    print()
