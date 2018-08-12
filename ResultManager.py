import json
from ElectionCounter import p

class Result:
    def __init__ (self,choices_filename=None):
        if(choices_filename!=None):
            self.choices = self.load_choice_dict(choices_filename)
            self.vote_counter = {}
            self.choice_counter = {}
            self.init_vote_counter()
            self.voter_list = []
        
    def init_vote_counter(self):
        for key in self.choices:
            self.vote_counter[self.choices[key]] = 0
    
    def import_blocks(self,data):
        self.blocks = data
    
    def process_data_block(self):
        data_list = []
        for block in self.blocks:
            data_list.append(block['data'])
        return data_list

    def process(self):
        for block in self.blocks:
            self.process_block(block)

    def process_block(self,blockData):
        dat = blockData['data']
        dic = json.loads(dat)
        self.voter_list.append(dic)
        voter_id,cand = dic['id'],dic['cand']
        self.vote_counter[cand] +=1 
        self.choice_counter[voter_id] = cand

    def exportResult(self):
        return self.vote_counter
    
    def export_voter_logs(self):
        return self.voter_list

    def load_choice_dict(self,filename):
        return json.loads(open(filename,'r').read())

    def print_individual_choices(self):
        colors = ['red','blue','white','yellow']                         # A bit more specific but .. 
        for user in self.voter_list:
            uch = user['choice']
            uid = user['id']
            cand = user['cand']
            strx = "VoterID : " + str(uid) + " |  Choice ID " + str(uch)+ " |  Candidate :  "  + cand 
            p(strx,colors[int(uch)-1])
        

