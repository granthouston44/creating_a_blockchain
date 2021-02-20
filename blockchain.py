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