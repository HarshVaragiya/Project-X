from BlockChain import BlockChain
from termcolor import cprint
import time

DATA_FILE_NAME = "ExampleFile.txt"
OUT_FILE_NAME  = "EncrypedBlockChain.txt"

raw_data = open(DATA_FILE_NAME,'r').read()
kernel = BlockChain(0xFF)
total_len = len(raw_data)

last_time = time.time()
for i in range(total_len):
    perc = 100*(i+1)/total_len
    try:
        rate = 1/(time.time()-last_time)
    except ZeroDivisionError:
        rate = 0xFF                                              # No idea how to handle this !
    last_time = time.time()
    eta = (total_len - i -1)/rate
    status = "Percentage : {:3.3f}  ->  Rate : {:4.2f}  ->  ETA : {:.2f} ".format(perc,rate,eta)
    cprint(status,color='green')
    kernel.insert(raw_data[i])

cprint("Exported Data Sucessfully!",'blue')
enc_data = kernel.export_chain()
open(OUT_FILE_NAME,'w').write(enc_data)
