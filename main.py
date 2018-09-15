from blockchain import Blockchain
from proof_of_work import ProofOfWork


bc = Blockchain()
bc.add_block('Send 1 BTC to Pavel')
bc.add_block('Send 2 BTC to Pavel')

for b in bc:
    pow = ProofOfWork(b)
    print('Prev. hash: {}'.format(b.prev_block_hash))
    print('Data: {}'.format(b.data))
    print('Hash: {}'.format(b.hash))
    print('PoW: {}'.format(pow.validate()))
    print()
