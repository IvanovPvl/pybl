from blockchain import Blockchain
from proof_of_work import ProofOfWork


bc = Blockchain()
bc.add_block('Send 1 BTC to Pavel')
bc.add_block('Send 2 BTC to Pavel')

for b in bc:
    print(b)
    print()
