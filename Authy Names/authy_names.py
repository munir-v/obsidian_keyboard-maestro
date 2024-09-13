import json
import os

authy_account_names_loc = os.path.expanduser('~/Documents/Coding-Projects/Keyboard-Maestro-and-Obsidian/Authy Names/authy_account_names.txt')

# def get_json_file_loc():
#     path = os.path.expanduser('~/Downloads')
#     for dirpath, dirnames, files in os.walk(path):
#         for folder in dirnames:
#             if 'Authy Backup' in folder:
#                 return path + '/' + folder + '/authy_backup.json'

def get_authy_names():
    # json_file_loc = get_json_file_loc()
    json_file_loc = os.path.expanduser('~/Downloads/authy_backup.json')
    with open(json_file_loc, "r") as j:
        json_file = json.load(j)
        account_names = []
        for line in json_file:
            account_names.append(line['name'])
        if len(account_names)>1:
            with open (authy_account_names_loc,'w') as f:
                f.write('\n'.join(account_names))
        else:
            print("Script failed!")

if __name__ == "__main__":
    get_authy_names()
