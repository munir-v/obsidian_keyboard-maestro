#!/usr/bin/env python3

import os
import sys
import pathlib #used to get working directory
from pathlib import Path #used to get working directory
import re #regex

# read each line of file
	# if line contains ;; ... ;; split into body, title, and tags
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
		for index, line in enumerate(file_array): 
			if ";;" in line: #for each line with ;; in it
				str = line.split(";;") # split into body, tags, and title
				child_body = str[0].strip()
				child_tags = str[1].strip()
				child_title = str[2].strip()

				child_tags = child_tags.replace("]][[","]] [[") #replace ]][[ with ]] [[

				if not ";;;" in line and add_to_end: # if there was an author name
					child_title+=author

				new_metadata = notes_metadata.replace("Topics:","Topics: " + child_tags) #add tags to metadata

				child_note_path = current_path / Path(child_title + ".md")
				with open(child_note_path, "x") as new_f: #create new file
					new_f.write(child_body) # add the body of the note
					new_f.write("\n\n\n" + new_metadata) # add metadata
					new_f.close()
				
				file_array[index] = "![[" + child_title + "]]" #update line in parent note
		f.close()

	with open(target_file, "w") as f: # write changes to the original file
		f.writelines(file_array)
		f.close()

def printResult():
	with open(target_file, "r") as f:
		for line in f:
			print(line, end='')
		print()
		f.close()

def debug(text,num):
	path = "/Users/munirv3/Documents/Main Obsidian Vault/TEXT" + str(num) + ".txt"
	with open(path, "x") as f:
		f.write(text)
		f.close()

# note_title = "The Advent of Divine Justice.md" # file to add author names to end
# author = "Shoghi Effendi"
# notes_metadata = "Source type: #book\nTitle: The Advent of Divine Justice\nAuthor: Shoghi Effendi\nTopics:\nGenre: #bahai\nDate created: Friday, January 21st 2022, 7:33 am"
# current_path = Path("/Users/munirv3/Downloads/")

note_title = str(os.environ["KMVAR_NoteTitle"]) + ".md"
author = str(os.environ["KMVAR_AuthorName"])
notes_metadata = str(os.environ["KMVAR_Metadata"])
current_path = Path(str(os.environ["KMVAR_Path"]))

target_file = current_path / Path(note_title) #full note directory

# debug("hello",1)
# debug("notes_metadata: " + notes_metadata,1)
# debug("target_file: " + str(target_file),1)


create_notes(target_file, author, notes_metadata)
# printResult()


















