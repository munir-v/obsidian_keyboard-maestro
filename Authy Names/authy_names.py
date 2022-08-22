import json
import os

json_file_loc = os.path.expanduser('~/Downloads/authy_backup.json')
authy_account_names_loc = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Authy Names/authy_account_names.txt')

def get_authy_names():
    with open(json_file_loc, "r") as j:
        json_file = json.load(j)
        
        account_names = []
        for line in json_file:
            account_names.append(line['name'])
        with open (authy_account_names_loc,'w') as f:
            f.write('\n'.join(account_names))
        

get_authy_names()