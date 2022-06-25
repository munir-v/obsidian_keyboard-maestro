#!/usr/bin/env python3

import os
import sys
import pathlib #used to get working directory
from pathlib import Path #used to get working directory

articles_path = Path("/Users/munirv3/Documents/Main Obsidian Vault/Home/025 Articles.md")

def get_headers():
	with open(articles_path, "r") as f:
		file = f.readlines()
		num_headers = 0
		for line in file:
			if "###" in line:
				num_headers += 1
				print(str(num_headers) + line.replace('###',''))

def get_num_headers():
	num_headers = 0
	with open(articles_path, "r") as f:
		file = f.readlines()
		for line in file:
			if "###" in line:
				num_headers += 1
	return num_headers

def update_article_page(article_title):
	selected_header_num = int(os.environ["KMVAR_HeaderNum"])
	article_link = '- [ ] [[' + article_title + ']]'

	file = []
	with open(articles_path, "r") as f: # find next blank line after article heading to insert link
		file = f.readlines()
		num_headers = 0
		line_to_check = 0
		for i, line in enumerate(file):
			if "###" in line:
				num_headers += 1
			if selected_header_num == num_headers:
				line_to_check = i + 1
				break
		
		total_num_headers = get_num_headers()
		for i in range(line_to_check, len(file)):
			if "###" in file[i] and num_headers<total_num_headers: # check if line is empty
				num_headers += 1
				file.insert(i-1,'\n')
				file.insert(i-1,article_link)
				break
			elif num_headers == total_num_headers:
				file.append(article_link)
				break
	# print('\n'.join(file))
	with open(articles_path, "w") as f: # write changes to the original file
		f.writelines(file)

def make_new_article(article_title):
	base_path = "/Users/munirv3/Documents/Main Obsidian Vault/" + article_title + ".md"
	with open(base_path, "x") as f: # write new file
		metadata = str(os.environ["KMVAR_Metadata"])
		f.write(metadata)

def get_article_title():
	article_title = str(os.environ["KMVAR_Title"])
	article_title = filter_article_title(article_title)
	return article_title

def filter_article_title(article_title): # remove illegal symbols
	article_title = article_title.replace('/','')
	article_title = article_title.replace('\\','')
	article_title = article_title.replace(':',' -')
	article_title = article_title.replace('|',' - ')
	article_title = article_title.replace('[','')
	article_title = article_title.replace(']','')
	article_title = article_title.replace('^','')
	article_title = article_title.replace('#','')
	return article_title


function = int(os.environ["KMVAR_Function"])
if function == 0:
	get_headers()
else:
	article_title = get_article_title()
	update_article_page(article_title)
	make_new_article(article_title)
	print('Script ran successfully!')





