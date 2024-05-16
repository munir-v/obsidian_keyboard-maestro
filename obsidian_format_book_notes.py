#!/usr/bin/env python3

import os
import sys # debugging
import constants


# read each line of file
	# if line contains ;; ... ;; split into body, tags, and title
		# create new note file as title.md
		# add body and metadata with tags
		# delete line in parent file, replace with ![[title]]

def create_notes(title, author, meta):
	if len(author)>0: # if an author name was provided
		author = " - " + author
		add_to_end = True
	else: 
		add_to_end = False

	file_array = []
	with open(target_file, "r") as f:
		file_array = f.readlines()
		for i, line in enumerate(file_array): 
			if line.count(";;") == 2: #for each line with ;;tags;; in it
				str = line.split(";;") # split into body, tags, and title
				child_body = str[0].strip()
				child_tags = str[1].strip()
				child_title = str[2].strip()

				child_tags = child_tags.replace("]][[","]] [[") #replace ]][[ with ]] [[

				if not ";;;" in line and add_to_end: # if there was an author name
					child_title+=author

				new_metadata = notes_metadata.replace("Topics:","Topics: " + child_tags) #add tags to metadata

				child_note_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + child_title + ".md"
				eprint(child_note_path)
				if not child_note_path.is_file():
					with open(child_note_path, "x") as new_f: #create new file
						new_f.write(child_body) # add the body of the note
						new_f.write("\n\n\n" + new_metadata) # add metadata
				
					file_array[i] = "![[" + child_title + "]]" #update line in parent note

	with open(target_file, "w") as f: # write changes to the original file
		f.writelines(file_array)

def printResult():
	with open(target_file, "r") as f:
		for line in f:
			print(line, end='')
		print()

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

note_title = str(os.environ["KMVAR_NoteTitle"]) + ".md"
author = str(os.environ["KMVAR_AuthorName"])
notes_metadata = str(os.environ["KMVAR_Metadata"])

target_file = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + note_title #full note directory

create_notes(target_file, author, notes_metadata)
# printResult()


















