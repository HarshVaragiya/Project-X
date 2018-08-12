# Project-X
BlockChain Based Election System +/  Encrypted Data Storage System

## Crypto-Structure:

1. Genesis Block is Made
2. New Block is made when data insertion in blockchain is required
3. New Block has Previous Hash,Previous Encrypted Hash,Previous AES Key data
4. New Block Encrypts itself with a random 256Bit AES Key  -> AES_EAX Mode Used
5. New Block exports its AES Key and Nonce to the next New Block
6. Next Block Repeats the same.
7. Top Block Is added in the End of Blockchain. it secures the last AES Key with 4096 Bit RSA Encryption
8. Blockchain is exported to a file as text data (list of hex data) 

### Crypto Specifications :

1. AES - EAX - 256 Bit 
2. RSA - 4096 Bit
3. PKCS1_OAEP with RSA
4. os library Random Number Generator (os.urandom()) / optionally Crypto.Random can be used.  

## Working :
This Example System (Prototype) works by encrypting each block data with AES 256Bit Key and storing
that key in the next block.The Top Block (at the end of the block) is secured with RSA Encrypted last block AES Key
so, we need the private key to unlock the top block, then we can get prevous key, then decrypt last block data,
which has key of last block ... over and over again .

In the End , if we want ordered Data, we can reverse the data array.

## Data Integrity :
Testing the integrity of this system using OPENSSL and Hashlib on Python ( SHA256 ) shows that 
once file is encrypted -> stored -> decrypted , the hashes are the same, meaning integrity is 100%.

## Future : 
1. No idea. 
2. Can be used to store data.
