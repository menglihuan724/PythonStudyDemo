import json
import hashlib
from time import time
from flask import  Flask, jsonify
from uuid import uuid4

from flask import request


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
    #获取上一个区块
    @property
    def last_block(self):
        return  self.chain[-1]
    #hash
    @staticmethod
    def  hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    #验证
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

#web app
app = Flask(__name__)

node_indentifier = str(uuid4()).replace('-', '')
blockChain = BlockChain()

@app.route('/make',methods=['GET'])
def make():
    last_block=blockChain.last_block
    last_proof=last_block['proof']
    proof=blockChain.proof_of_block(last_proof)
    blockChain.new_transaction(
        sender='0',
        recipient=node_indentifier,
        amount=1
    )
    previous_hash = blockChain.hash(last_block)
    block = blockChain.new_block(proof, previous_hash)
    response = {
        'message': 'new Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/transactions/',methods=['POST'])
def makeTransactions():
    values = request.get_json()
    required = ['sender','recipent','amount']
    if not all(k in values for k in required):
        return 'miss value',400
    index=blockChain.new_transaction(values['sender'],values['recipent'],values['amount'])
    response={'message':f'Transaction will be added  to Block{index}'}
    return  jsonify(response),200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockChain.chain,
        'length': len(blockChain.chain),
    }
    return jsonify(response), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7024)

