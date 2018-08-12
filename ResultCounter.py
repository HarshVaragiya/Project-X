from ElectionCounter import Decrypt_Election_Blockchain,get_status,p
import os
from ResultManager import Result

CHOICE_FILE_NAME     = "ElectionChoices.json"
ELECTION_RESULT_FILE = "Election.txt"

data_list = Decrypt_Election_Blockchain(ELECTION_RESULT_FILE)
modified = get_status()

if(modified == False):
    os.system('cls')
    p("Decrypted Vote Data From Blockchain is :\n",'red')
    Res = Result(CHOICE_FILE_NAME)
    Res.import_blocks(data_list)
    Res.process()

    p("Individual Voter Logs are :- \n",'green')
    Res.print_individual_choices()

    p("\nFinal Election Results Are :- \n",'red')
    votes = Res.exportResult()
    for key in votes:
        strx = str(key) + " - " + str(votes[key])
        p(strx,'blue')
    p("\nElection Results Verified! ",'green')


print("\n")

