import os
import json
import hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

AESKeyLen = 32    #  bytes

class Block:
    def __init__(self,id,prev_hash,prev_enc_hash,prev_key,data,top=False):
        self.id = id
        self.data = data
        self.prev_key = prev_key
        self.prev_hash = prev_hash
        self.prev_enc_hash = prev_enc_hash
        if(top==False):         
            self.key = os.urandom(32)
            self.cipher = AES.new(self.key,AES.MODE_EAX)
            self.cipher_nonce = self.cipher.nonce
            self.smash()
        else:
            self.top_smash()
    
    def top_smash(self):
        data = {
            'data':self.data,
            'hashP':self.prev_hash,
            'EhashP':self.prev_enc_hash
        }
        self.json_data  = json.dumps(data)
        self.ciphertext = self.json_data
        self.self_enc_hash = 0xFFFF
        self.self_hash     = 0xFFFF

    def smash(self):
        data = {
            'id'     :self.id,
            'lastKey':self.prev_key,
            'data'   :self.data,
            'hashP'  :self.prev_hash,
            'EhashP' :self.prev_enc_hash
        }
        self.json_data  = json.dumps(data)
        self.ciphertext = self.cipher.encrypt(self.json_data.encode()).hex()
        self.self_enc_hash = hashlib.sha256(bytes.fromhex(self.ciphertext)).hexdigest()
        self.self_hash     = hashlib.sha256(self.json_data.encode()).hexdigest()

    def get_ciphertext(self):
        return self.ciphertext
    
    def get_plaintext(self):
        print(self.json_data)
    
    def get_self_enc_hash(self):
        return self.self_enc_hash
    
    def get_self_hash(self):
        return self.self_hash
    
    def get_self_key(self):
        key_dict = {
            'key':self.key.hex(),
            'nonce':self.cipher_nonce.hex()
        }
        self.key_data = json.dumps(key_dict)
        return self.key_data.encode().hex()


