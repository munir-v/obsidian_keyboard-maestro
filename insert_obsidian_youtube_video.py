#!/usr/bin/env python3
import os
from string import Template #used to get working directory
import constants

audio_page = int(os.environ["KMVAR_Podcasts"])
video_title = str(os.environ["KMVAR_VideoTitle"])

if audio_page == 1:
	audio_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + '/Home/039 Podcasts and Audio.md'
else:
	audio_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/Home/035 Baha'i Audio.md"

def get_headers():
	with open(audio_path, "r") as f:
		file = f.readlines()
		num_headers = 0
		for line in file:
			if "###" in line:
				num_headers += 1
				print(str(num_headers) + line.replace('###',''))

def get_num_headers():
	num_headers = 0
	with open(audio_path, "r") as f:
		file = f.readlines()
		for line in file:
			if "###" in line:
				num_headers += 1
	return num_headers

def update_podcast_page(video_title):
	selected_header_num = int(os.environ["KMVAR_HeaderNum"])
	video_link = '- [x] [[' + video_title + ']]'

	file = []
	with open(audio_path, "r") as f: # find next blank line after article heading to insert link
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
				file.insert(i-1,video_link)
				break
			elif num_headers == total_num_headers:
				file.append('\n' + video_link)
				break
	# print('\n'.join(file))
	with open(audio_path, "w") as f: # write changes to the original file
		f.writelines(file)

def make_new_podcast_page(video_title):
	base_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + video_title + ".md"
	with open(base_path, "x") as f: # write new file
		metadata = str(os.environ["KMVAR_Metadata"])
		f.write(metadata)

def get_video_title():
	video_title = str(os.environ["KMVAR_VideoTitle"])
	video_title = filter_video_title(video_title)
	return video_title

def filter_video_title(video_title): # remove illegal symbols
	video_title = video_title.replace('/','')
	video_title = video_title.replace('\\','')
	video_title = video_title.replace(':',' -')
	video_title = video_title.replace('|',' - ')
	video_title = video_title.replace('~',' - ')
	video_title = video_title.replace('[','')
	video_title = video_title.replace(']','')
	video_title = video_title.replace('^','')
	video_title = video_title.replace('#','')
	return video_title

def get_link(file_name):
	vault_name = "Obsidian Vault"
	vault_name = vault_name.replace(' ','%20')
	file_name = file_name.replace(' ','%20')

	# provide link to note
	# https://help.obsidian.md/Advanced+topics/Using+obsidian+URI
	url_template = Template("obsidian://open?vault=$vault&file=$file.md")
	link = Template(url_template.safe_substitute(vault=vault_name))
	link = link.safe_substitute(file=file_name)
	return link

function = int(os.environ["KMVAR_Function"])
if function == 0:
	get_headers()
else:
	video_title = get_video_title()
	update_podcast_page(video_title)
	make_new_podcast_page(video_title)
	print(get_link(video_title))




