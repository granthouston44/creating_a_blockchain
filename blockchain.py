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

