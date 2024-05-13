#!/usr/bin/env python3
import os
from pathlib import Path #used to get working directory
import constants

todolist_path = Path(os.path.expanduser(constants.OBSIDIAN_VAULT_PATH + 'To-do List.md'))

def add_todo_item():
	file = []
	with open(todolist_path, "r") as f:
		file = f.readlines()
		todo_item = str(os.environ["KMVAR_Item"])
		for i, line in enumerate(file):
			if "### To-do" in line:
				file.insert(i+1,"- [ ] " + todo_item + "\n")
				break
		else:
				file.insert(0,"- [ ] " + todo_item + "\n")

	with open(todolist_path, "w") as f: 
		f.writelines(file)

add_todo_item()