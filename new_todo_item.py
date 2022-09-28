#!/usr/bin/env python3
import os
from pathlib import Path #used to get working directory

todolist_path = Path(os.path.expanduser('~/Documents/Main Obsidian Vault/To-do List.md'))

def add_todo_item():
	file = []
	with open(todolist_path, "r") as f:
		file = f.readlines()
		for i, line in enumerate(file):
			if "### At Computer" in line:
				todo_item = str(os.environ["KMVAR_Item"])
				file.insert(i+1,"- [ ] " + todo_item + "\n")
				break
	with open(todolist_path, "w") as f: 
		f.writelines(file)

add_todo_item()