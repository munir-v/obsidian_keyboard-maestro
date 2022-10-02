import os
import re
import json
from pprint import pprint
import datetime

file_loc1 = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/part1.txt')
json_file_loc = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/kindle_exports.json')
old_exports = os.path.expanduser('~/Documents/Coding Projects/Keyboard Maestro and Obsidian/Kindle Export/last_kindle_exports.txt')

with open(file_loc1, "r") as f:
    file1 = f.readlines()

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
            if "Anki" in note or "anki" in note:
                highlight += ' #ankify🚨 '
            if highlight.count(' ') > 2 or len(note) > 0: # highlight more than 2 words or note not empty
                if len(note)>0:
                    highlight += ';; ' + note
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
        clean_vocab = re.sub('[(){}\[\]<>;./\\+=_*&^%$#@!~`:\,"]', '', line)
        clean_vocab = clean_vocab.capitalize()
        clean_vocab_list.append(clean_vocab)
    return list(set(clean_vocab_list)) # remove duplicates

def get_unique_quotes_vocab(title,notes,vocab):
    is_old_book = title in json_file
    if not "vocab" in json_file:
        json_file["vocab"] = ()
    new_vocab = tuple([x for x in vocab if x not in json_file["vocab"]])
    if is_old_book:
        new_notes = tuple([x for x in notes if x not in json_file[title]])
        json_file[title] = tuple(json_file[title]) + new_notes
    else:
        new_notes = tuple(notes)
        json_file[title] = new_notes
    json_file["vocab"] = tuple(json_file["vocab"]) + new_vocab
    with open(old_exports,'a') as f: # save old exports
        f.write(str(datetime.datetime.now()) + '\n\nVocab:\n' + 
        '\n'.join(new_vocab) + '\n\nNotes:\n' + '\n\n'.join(notes))
    with open(json_file_loc, "w") as jf: # write notes and vocab to json file
        json.dump(json_file,jf)
    for word in new_vocab: # add vocab to obsidian md file
        os.system('echo "' + word + '" >> "$HOME/Documents/Main Obsidian Vault/Home/000 Anki Vocab.md"')
    return new_notes, new_vocab

def main():
    input = str(os.environ["KMVAR_Local_Clipboard"]).split('\n')
    title = input[1].strip()
    quotes_and_vocab = get_quotes_and_vocab(input)
    notes = quotes_and_vocab[0]
    vocab = quotes_and_vocab[1]
    vocab = clean_up_vocab(vocab)
    new_quotes_and_vocab = get_unique_quotes_vocab(title,notes,vocab)
    notes = new_quotes_and_vocab[0]
    vocab = new_quotes_and_vocab[1]
    print('\n\n'.join(notes))

main()