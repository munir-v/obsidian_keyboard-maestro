import os
import re
import json
from pprint import pprint

file_loc1 = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/part1.txt')
file_loc2 = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/part2.txt')
json_file_loc = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/kindle_exports.json')

with open(file_loc1, "r") as f:
    file1 = f.readlines()
    # file1 = f.read()

with open(file_loc2, "r") as f:
    file2 = f.readlines()


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
    return set(clean_vocab_list) # remove duplicates


def main():
    title = file1[1]
    quote_and_vocab = get_quotes_and_vocab(file2)
    notes = quote_and_vocab[0]
    vocab = quote_and_vocab[1]
    vocab = clean_up_vocab(vocab)
    print('\n notes:')
    pprint(notes)
    print('\n vocab:')
    print(vocab)

# main()

with open(json_file_loc, "w") as j:
    # json_file = json.load(j)
    data = {'vocab':''}
    json.dump(data,j)

# todo
# add ankify tag