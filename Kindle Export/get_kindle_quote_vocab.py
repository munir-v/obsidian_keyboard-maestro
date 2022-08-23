import os
import re
import json
from pprint import pprint

file_loc1 = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/part1.txt')
file_loc2 = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/part2.txt')
json_file_loc = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/kindle_exports.json')

with open(file_loc1, "r") as f:
    file1 = f.readlines()

with open(file_loc2, "r") as f:
    file2 = f.readlines()

with open(json_file_loc) as j:
    json_file = json.load(j)

def get_quotes_and_vocab(file):
    notes_list = []
    vocab_list = []
    p1 = re.compile(r'Highlight\(\w+\) - Location \d+')
    p2 = re.compile(r'Note - Location \d+')
    i = 2
    while (i<len(file)):
        if len(p1.findall(file[i])) > 0:
            highlight = file[i+1].strip()
            note = ''
            if i+2<len(file) and len(p2.findall(file[i+2])) > 0: # if there is a note
                note = file[i+3].strip()
                i+=2
            if highlight.count(' ') > 2 or len(note) > 0: # highlight more than 2 words or note not empty
                if len(note)>0:
                    highlight = highlight + ';; ' + note
                notes_list.append(highlight)
            else:
                vocab_list.append(highlight)
            i+=2
        else:
            i+=1
    return notes_list, vocab_list

def clean_up_vocab(vocab):
    clean_vocab_list = []
    for line in vocab:
        clean_vocab = re.sub('[(){}\[\]<>;./\\+=_*&^%$#@!~`:\"]', '', line)
        clean_vocab = clean_vocab.capitalize()
        clean_vocab_list.append(clean_vocab)
    return [set(clean_vocab_list)] # remove duplicates

def get_unique_quotes_vocab(title,notes,vocab):
    is_old_book = title in json_file
    new_vocab = [x for x in vocab if x not in json_file["vocab"]]
    if is_old_book:
        new_notes = [x for x in notes if x not in json_file[title]]
        json_file[title] = json_file[title] + new_notes
    else:
        new_notes = notes
        json_file[title] = new_notes
    json_file["vocab"] = json_file["vocab"] + new_vocab
    print('\n list(json_file):')
    print(list(json_file))
    # with open(json_file_loc, "w") as j:
    #     json.dump(list(json_file),j)
    return new_notes, new_vocab

def main():
    title = file1[1].strip()
    quotes_and_vocab = get_quotes_and_vocab(file2)
    notes = quotes_and_vocab[0]
    vocab = quotes_and_vocab[1]
    vocab = clean_up_vocab(vocab)
    new_quotes_and_vocab = get_unique_quotes_vocab(title,notes,vocab)
    notes = new_quotes_and_vocab[0]
    vocab = new_quotes_and_vocab[1]
    # print('\n notes:')
    # pprint(notes)
    # print('\n vocab:')
    # pprint(vocab)

main()



# todo
# add ankify tag