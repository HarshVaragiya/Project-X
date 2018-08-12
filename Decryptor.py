from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import json
import os
import hashlib
from termcolor import cprint


READ_FILE = "EncryptedBlockChain.txt"


os.system('cls')
data_list = []
modified = False

def p(data,color="blue"):
    cprint(data,color=color,attrs=['bold'])

def AESDecryptor(key,nonce,ciphertext):
    cipher = AES.new(key,AES.MODE_EAX,nonce=nonce)
    return cipher.decrypt(ciphertext)

def PublicKeyInit():
    private_key = open("private_key.pem",'rb').read()
    RSAObj = RSA.import_key(private_key)
    return PKCS1_OAEP.new(RSAObj)

def ReadData():
    global READ_FILE
    fw = open(READ_FILE,'r')
    raw_data = fw.read()
    fw.close()
    return raw_data

def Process_Top_Block():
    global enc_data
    raw_data = ReadData()
    PublicKeyObj = PublicKeyInit()
    enc_data = json.loads(raw_data)[::-1]
    top_block = json.loads(enc_data.pop(0))
    key_fingerprint = top_block['data']
    top_dict = PublicKeyObj.decrypt(bytes.fromhex(key_fingerprint)).decode()
    top_dict = json.loads(top_dict)
    return top_block,top_dict

try :                                                                       # to Process Top Block Correctly!
    top_block,top_dict = Process_Top_Block()
    key_data = top_dict['key']
    last_key = bytes.fromhex(key_data).decode()
    key_data = json.loads(last_key) 

    last_key = bytes.fromhex(key_data['key'])
    last_nonce = bytes.fromhex(key_data['nonce'])
    last_hash = top_block['hashP']
    last_enc_hash = top_block['EhashP']

except:
    print("Top Block Parsing Error!!")

for enc_block in enc_data:
    try:

        block_data = AESDecryptor(last_key,last_nonce,bytes.fromhex(enc_block)).decode()
        this_block_hash = hashlib.sha256(block_data.encode()).hexdigest()
        this_block_enc_hash = hashlib.sha256(bytes.fromhex(enc_block)).hexdigest()

        if(last_enc_hash != this_block_enc_hash or last_hash != this_block_hash):
            print("BlockChain Has Been Modified! Exiting !")
            modified = True
            break

        block = json.loads(block_data)
        id = block['id']
        print(block['data'] + " ",end='')
        if(id > 0 ):
            data_list.append(block)
            key_data = bytes.fromhex(block['lastKey']).decode()
            key_data = json.loads(key_data)
            last_key = bytes.fromhex(key_data['key'])
            last_nonce = bytes.fromhex(key_data['nonce'])
            last_hash = block['hashP']
            last_enc_hash = block['EhashP']
    except:
        modified = True
        print("Parsing Error!")


if(modified == False):
    data_list = data_list[::-1]
    print_data = ""
    p("Decrypted Data From Blockchain is : \n",'red')
    for data in data_list:
        print_data += data['data']
    p(print_data)
