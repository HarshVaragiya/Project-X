from BlockChain.BlockChain import BlockChain
import os
import json

def p(data,color="blue"):
    print(data)

class Election:
    def __init__(self,place_id,choices):
        self.place_id = place_id
        self.choices  = choices
        self.len_choices = len(self.choices)
        self.kernel = BlockChain(self.place_id)
        os.system('cls')
        p("Election Procedure Started!",'red')
        self.list_keys = [key for key in self.choices]

    def show_choices(self):
        os.system('cls')
        for key in self.choices:
            strx = key + " - " + self.choices[key]
            p(strx)
    
    def vote(self,voter_data):
        if(voter_data != None):
            strx = json.dumps(voter_data)
            self.kernel.insert(strx)
        else:
            p("Enter Valid Details!",'red')
        

    def export_logs(self,filename):
        data = self.kernel.export_chain()
        fw = open(filename,'w')
        fw.write(data)
        fw.close()

    def construct(self,voter_data,choice):
        if(choice in self.list_keys):
            data = {
                'id':voter_data,
                'choice':choice,
                'cand':self.choices[choice]
            }
            return data
        


