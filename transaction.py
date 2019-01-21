import hashlib


subsidy = 10

class Transaction:

    def __init__(self, to, data):
        if data == None:
            data = "Reward to {}".format(to)

        self.v_in = TxInput("", -1, data)
        self.v_out = TxOutput(subsidy, to)

        h = hashlib.sha256()
        h.update(bytes(self))
        self.id = h.digest()

class TxOutput:

    def __init__(self, value, script_pub_key):
        self.value = value
        self.script_pub_key = script_pub_key

class TxInput:

    def __init__(self, tx_id, v_out, script_sig):
        self.tx_id = tx_id
        self.v_out = v_out
        self.script_sig = script_sig
