from Block.Block import Block
import os
import json
import hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

public_key = open("public_key.pem",'rb').read()

RSAObj = RSA.import_key(public_key)
PublicKeyObj = PKCS1_OAEP.new(RSAObj)

def Encrypt_RSA(data):
    bytes_key = data.encode()
    enc_key = PublicKeyObj.encrypt(bytes_key).hex()
    return enc_key
    
class BlockChain:
    def __init__(self,ID=0xFF7):
        self.id = ID
        self.count = 0
        self.blockchain = []
        self.gen = self.create_genesis()
        self.blockchain.append(self.gen)
        self.add_top_block()
    # def __init__(self,id,prev_hash,prev_enc_hash,prev_key,data):
    def create_genesis(self):
        genesis_block_prev_hash = os.urandom(32).hex()
        genesis_block_prev_enc_hash = os.urandom(32).hex()
        genesis_block_prev_key = os.urandom(32).hex()
        genesis_block_data = os.urandom(32).hex()
        genesis_block = self.make_block(genesis_block_prev_hash,genesis_block_prev_enc_hash,genesis_block_prev_key,genesis_block_data)
        return genesis_block

    def make_block(self,prev_hash,prev_enc_hash,prev_key,data,top=False):
        new_block =  Block(self.count,prev_hash,prev_enc_hash,prev_key,data,top)
        self.count = len(self.blockchain)
        if(top==False):
            self.prev_hash     = new_block.get_self_hash()
            self.prev_enc_hash = new_block.get_self_enc_hash()
            self.prev_key      = new_block.get_self_key()
        return new_block

    def insert(self,data):
        new_block = self.make_block(self.prev_hash,self.prev_enc_hash,self.prev_key,data)
        self.blockchain.pop(len(self.blockchain)-1) # Remove Top Block
        self.blockchain.append(new_block)           # Add New Block
        self.add_top_block()                        # Add New Top Block
    
    def show_chain(self):
        for block in self.blockchain:
            #block.get_plaintext()
            print(block.get_ciphertext())
    
    def show_last_block(self):
        return self.blockchain[-1].get_ciphertext()

    def export_chain(self):
        enc_data = []
        for block in self.blockchain:
            enc_data.append(block.get_ciphertext())
        return json.dumps(enc_data)
    
    def add_top_block(self):
        raw_data = {
            'id':len(self.blockchain),
            'key':self.prev_key,
        }
        enc_key_data = Encrypt_RSA(json.dumps(raw_data))
        top_block = self.make_block(self.prev_hash,self.prev_enc_hash,self.prev_key,enc_key_data,top = True)
        self.blockchain.append(top_block)

