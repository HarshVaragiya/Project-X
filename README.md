# Project-X
BlockChain Based Election System +/  Encrypted Data Storage System

##Working :
This Example System (Prototype) works by encrypting each block data with AES 256Bit Key and storing
that key in the next block.The Top Block (at the end of the block) is secured with RSA Encrypted last block AES Key
so, we need the private key to unlock the top block, then we can get prevous key, then decrypt last block data,
which has key of last block ... over and over again .

In the End , if we want ordered Data, we can reverse the data array.

##Data Integrity :
Testing the integrity of this system using OPENSSL and Hashlib on Python ( SHA256 ) shows that 
once file is encrypted -> stored -> decrypted , the hashes are the same, meaning integrity is 100%.

##Future : 
1. No idea. 
2. Can be used to store data.
