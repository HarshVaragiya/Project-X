from ElectionHandler import Election,p
import json

choices = json.loads(open("ElectionChoices.json",'r').read())
EXPORT_FILE_NAME = "Election.txt"

X = Election(0xFF,choices)
choice_data = 0x00

while(True):
    X.show_choices()
    voter_data =  str(input("Enter Voter Id Number  0xid : "))
    if(voter_data == "end()"):
        break
    choice_data = str(input("Enter Choice           0xch : "))
    if(choice_data == "end()"):
        break
    try:
        data = X.construct(voter_data,choice_data)
        X.vote(data)
    except:
        p("Invalid Data !",'red')

X.export_logs(EXPORT_FILE_NAME)
p("Elections Ended Sucessfully!",'green')