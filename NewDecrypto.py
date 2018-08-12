from ResultManager import Result
from ElectionCounter import Decrypt_Election_Blockchain
from termcolor import cprint

READ_FILE_NAME = "EncrypedBlockChain.txt"
OUT_FILE_NAME  = "outfile.txt"

data = Decrypt_Election_Blockchain(READ_FILE_NAME)
result = Result()
result.import_blocks(data)
logs_data = result.process_data_block()

whole_data = ""

for log in logs_data:
    whole_data += log
 
print(whole_data + "\n")
open(OUT_FILE_NAME,'w').write(whole_data)