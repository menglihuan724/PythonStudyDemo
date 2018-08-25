import json
import hashlib
from time import time


class BlockChain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self,proof,previous_hash):
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions=[]
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index']+1

    @property
    def last_block(self):
        return  self.chain[-1]

    @staticmethod
    def hash(block):
        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def proof_of_block(self,last_proof):
        proof=0
        while self.valid_proof(last_proof,proof) is False:
            proof+=1
        return proof
    @staticmethod
    def valid_proof(last_proof,proof):
        guess=f'{last_proof}{proof}'.encode()
        guess_hash=hashlib.sha256(guess).hexdigest()
        return guess_hash[:4]=='0000'