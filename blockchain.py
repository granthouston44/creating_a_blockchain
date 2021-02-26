import datetime
import hashlib
import json
from flask, import Flask, jsonify

# blueprint for individual objects
# we can create an object from a class
# an object is an instance of the class - we instantiate an obect
class Blockchain:

    # self represents the instance of the class
    # we use the self keyword to allow us to access the attributes and methods defined within the class
     
    # the init method is a constructor - this is called whenever an object is instantiated 
    # in order to create the object
    # we can use this to initialize the attributes of the class 
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain)+1
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block
    
    def get_prev_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False: 
            # if new_proof=2 & prev_proof=3
            # then new (new_proof**2 - previous_proof**2) = 5
            # putting the above into the str function returns '5'
            # using the encode function just returns b'5', in order for it to be in the correct format for the sha256 function
            # this can be verified in the python console
            # the hexdigest is to make sure we get the result in a hexadecimal format 
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # [:4] uses index 0-3 as the upper limit in python is excluded
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block,sort_keys=True).encode(())
        return hashlib.sha256(encoded_block).hexdigest

    def is_chain_valid(self, chain):
        # this function needs to validate the whole chain
        # therefore, the previous block needs to start with index 0, as it is the very first block
        # it can't be a chain unless there's more than one block right?
        # So, the block_index is the looping variable. 
        # It will be the next block in the chain - starting at index 1, as the second block
        previous_block = chain[0]
        block_index = 1 
        while block_index < len(chain):
            block = chain[block_index]
            # self.hash because we are referencing hash method within its own class
            # hash method formats our block into json and then spits out the sha256 hash represenstation of that data
            # we haven't got any blocks yet until it is mined
            # this function initializes for the first block when it is made
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                return False
            previous_block = block
            block_index +=1
        return True

# Creating Flask Web App
app = Flask(__name__)

# Creating the blockchain
blockchain = Blockchain()

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_prev_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previoush_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp']
        'proof': block['proof'],
        'previoush_hash': block['previous_hash']
    }
    return jsonify(response), 200
