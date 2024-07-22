#!/usr/bin/env python

import os
import re
import sys # debugging
import constants


# read each line of file
# if line contains ;; ... ;; split into body, tags, and title
# create new note file as title.md
# add body and metadata with tags
# delete line in parent file, replace with ![[title]]

def create_notes(target_file, author, notes_metadata):
    if len(author) > 0:  # if an author name was provided
        author = " - " + author
        add_to_end = True
    else:
        add_to_end = False

    file_array = []
    with open(target_file, "r") as f:
        file_array = f.readlines()
        for i, line in enumerate(file_array): 
            if re.search(";;[^;]+;;[^;]+", line):
                parts = line.split(";;")  # split into body, tags, and title
                child_body = parts[0].strip()
                child_tags = parts[1].strip()
                child_title = parts[2].strip()

                child_tags = child_tags.replace("]][[", "]] [[")

                if ";;;" not in line and add_to_end:  # if there was an author name
                    child_title += author

                new_metadata = notes_metadata.replace("Topics:", "Topics: " + child_tags)  # add tags to metadata

                child_note_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + child_title + ".md"
                if not os.path.isfile(child_note_path):
                    with open(child_note_path, "x") as new_f:  # create new file
                        new_f.write(child_body)  # add the body of the note
                        new_f.write("\n\n\n" + new_metadata)  # add metadata
                
                    file_array[i] = "![[" + child_title + "]]"  # update line in parent note

    with open(target_file, "w") as f:  # write changes to the original file
        f.writelines(file_array)

def printResult(target_file):
    with open(target_file, "r") as f:
        for line in f:
            print(line, end='')
        print()

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

author = str(os.environ["KMVAR_AuthorName"])
notes_metadata = str(os.environ["KMVAR_local_Metadata"])
target_file = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + str(os.environ["KMVAR_local_NoteTitle"]) # full note directory

# print(author)
# print(notes_metadata)
# print(target_file)


create_notes(target_file, author, notes_metadata)
# printResult(target_file)